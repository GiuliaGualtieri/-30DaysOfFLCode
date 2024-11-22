## 📅 Date
**21.11.24**

## 📰 Resource
[Federated Learning: Challenges, Methods, and Future Directions: 2.1 Communication Efficiency](https://arxiv.org/pdf/1908.07873)

## 🔖 My Learn
As understood in [yesterday learning](../day1/day1.md), communication is a key bottleneck to consider when developing methods for federated networks.
Therefore the first challenge for FL is **communication efficiency.**

Several distributed learning methods hve been studied to make communication efficient and they can be grouped into
**1) local updating methods** <br>
In **Local updating schemes**, each device immediately applies local updates, e.g., 
gradients, after they are computed and a server performs a global aggregation after a variable number of local updates. 
The most commonly used optimization methods that allow for flexible local updating and low client participation for federated learning is [**Federated Averaging (FedAvg)**](https://arxiv.org/pdf/1602.05629)
several recent methods have been proposed to improve communication-efficiency
in distributed settings by allowing for a variable number of local updates to be applied on each machine in parallel at each communication round, making the amount of computation versus communication substantially more flexible.

**2) compression schemes** <br>

While local updating methods can reduce the total number of communication rounds, model compression schemes such as **sparsification**, **subsampling**, and **quantization** can significantly reduce the size of messages communicated at each round.
> [!TIP]
> Matter of investigation and study: **sparsification**, **subsampling**, and **quantization**.

**3) decentralized training** <br>

In federated learning, a star network (where a central server is connected to a network of devices, Figure below left) is the predominant communication topology. 
![immagine](https://github.com/user-attachments/assets/ad5fded4-2845-4929-85f4-b79eb16a1811)
However, **decentralized topologies** (where devices only communicate with their neighbors, Figure above right) is a potential alternative for efficient communication when communication to the server becomes a bottleneck. 

In data center environments, decentralized training has been demonstrated to be faster than centralized training when operating on networks with low bandwidth or high latency. Similarly, in federated learning, decentralized algorithms can reduce the high communication cost on the central server. Also, hierarchical communication patterns have also been proposed to further ease the burden on the central server, by first leveraging edge servers to aggregate the updates from edge devices and then relying on a cloud server to aggregate updates from edge servers. While this is a promising approach to reduce communication, it is not applicable to all networks,
as this type of physical hierarchy may not exist or be known a priori.

## 📮 Post
https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7265261806686720004-JCRV?utm_source=share&utm_medium=member_desktop
------
The _**Federated Learning Term of the Day**_ is **Federated Networks**.
> [!NOTE]
> **Federated Networks** refers to a collection of distributed devices (like smartphones, IoT devices, or local servers) that collaboratively train a machine learning model without sharing their local data.
