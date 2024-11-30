## 📅 Date
**30 November 2024**


## 📰 Resource
[Communication-Efficient Learning of Deep Networks from Decentralized Data](https://arxiv.org/pdf/1602.05629)


## 🔖 My Learning
As I wanted to get hands-on with the `FedAvg` algorithm, the workhorse of FL methods, this morning I started building a simple repository to replicate an experiment detailed in the article: [Communication-Efficient Learning of Deep Networks from Decentralized Data](https://arxiv.org/pdf/1602.05629).

I aim to replicate the following experiment:

Material            |  Description
:-------------------------:|:-------------------------:
**Dataset** | MNIST digit recognition task. With two ways of partitioning the MNIST data over clients: **IID**, where the data is shuffled, and then partitioned into 100 clients each receiving 600 examples, and **Non-IID**, where we first sort the data by digit label, divide it into 200 shards of size 300, and assign each of 100 clients 2 shards.
**Models** | Two models: 1) A simple multilayer-perceptron (**MLP**) with 2-hidden layers with 200 units each using ReLu activations, which we refer to as the MNIST 2NN. 2) A **CNN** with two 5x5 convolution layers (the first with 32 channels, the second with 64, each followed with 2x2 max pooling), a fully connected layer with 512 units and ReLu activation, and a final softmax output layer. 

All this details are better described in the paper. I just wanted to give you a quick overview of the experiment I'm replicating.

So for today I implemented the `data` module where I created:

- the `FederatedSampler` a custom sampler class from `torch.utils.data` for designed to handle both IID (Independent and Identically Distributed) and non-IID data distributions

- the `MNISTDataset` class which is a subclass of `datasets.MNIST` from PyTorch, which I use to handle the MNIST dataset with some customizations.

and the `model` module, which contains the two models:

- Multi-Layer Perceptron (MLP)
- Convolutional Neural Network (CNN)

Still a lot to do, but I am happy with the progress I made today.
Open TODOs:
- Implement the main `FedAvg` class.
- Implement the `logger` module (wandb is the one suggested on github for thi type of topic).
- Test and train a model on the MNIST dataset in a Federated Learning setting.

All the code will be available [here](./FedAvg).

## 📮 Post 

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is **Multi-Layer Perceptron**.
> [!NOTE]
> multilayer perceptron (MLP) represents a neural network consisting of fully connected neurons with nonlinear activation functions, organized in layers, notable for being able to distinguish data that is not linearly separable.
