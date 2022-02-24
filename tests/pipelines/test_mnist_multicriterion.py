# flake8: noqa
import os
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

from pytest import mark

import torch
from torch import nn, optim
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn import functional as F
from torch.utils.data import DataLoader

from catalyst import dl, metrics
from catalyst.contrib.datasets import MNIST
from catalyst.settings import IS_CUDA_AVAILABLE, NUM_CUDA_DEVICES, SETTINGS
from tests import (
    DATA_ROOT,
    IS_CPU_REQUIRED,
    IS_DDP_AMP_REQUIRED,
    IS_DDP_REQUIRED,
    IS_DP_AMP_REQUIRED,
    IS_DP_REQUIRED,
    IS_GPU_AMP_REQUIRED,
    IS_GPU_REQUIRED,
)


class CustomRunner(dl.Runner):
    def predict_batch(self, batch):
        # model inference step
        return self.model(batch[0].to(self.device))

    def on_loader_start(self, runner):
        super().on_loader_start(runner)
        self.meters = {
            key: metrics.AdditiveMetric(compute_on_call=False)
            for key in ["loss", "accuracy01", "accuracy03"]
        }

    def handle_batch(self, batch):
        # model train/valid step
        # unpack the batch
        x, y = batch
        # run model forward pass
        logits = self.model(x)
        # <--- multi-criterion usage --->
        # compute the loss
        loss_multiclass = self.criterion["multiclass"](logits, y)
        loss_multilabel = self.criterion["multilabel"](
            logits, F.one_hot(y, 10).to(torch.float32)
        )
        loss = loss_multiclass + loss_multilabel
        # <--- multi-criterion usage --->
        # compute other metrics of interest
        accuracy01, accuracy03 = metrics.accuracy(logits, y, topk=(1, 3))
        # log metrics
        self.batch_metrics.update(
            {"loss": loss, "accuracy01": accuracy01, "accuracy03": accuracy03}
        )
        for key in ["loss", "accuracy01", "accuracy03"]:
            self.meters[key].update(self.batch_metrics[key].item(), self.batch_size)
        # run model backward pass
        if self.is_train_loader:
            self.engine.backward(loss)
            self.optimizer.step()
            self.optimizer.zero_grad()

    def on_loader_end(self, runner):
        for key in ["loss", "accuracy01", "accuracy03"]:
            self.loader_metrics[key] = self.meters[key].compute()[0]
        super().on_loader_end(runner)


def train_experiment(engine=None):
    with TemporaryDirectory() as logdir:

        model = nn.Sequential(nn.Flatten(), nn.Linear(28 * 28, 10))
        optimizer = optim.Adam(model.parameters(), lr=0.02)
        # <--- multi-criterion setup --->
        criterion = {
            "multiclass": nn.CrossEntropyLoss(),
            "multilabel": nn.BCEWithLogitsLoss(),
        }
        # <--- multi-criterion setup --->

        loaders = {
            "train": DataLoader(
                MNIST(DATA_ROOT, train=True),
                batch_size=32,
            ),
            "valid": DataLoader(
                MNIST(DATA_ROOT, train=False),
                batch_size=32,
            ),
        }

        runner = CustomRunner()
        # model training
        runner.train(
            engine=engine,
            model=model,
            criterion=criterion,
            optimizer=optimizer,
            loaders=loaders,
            logdir=logdir,
            num_epochs=1,
            verbose=False,
            valid_loader="valid",
            valid_metric="loss",
            minimize_valid_metric=True,
        )


def train_experiment_from_configs(*auxiliary_configs: str):
    configs_dir = Path("tests", "pipelines", "configs")
    main_config = str(configs_dir / f"{Path(__file__).stem}.yml")
    auxiliary_configs = " ".join(str(configs_dir / c) for c in auxiliary_configs)

    cmd = f"catalyst-run -C {main_config} {auxiliary_configs}"
    subprocess.run(cmd.split(), check=True)


# Device
@mark.skipif(not IS_CPU_REQUIRED, reason="CUDA device is not available")
def test_run_on_cpu():
    train_experiment(dl.CPUEngine())


@mark.skipif(not IS_CPU_REQUIRED, reason="CPU device is not available")
def test_config_run_on_cpu():
    train_experiment_from_configs("engine_cpu.yml")


@mark.skipif(
    not all([IS_GPU_REQUIRED, IS_CUDA_AVAILABLE]), reason="CUDA device is not available"
)
def test_run_on_torch_cuda0():
    train_experiment(dl.GPUEngine())


@mark.skipif(
    not all([IS_GPU_REQUIRED, IS_CUDA_AVAILABLE]), reason="CUDA device is not available"
)
def test_config_run_on_torch_cuda0():
    train_experiment_from_configs("engine_gpu.yml")


@mark.skipif(
    not all([IS_GPU_AMP_REQUIRED, IS_CUDA_AVAILABLE, SETTINGS.amp_required]),
    reason="No CUDA or AMP found",
)
def test_run_on_amp():
    train_experiment(dl.GPUEngine(fp16=True))


@mark.skipif(
    not all([IS_GPU_AMP_REQUIRED, IS_CUDA_AVAILABLE, SETTINGS.amp_required]),
    reason="No CUDA or AMP found",
)
def test_config_run_on_amp():
    train_experiment_from_configs("engine_gpu_amp.yml")


# DP
@mark.skipif(
    not all([IS_DP_REQUIRED, IS_CUDA_AVAILABLE, NUM_CUDA_DEVICES >= 2]),
    reason="No CUDA>=2 found",
)
def test_run_on_torch_dp():
    train_experiment(dl.DataParallelEngine())


@mark.skipif(
    not all([IS_DP_REQUIRED, IS_CUDA_AVAILABLE, NUM_CUDA_DEVICES >= 2]),
    reason="No CUDA>=2 found",
)
def test_config_run_on_torch_dp():
    train_experiment_from_configs("engine_dp.yml")


@mark.skipif(
    not all(
        [
            IS_DP_AMP_REQUIRED,
            IS_CUDA_AVAILABLE,
            NUM_CUDA_DEVICES >= 2,
            SETTINGS.amp_required,
        ]
    ),
    reason="No CUDA>=2 or AMP found",
)
def test_run_on_amp_dp():
    train_experiment(dl.DataParallelEngine(fp16=True))


@mark.skipif(
    not all(
        [
            IS_DP_AMP_REQUIRED,
            IS_CUDA_AVAILABLE,
            NUM_CUDA_DEVICES >= 2,
            SETTINGS.amp_required,
        ]
    ),
    reason="No CUDA>=2 or AMP found",
)
def test_config_run_on_amp_dp():
    train_experiment_from_configs("engine_dp_amp.yml")


# DDP
# @mark.skipif(
#     not all([IS_DDP_REQUIRED, IS_CUDA_AVAILABLE, NUM_CUDA_DEVICES >= 2]),
#     reason="No CUDA>=2 found",
# )
# def test_run_on_torch_ddp():
#     train_experiment(dl.DistributedDataParallelEngine())


# @mark.skipif(
#     not all([IS_DDP_REQUIRED, IS_CUDA_AVAILABLE, NUM_CUDA_DEVICES >= 2]),
#     reason="No CUDA>=2 found",
# )
# def test_config_run_on_torch_ddp():
#     train_experiment_from_configs("engine_ddp.yml")


# @mark.skipif(
#     not all(
#         [
#             IS_DDP_AMP_REQUIRED,
#             IS_CUDA_AVAILABLE,
#             NUM_CUDA_DEVICES >= 2,
#             SETTINGS.amp_required,
#         ]
#     ),
#     reason="No CUDA>=2 or AMP found",
# )
# def test_run_on_amp_ddp():
#     train_experiment(dl.DistributedDataParallelEngine(fp16=True))


# @mark.skipif(
#     not all(
#         [
#             IS_DDP_AMP_REQUIRED,
#             IS_CUDA_AVAILABLE,
#             NUM_CUDA_DEVICES >= 2,
#             SETTINGS.amp_required,
#         ]
#     ),
#     reason="No CUDA>=2 or AMP found",
# )
# def test_config_run_on_amp_ddp():
#     train_experiment_from_configs("engine_ddp_amp.yml")


# def _train_fn(local_rank, world_size):
#     process_group_kwargs = {
#         "backend": "nccl",
#         "world_size": world_size,
#     }
#     os.environ["WORLD_SIZE"] = str(world_size)
#     os.environ["RANK"] = str(local_rank)
#     os.environ["LOCAL_RANK"] = str(local_rank)
#     dist.init_process_group(**process_group_kwargs)
#     train_experiment(dl.Engine())
#     dist.destroy_process_group()


# @mark.skipif(
#     not all([IS_DDP_REQUIRED, IS_CUDA_AVAILABLE, NUM_CUDA_DEVICES >= 2]),
#     reason="No CUDA>=2 found",
# )
# def test_run_on_torch_ddp_spawn():
#     world_size: int = torch.cuda.device_count()
#     mp.spawn(
#         _train_fn,
#         args=(world_size,),
#         nprocs=world_size,
#         join=True,
#     )


# def _train_fn_amp(local_rank, world_size):
#     process_group_kwargs = {
#         "backend": "nccl",
#         "world_size": world_size,
#     }
#     os.environ["WORLD_SIZE"] = str(world_size)
#     os.environ["RANK"] = str(local_rank)
#     os.environ["LOCAL_RANK"] = str(local_rank)
#     dist.init_process_group(**process_group_kwargs)
#     train_experiment(dl.Engine(fp16=True))
#     dist.destroy_process_group()


# @mark.skipif(
#     not all(
#         [
#             IS_DDP_AMP_REQUIRED,
#             IS_CUDA_AVAILABLE,
#             NUM_CUDA_DEVICES >= 2,
#             SETTINGS.amp_required,
#         ]
#     ),
#     reason="No CUDA>=2 or AMP found",
# )
# def test_run_on_torch_ddp_amp_spawn():
#     world_size: int = torch.cuda.device_count()
#     mp.spawn(
#         _train_fn_amp,
#         args=(world_size,),
#         nprocs=world_size,
#         join=True,
#     )
#     dist.destroy_process_group()
