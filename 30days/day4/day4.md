## 📅 Date
**23 November 2024**

## 📰 Resource
[Federated Learning: Challenges, Methods, and Future Directions: 2.3 Statistical Heterogeneity](https://arxiv.org/pdf/1908.07873)


## 🔖 My Learning

In today early morning, I studied another challenge that federated networks must address: **Statistical Heterogeneity**.  

Devices in federated networks collect and generate data in different ways, but mostly data varies a lot between devices. Here is where the challenges of training federated models from data, that are not identically distributed across devices, arises.

To overcome this issue federated networks are investigating various **model learning strategies**. Instead of creating a single global model, alternatives like **multi-task learning**, which develops separate models for each device, or **meta-learning**, which aims to personalize models for individual devices, are being considered as promising solutions.

Here's the notes I made along with a reference to a book from the article I read:

[📘 **Multi-task learning** ](https://link.springer.com/article/10.1023/A:1007379606734) (MTL) is a method where a model is trained to solve multiple tasks simultaneously, sharing common knowledge across tasks. Instead of learning each task independently, the model learns from multiple related tasks at the same time, which **can help improve the performance on each individual task due to shared information**. 

[📗 **Meta-learning** ](https://link.springer.com/book/10.1007/978-1-4615-5529-2) is a method where the model learns how to learn from different tasks. Instead of training a model for a single task, meta-learning tries to learn a model that can **quickly adapt to new, similar tasks with minimal data**. 

Another important aspect I noted is not to overlook issues like **fairness, accountability** and **interpretability.**

In particular, naively solving an aggregated loss function may implicitly advantage or disadvantage some of the devices, as the learned model may become biased towards devices with larger amounts of data, or (if weighting devices equally), to commonly occurring groups of devices.

Recent works have proposed modified modeling approaches that aim to reduce the variance of the model performance across devices. Some heuristics simply perform a varied number of local updates based on local loss. Other more principled approaches include Agnostic Federated Learning, which optimizes the centralized model for any target distribution formed by a mixture of the client distributions via a minimax optimization scheme. 
Another more general approach is an objective called q-FFL in which devices with higher loss are given higher relative weight to encourage less variance in the final accuracy distribution. Beyond issues of fairness, I noted that aspects such as accountability and interpretability in federated learning are additionally worth exploring, but may be challenging due to the scale and heterogeneity of the network.

Finaly, statistical heterogeneity also presents novel challenges in terms of analyzing the **convergence behavior** in federated setting. Methods like parallel SGD and related variants, which make local updates have shown to diverge in practice under the I.I.D. settings. ***FedProx*** has recently been proposed and it comes as a solution.

> [!TIP]
> [📃 **FedProx** ](https://arxiv.org/abs/1812.06127) can be an interesting reading, after the article of [📃 **FedAvg** ](https://arxiv.org/pdf/1602.05629)).

**FedProx** can be viewed as a generalization and re-parametrization of **FedAvg**, the current state-of-the-art method for federated learning.

Several other works have also explored convergence guarantees in the presence of heterogeneous data with different assumptions, e.g., convexity or uniformly bounded gradients.

## 📮 Post 

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is **Meta-learning**
> [!NOTE]
> **Meta-learning** is a subfield of machine learning where automatic learning algorithms are applied to metadata about machine learning experiments. 
