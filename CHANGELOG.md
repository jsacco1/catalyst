# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [YY.MM.R] - YYYY-MM-DD

### Added

-

### Changed

-

### Removed

-

### Fixed

-


## [22.02.1] - 2022-02-27

### Added

- `catalyst-run` for Config API support added [#1406](https://github.com/catalyst-team/catalyst/pull/1406)


### Fixed

- Logger API naming [#1405](https://github.com/catalyst-team/catalyst/pull/1405)


## [22.02] - 2022-02-13

### Tl;dr
- Catalyst architecture simplification.
- [#1395](https://github.com/catalyst-team/catalyst/issues/1395), [#1396](https://github.com/catalyst-team/catalyst/issues/1396), [#1397](https://github.com/catalyst-team/catalyst/issues/1397), [#1398](https://github.com/catalyst-team/catalyst/issues/1398), [#1399](https://github.com/catalyst-team/catalyst/issues/1399), [#1400](https://github.com/catalyst-team/catalyst/issues/1400), [#1401](https://github.com/catalyst-team/catalyst/issues/1401), [#1402](https://github.com/catalyst-team/catalyst/issues/1402), [#1403](https://github.com/catalyst-team/catalyst/issues/1403).

### Added

- Additional tests for different hardware accelerators setups. Please check out the `tests/pipelines` folder for more information.
- `BackwardCallback` and `BackwardCallbackOrder` as an abstraction on top of `loss.backward`. Now you could easily log model gradients or transform them before `OptimizerCallback`.
- `CheckpointCallbackOrder` for `ICheckpointCallback`.

### Changed

- Minimal python version moved to `3.7`, minimal pytorch version moved to `1.4.0`.
- Engines rewritten on top of Accelerate. First, we found these two abstractions very close to each other. Second, Accelerate provides additional user-friendly API and more stable API for "Nvidia APEX" and "Facebook Fairscale" - it does not support them.
- SelfSupervisedRunner moved to the `examples` folder from the Catalyst API. The only Runners API, that will be supported in the future: `IRunner`, `Runner`, `ISupervisedRunner`, `SupervisedRunner` due to their consistency. If you are interested in any other Runner API - feel free to write your own `CustomRunner` and use `SelfSupervisedRunner` as an example.
- `Runner.{global/stage}_{batch/loader/epoch}_metrics` renamed to `Runner.{batch/loader/epoch}_metrics`
- `CheckpointCallback` rewritten from scratch.
- Catalyst registry moved to full-imports-paths only.
- Logger API changed to receive `IRunner` for all `log_*` methods.
- Metric API: `topk_args` renamed to `topk`
- Contrib API: init imports from `catalyst.contrib` - removed, use `from catalyst.contrib.{smth} import {smth}`. Could be change to full-imports-only in future versions for stability.
- All quickstarts, minimal examples, notebooks and pipelines moved to new version.
- Codestyle moved to `89` right margin. Honestly speaking, it's much easier to maintain Catalyst with `89` right margin on MBP'16.

### Removed

- `ITrial` removed.
- Stages support removed. While we embrace stages in deep learning experiments, current hardware accelerators are not prepared well for such setups. Additionally, ~95% of dl pipelines are single-stage. Multi-stage runner support is under review. For multi-stage support, please define a `CustomRunner` with rewritten API.
- Config/Hydra API support removed. Config API is under review. For now, you could write your own Config API with [hydra-slayer](https://github.com/catalyst-team/hydra-slayer) if needed.
- `catalyst-dl` scripts removed. Without Config API we don't need them anymore.
- `Nvidia Apex`, `Fairscale`, `Albumentations`, `Nifti`, `Hydra` requiremets removed.
- `OnnxCallback`, `PruningCallback`, `QuantizationCallback`, `TracingCallback` removed from callbacks API. Theese callbacks are under review now.

If you have any questions on the Catalyst 22 edition updates, please join Catalyst slack for discussion.


## [21.12] - 2021-12-28

### Added

- MNIST dataset for SSL banchmark ([#1368](https://github.com/catalyst-team/catalyst/pull/1368))
- MoveiLens 20M dataset [#1336](https://github.com/catalyst-team/catalyst/pull/1336)
- logger property for logging customization ([#1372](https://github.com/catalyst-team/catalyst/pull/1372))
- MacridVAE example ([#1363](https://github.com/catalyst-team/catalyst/pull/1363))
- SSL benchmark results ([#1374](https://github.com/catalyst-team/catalyst/pull/1374))
- Neptune example ([#1377](https://github.com/catalyst-team/catalyst/pull/1377))
- multi-node support for engines ([#1364](https://github.com/catalyst-team/catalyst/pull/1364))

### Changed

- RL examples update to last version ([#1370](https://github.com/catalyst-team/catalyst/pull/1370))
- DDPLoaderWrapper updated to new version ([#1385](https://github.com/catalyst-team/catalyst/pull/1385))
- `num_classes` for classification metrics became optional ([#1379](https://github.com/catalyst-team/catalyst/pull/1379))
- colab ci/cd update to new verion

### Removed

-

### Fixed

- `requests` requirements for `catalyst[cv]` added ([#1371](https://github.com/catalyst-team/catalyst/pull/1370))
- loader step counter ([#1374](https://github.com/catalyst-team/catalyst/pull/1374))
- detection example data preprocessing ([#1369](https://github.com/catalyst-team/catalyst/pull/1369))
- gradient clipping with fp16 runs ([#1378](https://github.com/catalyst-team/catalyst/pull/1378))
- config API fix for DDP runs ([#1383](https://github.com/catalyst-team/catalyst/pull/1383))
- checkpoint creation for fp16 engines ([#1382](https://github.com/catalyst-team/catalyst/pull/1382))

## [21.11] - 2021-11-30

### Added

- MultiVAE RecSys example ([#1340](https://github.com/catalyst-team/catalyst/pull/1340))
- Returned `resume` support - resolved [#1193](https://github.com/catalyst-team/catalyst/issues/1193) ([#1349](https://github.com/catalyst-team/catalyst/pull/1349))
- Smoothing dice loss to contrib ([#1344](https://github.com/catalyst-team/catalyst/pull/1344))
- `profile` flag for `runner.train` ([#1348](https://github.com/catalyst-team/catalyst/pull/1348))
- MultiDAE RecSys example ([#1356](https://github.com/catalyst-team/catalyst/pull/1356))
- `SETTINGS.log_batch_metrics`, `SETTINGS.log_epoch_metrics`, `SETTINGS.compute_per_class_metrics` for framework-wise  Metric & Logger APIs specification ([#1357](https://github.com/catalyst-team/catalyst/pull/1357))
- `log_batch_metrics` and `log_epoch_metrics` options for all available Loggers ([#1357](https://github.com/catalyst-team/catalyst/pull/1357))
- `compute_per_class_metrics` option for all available multiclass/label metrics ([#1357](https://github.com/catalyst-team/catalyst/pull/1357))
- pytorch benchmark script and simplified MNIST ([#1360](https://github.com/catalyst-team/catalyst/pull/1360))

### Changed

- A few framework simplifications were made ([#1346](https://github.com/catalyst-team/catalyst/pull/1346)):
  - `catalyst-contrib` scripts reduced to `collect-env` and `project-embeddings` only
  - `catalyst-dl` scripts recuded to `run` and `tune` only
  - `transforms.` prefix deprecated for Catalyst-based transforms
  - `catalyst.tools` moved to `catalyst.extras`
  - task-dependent extensions from `catalyst.data` moved to `catalyst.contrib.data`
  - `catalyst.data.transforms` moved to `catalyst.contrib.data.transforms`
  - `Normalize`, `ToTensor` transforms renamed to `NormalizeImage`, `ImageToTensor`
  - metric learning extensions moved to `catalyst.contrib.data`
  - `catalyst.contrib` moved to code-as-a-documentation development
  - `catalyst[cv]` and `catalyst[ml]` extensions moved to flatten architecture design; examples: `catalyst.contrib.data.dataset_cv`, `catalyst.contrib.data.dataset_ml`
  - `catalyst.contrib` moved to flatten architecture design; exampels: `catalyst.contrib.data`, `catalyst.contrib.datasets`, `catalyst.contrib.layers`, `catalyst.contrib.models`, `catalyst.contrib.optimizers`, `catalyst.contrib.schedulers`
  - internal functionality moved to `***._misc` modules
  - `catalyst.utils.mixup` moved to `catalyst.utils.torch`
  - `catalyst.utils.numpy` moved to `catalyst.contrib.utils.numpy`
- default logging logic moved from "batch & epoch" to "epoch"-only to save computation time during logging; to respecify, please use:
  - `SETTINGS.log_batch_metrics=True/False` or `os.environ["CATALYST_LOG_BATCH_METRICS"]`
  - `SETTINGS.log_epoch_metrics=True/False` or `os.environ["CATALYST_LOG_EPOCH_METRICS"]`
- default metrics computation moved from "per-class & aggregations" to "aggregations"-only to save computation time during logging; to respecify, please use:
  - `SETTINGS.compute_per_class_metrics=True/False` or `os.environ["CATALYST_COMPUTE_PER_CLASS_METRICS"]`
- no transformations required for MNIST contrib dataset ([#1360](https://github.com/catalyst-team/catalyst/pull/1360)

### Removed

- A few framework simplifications were made ([#1346](https://github.com/catalyst-team/catalyst/pull/1346)):
  - `catalyst.contrib.pandas`
  - `catalyst.contrib.parallel`
  - `catalyst.contrib.models.cv`
  - a few `catalyst.utils.misc` functions
  - `catalyst.extras` removed from the public documentation


### Fixed

- documentation search error (21.10 only) ([#1346](https://github.com/catalyst-team/catalyst/pull/1346))
- docs examples ([#1362](https://github.com/catalyst-team/catalyst/pull/1362))
- Self-Supervised benchmark: ([#1365](https://github.com/catalyst-team/catalyst/pull/1365)), ([#1361](https://github.com/catalyst-team/catalyst/pull/1361))


## [21.10] - 2021-10-30

### Added

- RSquareLoss ([#1313](https://github.com/catalyst-team/catalyst/pull/1313))
- Self-Supervised example updates: ([#1305](https://github.com/catalyst-team/catalyst/pull/1305)), ([#1322](https://github.com/catalyst-team/catalyst/pull/1322)), ([#1325](https://github.com/catalyst-team/catalyst/pull/1325)), ([#1335](https://github.com/catalyst-team/catalyst/pull/1335))
- Albert training example ([#1326](https://github.com/catalyst-team/catalyst/pull/1326))
- YOLO-X (new) detection example and refactoring ([#1324](https://github.com/catalyst-team/catalyst/pull/1324))
- `TopKMetric` abstraction ([#1330](https://github.com/catalyst-team/catalyst/pull/1330))

### Changed

- simlified readme ([#1312](https://github.com/catalyst-team/catalyst/pull/1312))
- improved DDP tutorial ([#1327](https://github.com/catalyst-team/catalyst/pull/1327))
- `CMCMetric` renamed from `<prefix>cmc<suffix><k>` to `<prefix>cmc<k><suffix>` ([#1330](https://github.com/catalyst-team/catalyst/pull/1330))

### Removed

-

### Fixed

- Zero seed error ([#1329](https://github.com/catalyst-team/catalyst/pull/1329))
- updated codestyle issues ([#1331](https://github.com/catalyst-team/catalyst/pull/1331))
- TopK metrics: ([#1330](https://github.com/catalyst-team/catalyst/pull/1330)), ([#1334](https://github.com/catalyst-team/catalyst/pull/1334)), ([#1339](https://github.com/catalyst-team/catalyst/pull/1339))
- `--expdir` param for `catalyst-dl run` ([#1338](https://github.com/catalyst-team/catalyst/pull/1338))
- ControlFlowCallback for distributed setup ([#1341](https://github.com/catalyst-team/catalyst/pull/1341))


## [21.09] - 2021-09-30

### Added

- CometLogger support ([#1283](https://github.com/catalyst-team/catalyst/pull/1283))
- CometLogger examples ([#1287](https://github.com/catalyst-team/catalyst/pull/1287))
- XLA docs ([#1288](https://github.com/catalyst-team/catalyst/pull/1288))
- Contarstive loss functions: `NTXentLoss` ([#1278](https://github.com/catalyst-team/catalyst/pull/1278)), `SupervisedContrastiveLoss` ([#1293](https://github.com/catalyst-team/catalyst/pull/1293))
- Self supervised learning: `ISelfSupervisedRunner`, `SelfSupervisedConfigRunner`, `SelfSupervisedRunner`, `SelfSupervisedDatasetWrapper` ([#1278](https://github.com/catalyst-team/catalyst/pull/1278))
- SimCLR example ([#1278](https://github.com/catalyst-team/catalyst/pull/1278))
- Superivised Contrastive example ([#1293](https://github.com/catalyst-team/catalyst/pull/1293))
- extra warnings for runner-callbacks interaction ([#1295](https://github.com/catalyst-team/catalyst/pull/1295))
- `CategoricalRegressionLoss` and `QuantileRegressionLoss` to the `contrib` ([#1295](https://github.com/catalyst-team/catalyst/pull/1295))
- R2 score metric ([#1274](https://github.com/catalyst-team/catalyst/pull/1274))


### Changed
- Improved `WandbLogger` to support artifacts and fix logging steps ([#1309](https://github.com/catalyst-team/catalyst/pull/1309))
- full `Runner` cleanup, with callbacks and loaders destruction, moved to `PipelineParallelFairScaleEngine` only ([#1295](https://github.com/catalyst-team/catalyst/pull/1295))
- `HuberLoss` renamed to `HuberLossV0` for the PyTorch compatibility ([#1295](https://github.com/catalyst-team/catalyst/pull/1295))
- codestyle update ([#1298](https://github.com/catalyst-team/catalyst/pull/1298))
- BalanceBatchSampler - deprecated ([#1303](https://github.com/catalyst-team/catalyst/pull/1303))

### Removed

-

### Fixed

- CI/CD ([#1292](https://github.com/catalyst-team/catalyst/pull/1292)), ([#1299](https://github.com/catalyst-team/catalyst/pull/1299)), ([#1304](https://github.com/catalyst-team/catalyst/pull/1304)), ([#1306](https://github.com/catalyst-team/catalyst/pull/1306))
- Optuna configs ([#1296](https://github.com/catalyst-team/catalyst/pull/1292)), ([#1296](https://github.com/catalyst-team/catalyst/pull/1299))


## [21.08] - 2021-08-31

### Added

- RecSys loss functions: `AdaptiveHingeLoss`, `BPRLoss`, `HingeLoss`, `LogisticLoss`, `RocStarLoss`, `WARPLoss` ([#1269](https://github.com/catalyst-team/catalyst/pull/1269), [#1282](https://github.com/catalyst-team/catalyst/pull/1282))
- object detection examples ([#1271](https://github.com/catalyst-team/catalyst/pull/1271))
- SklearnModelCallback ([#1261](https://github.com/catalyst-team/catalyst/pull/1261))
- Barlow Twins example ([#1261](https://github.com/catalyst-team/catalyst/pull/1261))
- TPU/XLA support ([#1275](https://github.com/catalyst-team/catalyst/pull/1275))
  - with updated [example](./examples/engines)
- native `sync_bn` support for all available engines ([#1275](https://github.com/catalyst-team/catalyst/pull/1275))
  - Torch, AMP, Apex, FairScale

### Changed

- Registry moved to `hydra-slayer` ([#1264)](https://github.com/catalyst-team/catalyst/pull/1264))
- ([#1275](https://github.com/catalyst-team/catalyst/pull/1275))
  - batch metrics sync removed from ddp-runs to speedup training process
  - `AccumulationMetric` renamed to `AccumulativeMetric`
    - moved from `catalyst.metrics._metric` to `catalyst.metrics._accumulative`
    - `accululative_fields` renamed to `keys`


### Removed

-

### Fixed

- PeriodicLoaderCallback docsting ([#1279](https://github.com/catalyst-team/catalyst/pull/1279))
- matplotlib issue ([#1272](https://github.com/catalyst-team/catalyst/pull/1272))
- sample counter for the loader ([#1285](https://github.com/catalyst-team/catalyst/pull/1285))


## [21.07] - 2021-07-29

### Added

- added `pre-commit` hook to run codestyle checker on commit ([#1257](https://github.com/catalyst-team/catalyst/pull/1257))
- `on publish` github action for docker and docs added ([#1260](https://github.com/catalyst-team/catalyst/pull/1260))
- MixupCallback and `utils.mixup_batch` ([#1241](https://github.com/catalyst-team/catalyst/pull/1241))
- Barlow twins loss ([#1259](https://github.com/catalyst-team/catalyst/pull/1259))
- BatchBalanceClassSampler ([#1262](https://github.com/catalyst-team/catalyst/pull/1262))

### Changed

-

### Removed

-

### Fixed

- make `expdir` in `catalyst-dl run` optional ([#1249](https://github.com/catalyst-team/catalyst/pull/1249))
- Bump neptune-client from 0.9.5 to 0.9.8 in `requirements-neptune.txt` ([#1251](https://github.com/catalyst-team/catalyst/pull/1251))
- automatic merge for master (with [Mergify](https://mergify.io/)) fixed ([#1250](https://github.com/catalyst-team/catalyst/pull/1250))
- Evaluate loader custom model bug was fixed ([#1254](https://github.com/catalyst-team/catalyst/pull/1254))
- `BatchPrefetchLoaderWrapper` issue with batch-based PyTorch samplers ([#1262](https://github.com/catalyst-team/catalyst/pull/1262))
- Adapted MlflowLogger for new config hierarchy ([#1263](https://github.com/catalyst-team/catalyst/pull/1263))


## [21.06] - 2021-06-29

### Added

- ([#1230](https://github.com/catalyst-team/catalyst/pull/1230))
  - FairScale support
  - DeepSpeed support
  - `utils.ddp_sync_run` function for synchronous ddp run
  - CIFAR10 and CIFAR100 datasets from torchvision (no cv-based requirements)
  - [Catalyst Engines demo](https://github.com/catalyst-team/catalyst/tree/master/examples/engines)
- `dataset_from_params` support in config API ([#1231](https://github.com/catalyst-team/catalyst/pull/1231))
- transform from params support for config API added ([#1236](https://github.com/catalyst-team/catalyst/pull/1236))
- samplers from params support for config API added ([#1240](https://github.com/catalyst-team/catalyst/pull/1240))
- recursive registry.get_from_params added ([#1241](https://github.com/catalyst-team/catalyst/pull/1241))
- albumentations integration ([#1238](https://github.com/catalyst-team/catalyst/pull/1238))
- Profiler callback ([#1226](https://github.com/catalyst-team/catalyst/pull/1226))

### Changed

- ([#1230](https://github.com/catalyst-team/catalyst/pull/1230))
  - loaders creation now wrapper with `utils.ddp_sync_run` for `utils.ddp_sync_run` data preparation
  - runner support stage cleanup: loaders and callbacks will be deleted on the stage end
  - Apex-based engines now support both APEXEngine and ApexEngine registry names

### Removed

-

### Fixed

- multiprocessing in minimal tests hotfix ([#1232](https://github.com/catalyst-team/catalyst/pull/1232))
- Tracing callback hotfix ([#1234](https://github.com/catalyst-team/catalyst/pull/1234))
- Engine hotfix for `predict_loader` ([#1235](https://github.com/catalyst-team/catalyst/pull/1235))
- ([#1230](https://github.com/catalyst-team/catalyst/pull/1230))
  - Hydra hotfix due to `1.1.0` version changes
- `HuberLoss` name conflict for pytorch 1.9 hotfix ([#1239](https://github.com/catalyst-team/catalyst/pull/1239))


## [21.05] - 2021-05-31

### Added

- Reinforcement learning tutorials ([#1205](https://github.com/catalyst-team/catalyst/pull/1205))
- customization demo ([#1207](https://github.com/catalyst-team/catalyst/pull/1207))
- FAQ docs: multiple input and output keys, engine tutorial ([#1202](https://github.com/catalyst-team/catalyst/pull/1202))
- minimal Config API example ([#1215](https://github.com/catalyst-team/catalyst/pull/1215))
- Distributed RL example (Catalyst.RL 2.0 concepts) ([#1224](https://github.com/catalyst-team/catalyst/pull/1224))
- SklearnCallback as integration of sklearn metrics ([#1198](https://github.com/catalyst-team/catalyst/pull/1198))

### Changed

- tests moved to `tests` folder ([#1208](https://github.com/catalyst-team/catalyst/pull/1208))
- pipeline tests moved to `tests/pipelines` ([#1215](https://github.com/catalyst-team/catalyst/pull/1215))
- updated NeptuneLogger docstrings ([#1223](https://github.com/catalyst-team/catalyst/pull/1223))

### Removed

-

### Fixed

- customizing what happens in `train()` notebook ([#1203](https://github.com/catalyst-team/catalyst/pull/1203))
- transforms imports under catalyst.data ([#1211](https://github.com/catalyst-team/catalyst/pull/1211))
- change layerwise to layerwise_params ([#1210](https://github.com/catalyst-team/catalyst/pull/1210))
- add torch metrics support ([#1195](https://github.com/catalyst-team/catalyst/issues/1195))
- add Config API support for BatchTransformCallback ([#1209](https://github.com/catalyst-team/catalyst/issues/1209))


## [21.04.2] - 2021-04-30

### Added

- Weights and Biases Logger (``WandbLogger``) ([#1176](https://github.com/catalyst-team/catalyst/pull/1176))
- Neptune Logger (``NeptuneLogger``) ([#1196](https://github.com/catalyst-team/catalyst/pull/1196))
- `log_artifact` method for logging arbitrary files like audio, video, or model weights to `ILogger` and `IRunner` ([#1196](https://github.com/catalyst-team/catalyst/pull/1196))

## [21.04/21.04.1] - 2021-04-17

### Added

- Nifti Reader (NiftiReader) ([#1151](https://github.com/catalyst-team/catalyst/pull/1151))
- CMC score and callback for ReID task (ReidCMCMetric and ReidCMCScoreCallback) ([#1170](https://github.com/catalyst-team/catalyst/pull/1170))
- Market1501 metric learning datasets (Market1501MLDataset and Market1501QGDataset) ([#1170](https://github.com/catalyst-team/catalyst/pull/1170))
- extra kwargs support for Engines ([#1156](https://github.com/catalyst-team/catalyst/pull/1156))
- engines exception for unknown model type ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))
- a few docs to the supported loggers ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))

### Changed

- ``TensorboardLogger`` switched from ``global_batch_step`` counter to ``global_sample_step`` one ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))
- ``TensorboardLogger`` logs loader metric ``on_loader_end`` rather than ``on_epoch_end`` ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))
- ``prefix`` renamed to ``metric_key`` for ``MetricAggregationCallback`` ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))
- ``micro``, ``macro`` and ``weighted`` aggregations renamed to ``_micro``, ``_macro`` and ``_weighted`` ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))
- ``BatchTransformCallback`` updated ([#1153](https://github.com/catalyst-team/catalyst/issues/1153))

### Removed

- auto ``torch.sigmoid`` usage for ``metrics.AUCMetric`` and ``metrics.auc`` ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))

### Fixed

- hitrate calculation issue ([#1155](https://github.com/catalyst-team/catalyst/issues/1155))
- ILoader wrapper usage issue with Runner ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))
- counters for ddp case ([#1174](https://github.com/catalyst-team/catalyst/issues/1174))

## [21.03.2] - 2021-03-29

### Fixed

- minimal requirements issue ([#1147](https://github.com/catalyst-team/catalyst/issues/1147))
- nested dicts in `loaders_params`/`samplers_params` overriding ([#1150](https://github.com/catalyst-team/catalyst/pull/1150))

## [21.03.1] - 2021-03-28

### Added

- Additive Margin SoftMax(AMSoftmax) ([#1125](https://github.com/catalyst-team/catalyst/issues/1125))
- Generalized Mean Pooling(GeM) ([#1084](https://github.com/catalyst-team/catalyst/issues/1084))
- Key-value support for CriterionCallback ([#1130](https://github.com/catalyst-team/catalyst/issues/1130))
- Engine configuration through cmd ([#1134](https://github.com/catalyst-team/catalyst/issues/1134))
- Extra utils for thresholds ([#1134](https://github.com/catalyst-team/catalyst/issues/1134))
- Added gradient clipping function to optimizer callback ([1124](https://github.com/catalyst-team/catalyst/pull/1124))
- FactorizedLinear to contrib ([1142](https://github.com/catalyst-team/catalyst/pull/1142))
- Extra init params for ``ConsoleLogger`` ([1142](https://github.com/catalyst-team/catalyst/pull/1142))
- Tracing, Quantization, Onnx, Pruninng Callbacks ([1127](https://github.com/catalyst-team/catalyst/pull/1127))


### Changed

- CriterionCallback now inherits from BatchMetricCallback [#1130](https://github.com/catalyst-team/catalyst/issues/1130))
    - united metrics computation logic

### Removed

- Config API deprecated parsings logic ([1142](https://github.com/catalyst-team/catalyst/pull/1142)) ([1138](https://github.com/catalyst-team/catalyst/pull/1138))

### Fixed

- Data-Model device sync and ``Engine`` logic during `runner.predict_loader` ([#1134](https://github.com/catalyst-team/catalyst/issues/1134))
- BatchLimitLoaderWrapper logic for loaders with shuffle flag ([#1136](https://github.com/catalyst-team/catalyst/issues/1136))
- config description in the examples ([1142](https://github.com/catalyst-team/catalyst/pull/1142))
- Config API deprecated parsings logic ([1142](https://github.com/catalyst-team/catalyst/pull/1142)) ([1138](https://github.com/catalyst-team/catalyst/pull/1138))
- RecSys metrics Top_k calculations ([#1140](https://github.com/catalyst-team/catalyst/pull/1140))
- `_key_value` for schedulers in case of multiple optimizers ([#1146](https://github.com/catalyst-team/catalyst/pull/1146))

## [21.03] - 2021-03-13 ([#1095](https://github.com/catalyst-team/catalyst/issues/1095))

### Added

- [``Engine`` abstraction](https://catalyst-team.github.io/catalyst/api/engines.html) to support various hardware backends and accelerators: CPU, GPU, multi GPU, distributed GPU, TPU, Apex, and AMP half-precision training.
- [``Logger`` abstraction](https://catalyst-team.github.io/catalyst/api/loggers.html) to support various monitoring tools: console, tensorboard, MLflow, etc.
- ``Trial`` abstraction to support various hyperoptimization tools: Optuna, Ray, etc.
- [``Metric`` abstraction](https://catalyst-team.github.io/catalyst/api/metrics.html) to support various of machine learning metrics: classification, segmentation, RecSys and NLP.
- Full support for Hydra API.
- Full DDP support for Python API.
- MLflow support for metrics logging.
- United API for model post-processing: tracing, quantization, pruning, onnx-exporting.
- United API for metrics: classification, segmentation, RecSys, and NLP with full DDP and micro/macro/weighted/etc aggregations support.

### Changed

- ``Experiment`` abstraction merged into ``Runner`` one.
- Runner, SupervisedRunner, ConfigRunner, HydraRunner architectures and dependencies redesigned.
- Internal [settings](https://github.com/catalyst-team/catalyst/blob/master/catalyst/settings.py) and [registry](https://github.com/catalyst-team/catalyst/blob/master/catalyst/registry.py) mechanisms refactored to be simpler, user-friendly and more extendable.
- Bunch of Config API test removed with Python API and pytest.
- Codestyle now supports up to 99 symbols per line :)
- All callbacks/runners moved for contrib to the library core if was possible.
- ``Runner`` abstraction simplified to store only current state of the experiment run: all validation logic was moved to the callbacks (by this way, you could easily select best model on various metrics simultaneously).
- ``Runner.input`` and ``Runner.output`` merged into united ``Runner.batch`` storage for simplicity.
- All metric moved from ``catalyst.utils.metrics`` to ``catalyst.metrics``.
- All metrics now works on scores/metric-defined-input rather that logits (!).
- Logging logic moved from ``Callbacks`` to appropriate ``Loggers``.
- ``KorniaCallbacks`` refactored to ``BatchTransformCallback``.

### Removed

- Lots of unnecessary contrib extensions.
- Transforms configuration support through Config API (could be returned in next releases).
- Integrated Python cmd command for model pruning, swa, etc (should be returned in next releases).
- ``CallbackOrder.Validation`` and ``CallbackOrder.Logging``
- All 2020 year backward compatibility fixes and legacy support.

### Fixed

- Docs rendering simplified.
- LrFinderCallback.

[Release docs](https://catalyst-team.github.io/catalyst/v21.03/index.html),
[Python API minimal examples](https://github.com/catalyst-team/catalyst#minimal-examples),
[Config/Hydra API example](https://github.com/catalyst-team/catalyst/tree/master/examples/mnist_stages).

## [20.12.1] - XXXX-XX-XX


### Added

- Inference mode for face layers ([#1045](https://github.com/catalyst-team/catalyst/pull/1045))

### Fixed

- Fix bug in `OptimizerCallback` when mixed-precision params set both:
  in callback arguments and in distributed_params  ([#1042](https://github.com/catalyst-team/catalyst/pull/1042))


## [20.12] - 2020-12-20

### Added

- CVS Logger ([#1005](https://github.com/catalyst-team/catalyst/pull/1005))
- DrawMasksCallback ([#999](https://github.com/catalyst-team/catalyst/pull/999))
- ([#1002](https://github.com/catalyst-team/catalyst/pull/1002))
    - a few docs
- ([#998](https://github.com/catalyst-team/catalyst/pull/998))
    - ``reciprocal_rank`` metric
    - unified recsys metrics preprocessing
-  ([#1018](https://github.com/catalyst-team/catalyst/pull/1018))
    - readme examples for all supported metrics under ``catalyst.metrics``
    - ``wrap_metric_fn_with_activation`` for model outputs wrapping with activation
    -  extra tests for metrics
- ([#1039](https://github.com/catalyst-team/catalyst/pull/1039))
    - ``per_class=False`` option for metrics callbacks
    - ``PrecisionCallack``, ``RecallCallack`` for multiclass problems
    - extra docs

### Changed

- docs update ([#1000](https://github.com/catalyst-team/catalyst/pull/1000))
- ``AMPOptimizerCallback`` and ``OptimizerCallback`` were merged ([#1007](https://github.com/catalyst-team/catalyst/pull/1007))
- ([#1017](https://github.com/catalyst-team/catalyst/pull/1017))
    - fixed bug in `SchedulerCallback`
    - Log LRs and momentums for all param groups, not only for the first one
- ([#1002](https://github.com/catalyst-team/catalyst/pull/1002))
    - ``tensorboard, ipython, matplotlib, pandas, scikit-learn`` moved to optional requirements
    - ``PerplexityMetricCallback`` moved to ``catalyst.callbacks`` from ``catalyst.contrib.callbacks``
    - ``PerplexityMetricCallback`` renamed to ``PerplexityCallback``
    - ``catalyst.contrib.utils.confusion_matrix`` renamed to ``catalyst.contrib.utils.torch_extra``
    - many parts of ``catalyst.data`` moved to ``catalyst.contrib.data``
    - ``catalyst.data.scripts`` moved to ``catalyst.contrib.scripts``
    - ``catalyst.utils``, ``catalyst.data.utils`` and ``catalyst.contrib.utils`` restructured
    - ``ReaderSpec`` renamed to ``IReader``
    - ``SupervisedExperiment`` renamed to ``AutoCallbackExperiment``
- gain functions renamed for ``dcg``/``ndcg`` metrics ([#998](https://github.com/catalyst-team/catalyst/pull/998))
- ([#1014](https://github.com/catalyst-team/catalyst/pull/1014))
    - requirements respecification: ``catalyst[cv]``, ``catalyst[dev]``, ``catalyst[log]``, ``catalyst[ml]``, ``catalyst[nlp]``,``catalyst[tune]``
    - settings respecification
    - extra tests for settings
    - contrib refactoring
- iou and dice metrics moved to per-class computation ([#1031](https://github.com/catalyst-team/catalyst/pull/1031))

### Removed

- ([#1002](https://github.com/catalyst-team/catalyst/pull/1002))
    - ``KNNMetricCallback``
    - ``sklearn`` mode for ``ConfusionMatrixLogger``
    - ``catalyst.data.utils``
    - unnecessary ``catalyst.tools.meters``
    - todos for unnecessary docs
- ([#1014](https://github.com/catalyst-team/catalyst/pull/1014))
    - transformers-based contrib (too unstable)
- ([#1018](https://github.com/catalyst-team/catalyst/pull/1014))
    - ClasswiseIouCallback/ClasswiseJaccardCallback as deprecated on (should be refactored in future releases)



### Fixed

- prevented modifying config during the experiment and runner initialization ([#1004](https://github.com/catalyst-team/catalyst/pull/1004))
- a few test for RecSys MAP computation ([#1018](https://github.com/catalyst-team/catalyst/pull/1014))
- leave batch size the same for default distributed training ([#1023](https://github.com/catalyst-team/catalyst/issues/1023))
- ([#1032](https://github.com/catalyst-team/catalyst/pull/1032))
  - Apex: now you can use apex for multiple models training
  - Apex: DataParallel is allowed for opt_level other than "O1"



## [20.11] - 2020-11-12

### Added
- DCG, nDCG metrics ([#881](https://github.com/catalyst-team/catalyst/pull/881))
- MAP calculations [#968](https://github.com/catalyst-team/catalyst/pull/968)
- hitrate calculations [#975] (https://github.com/catalyst-team/catalyst/pull/975)
- extra functions for classification metrics ([#966](https://github.com/catalyst-team/catalyst/pull/966))
- `OneOf` and `OneOfV2` batch transforms ([#951](https://github.com/catalyst-team/catalyst/pull/951))
- ``precision_recall_fbeta_support`` metric ([#971](https://github.com/catalyst-team/catalyst/pull/971))
- Pruning tutorial ([#987](https://github.com/catalyst-team/catalyst/pull/987))
- BatchPrefetchLoaderWrapper ([#986](https://github.com/catalyst-team/catalyst/pull/986))
- DynamicBalanceClassSampler ([#954](https://github.com/catalyst-team/catalyst/pull/954))

### Changed

- update Catalyst version to `20.10.1` for tutorials ([#967](https://github.com/catalyst-team/catalyst/pull/967))
- added link to dl-course ([#967](https://github.com/catalyst-team/catalyst/pull/967))
- ``IRunner`` -> simplified ``IRunner`` ([#984](https://github.com/catalyst-team/catalyst/pull/984))
- docs were restructured ([#985](https://github.com/catalyst-team/catalyst/pull/985))
- `set_global_seed` moved from `utils.seed` to `utils.misc` ([#986](https://github.com/catalyst-team/catalyst/pull/986))

### Removed

- several deprecated tutorials ([#967](https://github.com/catalyst-team/catalyst/pull/967))
- several deprecated func from utils.misc ([#986](https://github.com/catalyst-team/catalyst/pull/986))

### Fixed

- `BatchTransformCallback` - add `nn.Module` transforms support ([#951](https://github.com/catalyst-team/catalyst/pull/951))
- moved to `contiguous` view for accuracy computation ([#982](https://github.com/catalyst-team/catalyst/pull/982))
- fixed torch warning on `optimizer.py:140` ([#979](https://github.com/catalyst-team/catalyst/pull/979))


## [20.10.1] - 2020-10-15

### Added

- MRR metrics calculation ([#886](https://github.com/catalyst-team/catalyst/pull/886))
- docs for MetricCallbacks ([#947](https://github.com/catalyst-team/catalyst/pull/947))
- SoftMax, CosFace, ArcFace layers to contrib ([#939](https://github.com/catalyst-team/catalyst/pull/939))
- ArcMargin layer to contrib ([#957](https://github.com/catalyst-team/catalyst/pull/957))
- AdaCos to contrib ([#958](https://github.com/catalyst-team/catalyst/pull/958))
- Manual SWA to utils ([#945](https://github.com/catalyst-team/catalyst/pull/945))

### Changed

- fixed path to `CHANGELOG.md` file and add information about unit test to `PULL_REQUEST_TEMPLATE.md` ([#955])(https://github.com/catalyst-team/catalyst/pull/955)
- `catalyst-dl tune` config specification - now optuna params are grouped under `study_params` ([#947](https://github.com/catalyst-team/catalyst/pull/947))
- `IRunner._prepare_for_stage` logic moved to `IStageBasedRunner.prepare_for_stage` ([#947](https://github.com/catalyst-team/catalyst/pull/947))
    - now we create components in the following order: datasets/loaders, model, criterion, optimizer, scheduler, callbacks
- `MnistMLDataset` and `MnistQGDataset` data split logic - now targets of the datasets are disjoint ([#949](https://github.com/catalyst-team/catalyst/pull/949))
- architecture redesign ([#953](https://github.com/catalyst-team/catalyst/pull/953))
    - experiments, runners, callbacks grouped by primitives under `catalyst.experiments`/`catalyst.runners`/`catalyst.callbacks` respectively
    - settings and typing moved from `catalyst.tools.*` to `catalyst.*`
    - utils moved from `catalyst.*.utils` to `catalyst.utils`
- swa moved to `catalyst.utils` ([#963](https://github.com/catalyst-team/catalyst/pull/963))

### Removed

-

### Fixed

- `AMPOptimizerCallback` - fix grad clip fn support ([#948](https://github.com/catalyst-team/catalyst/pull/948))
- removed deprecated docs types ([#947](https://github.com/catalyst-team/catalyst/pull/947)) ([#952](https://github.com/catalyst-team/catalyst/pull/952))
- docs for a few files ([#952](https://github.com/catalyst-team/catalyst/pull/952))
- extra backward compatibility fixes ([#963](https://github.com/catalyst-team/catalyst/pull/963))


## [20.09.1] - 2020-09-25

### Added

- Runner registry support for Config API ([#936](https://github.com/catalyst-team/catalyst/pull/936))
- `catalyst-dl tune` command - Optuna with Config API integration for AutoML hyperparameters optimization ([#937](https://github.com/catalyst-team/catalyst/pull/937))
- `OptunaPruningCallback` alias for `OptunaCallback` ([#937](https://github.com/catalyst-team/catalyst/pull/937))
- AdamP and SGDP to `catalyst.contrib.losses` ([#942](https://github.com/catalyst-team/catalyst/pull/942))

### Changed

- Config API components preparation logic moved to ``utils.prepare_config_api_components`` ([#936](https://github.com/catalyst-team/catalyst/pull/936))

### Removed

-

### Fixed

- Logging double logging :) ([#936](https://github.com/catalyst-team/catalyst/pull/936))
- CMCCallback ([#941](https://github.com/catalyst-team/catalyst/pull/941))

## [20.09] - 2020-09-07

### Added

- `MovieLens dataset` loader ([#903](https://github.com/catalyst-team/catalyst/pull/903))
- `force` and `bert-level` keywords to `catalyst-data text2embedding` ([#917](https://github.com/catalyst-team/catalyst/pull/917))
- `OptunaCallback` to `catalyst.contrib` ([#915](https://github.com/catalyst-team/catalyst/pull/915))
- `DynamicQuantizationCallback` and `catalyst-dl quantize` script for fast quantization of your model ([#890](https://github.com/catalyst-team/catalyst/pull/915))
- Multi-scheduler support for multi-optimizer case ([#923](https://github.com/catalyst-team/catalyst/pull/923))
- Native mixed-precision training support ([#740](https://github.com/catalyst-team/catalyst/issues/740))
- `OptiomizerCallback` - flag `use_fast_zero_grad` for faster (and hacky) version of `optimizer.zero_grad()` ([#927](https://github.com/catalyst-team/catalyst/pull/927))
- `IOptiomizerCallback`, `ISchedulerCallback`, `ICheckpointCallback`, `ILoggerCallback` as core abstractions for Callbacks ([#933](https://github.com/catalyst-team/catalyst/pull/933))
- flag `USE_AMP` for PyTorch AMP usage ([#933](https://github.com/catalyst-team/catalyst/pull/933))

### Changed

- Pruning moved to `catalyst.dl` ([#933](https://github.com/catalyst-team/catalyst/pull/933))
- default `USE_APEX` changed to 0 ([#933](https://github.com/catalyst-team/catalyst/pull/933))

### Removed

-

### Fixed

- autoresume option for Config API ([#907](https://github.com/catalyst-team/catalyst/pull/907))
- a few issues with TF projector ([#917](https://github.com/catalyst-team/catalyst/pull/917))
- batch sampler speed issue ([#921](https://github.com/catalyst-team/catalyst/pull/921))
- add apex key-value optimizer support ([#924](https://github.com/catalyst-team/catalyst/pull/924))
- runtime warning for PyTorch 1.6 ([920](https://github.com/catalyst-team/catalyst/pull/920))
- Apex synbn usage ([920](https://github.com/catalyst-team/catalyst/pull/920))
- Catalyst dependency on system git ([922](https://github.com/catalyst-team/catalyst/pull/922))


## [20.08] - 2020-08-09

### Added
- `CMCScoreCallback` ([#880](https://github.com/catalyst-team/catalyst/pull/880))
- kornia augmentations `BatchTransformCallback` ([#862](https://github.com/catalyst-team/catalyst/issues/862))
- `average_precision` and `mean_average_precision` metrics ([#883](https://github.com/catalyst-team/catalyst/pull/883))
- `MultiLabelAccuracyCallback`, `AveragePrecisionCallback` and `MeanAveragePrecisionCallback` callbacks ([#883](https://github.com/catalyst-team/catalyst/pull/883))
- minimal examples for multiclass and multilabel classification ([#883](https://github.com/catalyst-team/catalyst/pull/883))
- experimental TPU support ([#893](https://github.com/catalyst-team/catalyst/pull/893))
- add `Imagenette`, `Imagewoof`, and `Imagewang` datasets ([#902](https://github.com/catalyst-team/catalyst/pull/902))
- `IMetricCallback`, `IBatchMetricCallback`, `ILoaderMetricCallback`, `BatchMetricCallback`, `LoaderMetricCallback` abstractions ([#897](https://github.com/catalyst-team/catalyst/pull/897))
- `HardClusterSampler` inbatch sampler ([#888](https://github.com/catalyst-team/catalyst/pull/888))

### Changed

- all registries merged to one `catalyst.registry` ([#883](https://github.com/catalyst-team/catalyst/pull/883))
- `mean_average_precision` logic merged with `average_precision` ([#897](https://github.com/catalyst-team/catalyst/pull/897))
- all imports moved to absolute ([#905](https://github.com/catalyst-team/catalyst/pull/905))
- `catalyst.contrib.data` merged to `catalyst.data` ([#905](https://github.com/catalyst-team/catalyst/pull/905))
- {breaking} Catalyst transform `ToTensor` was renamed to `ImageToTensor` ([#905](https://github.com/catalyst-team/catalyst/pull/905))
- `TracerCallback` moved to `catalyst.dl` ([#905](https://github.com/catalyst-team/catalyst/pull/905))
- `ControlFlowCallback`, `PeriodicLoaderCallback` moved to `catalyst.core` ([#905](https://github.com/catalyst-team/catalyst/pull/905))

### Removed

- `average_accuracy` and `mean_average_accuracy` metrics ([#883](https://github.com/catalyst-team/catalyst/pull/883))
- MultiMetricCallback abstraction ([#897](https://github.com/catalyst-team/catalyst/pull/897))

### Fixed

- `utils.tokenize_text` typo with punctuation ([#880](https://github.com/catalyst-team/catalyst/pull/880))
- `ControlFlowCallback` logic ([#892](https://github.com/catalyst-team/catalyst/pull/892))
- docs ([#897](https://github.com/catalyst-team/catalyst/pull/897))


## [20.07] - 2020-07-06

### Added

- `log` parameter to `WandbLogger` ([#836](https://github.com/catalyst-team/catalyst/pull/836))
- hparams experiment property ([#839](https://github.com/catalyst-team/catalyst/pull/839))
- add docs build on push to master branch ([#844](https://github.com/catalyst-team/catalyst/pull/844))
- `WrapperCallback` and `ControlFlowCallback` ([#842](https://github.com/catalyst-team/catalyst/pull/842))
- `BatchOverfitCallback` ([#869](https://github.com/catalyst-team/catalyst/pull/869))
- `overfit` flag for Config API ([#869](https://github.com/catalyst-team/catalyst/pull/869))
- `InBatchSamplers`: `AllTripletsSampler` and `HardTripletsSampler` ([#825](https://github.com/catalyst-team/catalyst/pull/825))

### Changed

- Renaming ([#837](https://github.com/catalyst-team/catalyst/pull/837))
    - `SqueezeAndExcitation` -> `cSE`
    - `ChannelSqueezeAndSpatialExcitation` -> `sSE`
    - `ConcurrentSpatialAndChannelSqueezeAndChannelExcitation` -> `scSE`
    - `_MetricCallback` -> `IMetricCallback`
    - `dl.Experiment.process_loaders` -> `dl.Experiment._get_loaders`
- `LRUpdater` become abstract class ([#837](https://github.com/catalyst-team/catalyst/pull/837))
- `calculate_confusion_matrix_from_arrays` changed params order ([#837](https://github.com/catalyst-team/catalyst/pull/837))
- `dl.Runner.predict_loader` uses `_prepare_inner_state` and cleans `experiment` ([#863](https://github.com/catalyst-team/catalyst/pull/863))
- `toml` to the dependencies ([#872](https://github.com/catalyst-team/catalyst/pull/872))

### Removed

- `crc32c` dependency ([#872](https://github.com/catalyst-team/catalyst/pull/872))

### Fixed

- `workflows/deploy_push.yml` failed to push some refs ([#864](https://github.com/catalyst-team/catalyst/pull/864))
- `.dependabot/config.yml` contained invalid details ([#781](https://github.com/catalyst-team/catalyst/issues/781))
- `LanguageModelingDataset` ([#841](https://github.com/catalyst-team/catalyst/pull/841))
- `global_*` counters in `Runner` ([#858](https://github.com/catalyst-team/catalyst/pull/858))
- EarlyStoppingCallback considers first epoch as bad ([#854](https://github.com/catalyst-team/catalyst/issues/854))
- annoying numpy warning ([#860](https://github.com/catalyst-team/catalyst/pull/860))
- `PeriodicLoaderCallback` overwrites best state ([#867](https://github.com/catalyst-team/catalyst/pull/867))
- `OneCycleLRWithWarmup` ([#851](https://github.com/catalyst-team/catalyst/issues/851))

## [20.06] - 2020-06-04

### Added

- `Mergify` ([#831](https://github.com/catalyst-team/catalyst/pull/831))
- `PerplexityMetricCallback` ([#819](https://github.com/catalyst-team/catalyst/pull/819))
- `PeriodicLoaderRunnerCallback` ([#818](https://github.com/catalyst-team/catalyst/pull/818))

### Changed

- docs structure were updated during ([#822](https://github.com/catalyst-team/catalyst/pull/822))
- `utils.process_components` moved from `utils.distributed` to `utils.components` ([#822](https://github.com/catalyst-team/catalyst/pull/822))
- `catalyst.core.state.State` merged to `catalyst.core.runner._Runner` ([#823](https://github.com/catalyst-team/catalyst/pull/823)) (backward compatibility included)
    - `catalyst.core.callback.Callback` now works directly with `catalyst.core.runner._Runner`
    - `state_kwargs` renamed to `stage_kwargs`

### Removed

-

### Fixed

- added missed dashes in docker perfixes ([#828](https://github.com/catalyst-team/catalyst/issues/828))
- handle empty loader in Runner ([#873](https://github.com/catalyst-team/catalyst/pull/873))


## [20.05.1] - 2020-05-23

### Added

- Circle loss implementation ([#802](https://github.com/catalyst-team/catalyst/pull/802))
- BatchBalanceSampler for metric learning and classification ([#806](https://github.com/catalyst-team/catalyst/pull/806))
- `CheckpointCallback`: new argument `load_on_stage_start` which accepts `str` and `Dict[str, str]` ([#797](https://github.com/catalyst-team/catalyst/pull/797))
- LanguageModelingDataset to catalyst\[nlp\] ([#808](https://github.com/catalyst-team/catalyst/pull/808))
- Extra counters for batches, loaders and epochs ([#809](https://github.com/catalyst-team/catalyst/pull/809))
- `TracerCallback` ([#789](https://github.com/catalyst-team/catalyst/pull/789))

### Changed

- `CheckpointCallback`: additional logic for argument `load_on_stage_end` - accepts `str` and `Dict[str, str]` ([#797](https://github.com/catalyst-team/catalyst/pull/797))
- counters names for batches, loaders and epochs ([#809](https://github.com/catalyst-team/catalyst/pull/809))
- `utils.trace_model`: changed logic - `runner` argument was changed to `predict_fn` ([#789](https://github.com/catalyst-team/catalyst/pull/789))
- redesigned `contrib.data` and `contrib.datasets` ([#820](https://github.com/catalyst-team/catalyst/pull/820))
- `catalyst.utils.meters` moved to `catalyst.tools` ([#820](https://github.com/catalyst-team/catalyst/pull/820))
- `catalyst.contrib.utils.tools.tensorboard` moved to `catalyst.contrib.tools` ([#820](https://github.com/catalyst-team/catalyst/pull/820))

### Removed

-

### Fixed

- device selection fix for [#798](https://github.com/catalyst-team/catalyst/issues/798) ([#815](https://github.com/catalyst-team/catalyst/pull/815))
- batch size counting fix for [#799](https://github.com/catalyst-team/catalyst/issues/799) and [#755](https://github.com/catalyst-team/catalyst/issues/755) issues ([#809](https://github.com/catalyst-team/catalyst/pull/809))


## [20.05] - 2020-05-07

### Added

- Added new docs and minimal examples ([#747](https://github.com/catalyst-team/catalyst/pull/747))
- Added experiment to registry ([#746](https://github.com/catalyst-team/catalyst/pull/746))
- Added examples with extra metrics ([#750](https://github.com/catalyst-team/catalyst/pull/750))
- Added VAE example ([#752](https://github.com/catalyst-team/catalyst/pull/752))
- Added gradient tracking ([#679](https://github.com/catalyst-team/catalyst/pull/679)
- Added dependabot ([#771](https://github.com/catalyst-team/catalyst/pull/771))
- Added new test for Config API ([#768](https://github.com/catalyst-team/catalyst/pull/768))
- Added Visdom logger ([#769](https://github.com/catalyst-team/catalyst/pull/769))
- Added new github actions and templates ([#777](https://github.com/catalyst-team/catalyst/pull/777))
- Added `save_n_best=0` support for CheckpointCallback ([#784](https://github.com/catalyst-team/catalyst/pull/784))
- Added new contrib modules for CV ([#793](https://github.com/catalyst-team/catalyst/pull/793))
- Added new github actions CI ([#791](https://github.com/catalyst-team/catalyst/pull/791))

### Changed

- Changed `Alchemy` dependency (from `alchemy-catalyst` to `alchemy`) ([#748](https://github.com/catalyst-team/catalyst/pull/748))
- Changed warnings logic ([#719](https://github.com/catalyst-team/catalyst/pull/719))
- Github actions CI was updated ([#754](https://github.com/catalyst-team/catalyst/pull/754))
- Changed default `num_epochs` to 1 for `State` ([#756](https://github.com/catalyst-team/catalyst/pull/756))
- Changed `state.batch_in`/`state.batch_out` to `state.input`/`state.output` ([#763](https://github.com/catalyst-team/catalyst/pull/763))
- Moved `torchvision` dependency from `catalyst` to `catalyst[cv]` ([#738](https://github.com/catalyst-team/catalyst/pull/738)))

### Removed

- GanRunner removed to Catalyst.GAN ([#760](https://github.com/catalyst-team/catalyst/pull/760))
- `monitoring_params` were removed ([#760](https://github.com/catalyst-team/catalyst/pull/760))

### Fixed

- Fixed docker dependencies ([$753](https://github.com/catalyst-team/catalyst/pull/753))
- Fixed `text2embeddding` script ([#722](https://github.com/catalyst-team/catalyst/pull/722))
- Fixed `utils/sys` exception ([#762](https://github.com/catalyst-team/catalyst/pull/762))
- Returned `detach` method ([#766](https://github.com/catalyst-team/catalyst/pull/766))
- Fixed timer division by zero ([#749](https://github.com/catalyst-team/catalyst/pull/749))
- Fixed minimal torch version ([#775](https://github.com/catalyst-team/catalyst/pull/775))
- Fixed segmentation tutorial ([#778](https://github.com/catalyst-team/catalyst/pull/778))
- Fixed Dockerfile dependency ([#780](https://github.com/catalyst-team/catalyst/pull/780))


## [20.04] - 2020-04-06

### Added


### Changed

-

### Removed

-

### Fixed

-


## [YY.MM.R] - YYYY-MM-DD

### Added

-

### Changed

-

### Removed

-

### Fixed

-
