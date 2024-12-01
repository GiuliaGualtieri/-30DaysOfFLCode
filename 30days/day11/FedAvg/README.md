## Overview

Implementation of [FedAvg](http://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf) in Pytorch, supporting [WandB](https://wandb.ai) logging.

## Installation

### Dependencies

Requires **Python 3.6+**. Suggested **3.12**.

- numpy>=1.22.4
- pytorch>=1.12.0
- torchvision>=0.13.0
- wandb>=0.12.19

### Conda Installation

```
conda create -n fedavg python=3.12
pip install -r requirements.txt
```

## How To Use

### Major Arguments

| Flag            | Options     | Default |Info        |
| --------------- | ----------- | :-------: |----------|
| `--data_root` | String     | "../datasets/" | path to data directory |
| `--model_name`   | String | "cnn"       | name of the model (cnn, mlp)             |
|`--non_iid` | Int (0 or 1) | 1 | 0: IID, 1: Non-IID |
| `--n_clients` | Int     | 100 | number of the clients |
| `--frac` | Float     | 0.1 | fraction of clients in each round |
| `--n_rounds` | Int     | 1000 | total number of rounds |
| `--n_client_epochs` | Int     | 5 | number of local training epochs |
| `--batch_size` | Int     | 10 | batch size |
| `--lr` | Float     | 0.01 | leanring-rate |
| `--wandb` | Bool     | False | log the results to WandB |
| --early_stopping | Bool | True | stop training when the validation accuracy reach the target one |


### Training Example

```
python fed_avg.py  --non_iid=1 --n_clients=100 --frac=0.1 --n_rounds=1000 --n_client_epochs=20 --batch_size=10 --lr=0.01 
```

To perform a sweep over hyperparameters using WandB:

```
wandb sweep sweep.yaml
wandb agent <sweep_id>
```
