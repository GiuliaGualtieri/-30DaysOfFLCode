## 📅 Date
**6 December 2024**

## 📰 Resource
[FEDERATED OPTIMIZATION IN HETEROGENEOUS NETWORKS](https://arxiv.org/pdf/1812.06127)

## 🔖 My Learning

Today I started reading the article titled [FEDERATED OPTIMIZATION IN HETEROGENEOUS NETWORKS](https://arxiv.org/pdf/1812.06127) where they introduce the `FedProx`, a generalization and re-parametrization of the `FedAvg` algorithm, the current state-of-the-art method for federated learning. 

Federated Learning is a distributed learning with diverse challenges (read my blog [Day 1️⃣ ](../day1/day1.md)). The most investigated ones are: [systems heterogeneity](../day2/day2.md), and [statistical heterogeneity](../day3/day3.md).

To handle heterogeneity and tackle high communication costs, optimization methods, like `FedAvg` algorithm where local updating and a small fraction of participating clients, have been researched. In particular the `FedAvg` algorithm by [McMahan et al. in 2017](https://arxiv.org/pdf/1602.05629) represents the de facto optimization method in the federated setting.

Drawbacks of `FedAvg`:
* `FedAvg` has demonstrated empirical success in heterogeneous settings, but it does not fully address the underlying challenges associated with heterogeneity. In the context of **systems heterogeneity**, `FedAvg` does not allow participating devices to perform variable amounts of local work based on their underlying systems constraints; instead it is common to simply drop devices that fail to compute `E` epochs within a specified time window. 
* `FedAvg` has been shown to **diverge empirically** in settings where the data is **non-identically distributed across devices**.
* `FedAvg` is difficult to analyze theoretically in such realistic scenarios and thus **lacks convergence guarantees** to characterize its behavior.

> [!IMPORTANT]
> **`FedProx`**, a federated optimization algorithm that addresses the challenges of heterogeneity both theoretically and empirically.

Idea behind `FedProx`: naively incorporating partial information from stragglers. A proximal term to the objective that helps to improve the stability of the method. This term provides a principled way for the server to account for heterogeneity associated with partial information. 
- *Theoretically*: these modifications provide convergence guarantees and to analyze the effect of heterogeneity. 
- *Empirically*: the modifications improve the stability and overall accuracy of federated learning in heterogeneous networks—improving the absolute testing accuracy by 22% on average in highly heterogeneous settings.

> [!IMPORTANT]
> **KEY INSIGHT**: In `FedProx`: an interplay exists between systems and statistical heterogeneity in federated learning.

### Overview of Status Quo

### Task
**Topic**: it is increasingly attractive to learn statistical models locally in networks of distributed devices, in contrast to moving the data to the data center.

### Current Situation
**Convex Setting**: [Federated Averaging (`FedAvg`)](https://arxiv.org/pdf/1602.05629), a heuristic method based on averaging local Stochastic Gradient Descent (SGD) updates in the primal, has instead been shown to work well empirically.

Beyond statistical heterogeneity, systems heterogeneity is also a critical concern in federated networks. The storage, computational, and communication capabilities of each device in federated networks may differ due to variability in hardware (CPU, memory), network connectivity (3G, 4G, 5G, wifi), and power (battery level). 

### Solution
`FedProx`, that is capable of:
- **handling heterogeneous federated settings** while maintaining similar privacy and computational benefits;
- ensure **convergence behavior** through a statistical heterogeneity between local data, while also taking into account practical systems constraints.

*How?*
- the **proximal term** in `FedProx`,
- the **bounded dissimilarity** assumption used in our analysis.

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7270848801735671808-L-h_?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Theoretical Convergence**.
> [!NOTE]
> **Theoretical Convergence** is a property of an optimization algorithm to mathematically guarantee that the global model in federated learning approaches an optimal solution (or a stationary point) over time.
