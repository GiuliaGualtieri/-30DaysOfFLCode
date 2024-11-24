## 📅 Date
**25 November 2024**

## 📰 Resource
[Communication-Efficient Learning of Deep Networks from Decentralized Data: Abstract, Introduction, FederatedAveraging algorithm](https://arxiv.org/pdf/1602.05629)

## 🔖 My Learning
Early this morning, I started reading an article about the **Federated Averaging algorithm**, one of the workhorses of Federated Learning methods.

The algorithm combines local stochastic gradient descent (SGD) on each client with a server that performs model averaging, which is why 'average' is in the name. 
It has been developed as a practical method for federated learning of deep networks based on iterative model averaging.

Here you can find my notes and my drawings of the algorithm, which highlight the major parametric characteristics of 
`FedAvg` compared to a general standard federated learning algorithm using stochastic gradient descent (SGD), referred as `FedSGD`, for parameter updates.

Federated Network| 
:-------------------------:|
![Figure 1: Federated Networks](30days/images/FederatedNetworks.jpeg)

**Setting**: 
- The learning task is solved by a federation of participating _local devices_ (called also clients) which are coordinated by a _central server_ (see [Figure 1: Federated Networks](https://github.com/GiuliaGualtieri/30DaysOfFLCode/raw/main/30days/images/FederatedNetworks.jpeg)).
- We assume a synchronous update scheme that proceeds in rounds of communication, `t` = round in figures below.
- There is a fixed set of `K` clients, each with a fixed local dataset. 
- At the end of each round we only select a fraction of clients thet effectively ended local updates computation. (see [Figure 2: `Federated SGD algorithm`](https://github.com/GiuliaGualtieri/30DaysOfFLCode/raw/main/30days/images/FedSGD.jpeg), row 5, [Figure 3: `Federated Averaging algorithm`](https://github.com/GiuliaGualtieri/30DaysOfFLCode/raw/main/30days/images/FedAVG.jpeg), row 7)
- Fixed learning rate `η`.
> [!NOTE]
> - `C`, the fraction of clients that perform computation on each round. At the beginning of each round, a random fraction `C` of clients is selected, and the server sends the current global algorithm state to each of these clients (e.g., the current model parameters).
> - `E`, then number of training passes each client makes over its local dataset on each round
> - `B`, the local minibatch size used for the client updates


FedSGD algorithm             |  FedAvg algorithm
:-------------------------:|:-------------------------:
![Figure 2: `Federated SGD algorithm`](30days/images/FedSGD.jpeg)  |  ![Figure 3: `Federated Averaging algorithm`](30days/images/FedAVG.jpeg)
 

If:
- `C = 1` corresponding to full-batch (non-stochastic) gradient descent
- `B = inf`
- `E = 1`
then `FedAVG` --> `FedSGD`.


## 📮 Post 

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is **FederatedSGD**.
> [!NOTE]
> Each selected client performs local computation based on the global state and its local dataset, and sends an update to the server. The server then applies these updates to its global state, and the process repeats until convergence is reached.
