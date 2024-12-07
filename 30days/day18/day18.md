## 📅 Date
**7 December 2024**

## 📰 Resource
[FEDERATED OPTIMIZATION IN HETEROGENEOUS NETWORKS](https://arxiv.org/pdf/1812.06127)

## 🔖 My Learning

Today let's dive into the algorithmic POV of the development of the optimization method, introduced [yesterday](../day17/day17.md), `FedProx`.

### Federated Optimization Methods

[Federated learning methods](https://arxiv.org/pdf/1602.05629) are designed to handle multiple devices collecting data and a central server coordinating the global learning objective across the network. 
In particular, the aim is to minimize the weighted sum of local objective functions `Fk(·)`.

#### State Of Art: Federated Averaging (`FedAvg`)
To reduce communication, a common technique in federated optimization is that on each device, a local objective based on the device’s data is used as a surrogate for the global objective function at each outer iteration, a subset of the devices are selected and local solvers are
used to optimize the local objective functions on each of the selected devices. The devices then communicate their local model updates to the central server, which aggregates them and updates the global model accordingly. The key to allowing flexible performance in this scenario is that each of the local objectives can be solved inexactly. This allows the amount of local computation vs. communication to be tuned based on the number of local iterations that are performed (with additional local iterations corresponding to more exact local solutions).  

`FedAvg` on each local device:
- same learning rate
- same number of local epochs
- local solver : SGD
- local function: surrogate of global function 

➡️ **Key hyperparamater** is **the number of local epochs** `E`, which plays an important role in convergence.
- high number of local epochs: less number of communication rounds, but low convergence to the global objective, so risk of divergence.
- low number of local epochs: more communication rounds, but robust convergence.

#### Proposed Framework: `FedProx`
Idea behind `FedProx` : instead of a fixed number of local epochs, allowing the epochs to vary according to the characteristics of the network, and to carefully merge solutions by accounting for this heterogeneity.

Same Characteristics as FedAvg:
- a subset of devices are selected at each round, 
- local updates are performed,
- local updates are then averaged to form a global update.

Modifications:

![FedProx](../images/FedProx.png)

1️⃣ **Tolerating partial work**
As previously discussed, different devices in federated networks often have different resource constraints in terms of the computing hardware, network connections, and battery levels. Therefore, it is unrealistic to force each device to perform a uniform and fixed amount of work (i.e., running the same number of local epochs, `E`), as in `FedAvg`.
In FedProx, we generalize FedAvg by allowing for variable amounts of work to be performed locally across devices based on their available systems resources, and then aggregate the partial solutions sent from the stragglers (as compared to dropping these devices). In other words, instead of assuming a uniform number of local epochs for all devices throughout the training process, `FedProx` implicitly allows a variable number  of `E` for different devices and at different iterations. See Figure above!.

2️⃣ **Proximal term**. While tolerating nonuniform amounts of work to be performed across devices can help alleviate negative impacts of systems heterogeneity, too many local updates may still (potentially) cause the methods to diverge due to the underlying heterogeneous data.  
The `FedProx` algorithm proposes a proximal term to the local subproblem to effectively limit the impact of variable local updates. In particular, instead of just minimizing the local function `Fk(·)`, device k uses its local solver of choice to approximately minimize the local function  `Fk(·)` plus a proximal term, the l2-norm of the difference between the current local parameters and the parameters of the global model. This proximal term is beneficial in two aspects:
🔸 It addresses the issue of statistical heterogeneity by restricting the local updates to be closer to the initial (global) model without any need to manually set the number of local epochs.
🔸 It allows for safely incorporating variable amounts of local work resulting from systems heterogeneity. 


## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7271072020069527553-clb2?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Proximal Term**.
> [!NOTE]
> **Proximal Term** is key component introduced in the `FedProx` algorithm to stabilize training in federated learning by explicitly controlling the divergence between local updates and the global model. This term penalizes local model updates that deviate significantly from the global model, addressing both statistical heterogeneity and systems heterogeneity.
