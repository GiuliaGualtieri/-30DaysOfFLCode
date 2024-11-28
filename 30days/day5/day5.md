## 📅 Date
**23 November 2024**

## 📰 Resource
[Federated Learning: Challenges, Methods, and Future Directions: 2.4 Privacy](https://arxiv.org/pdf/1908.07873)

## 🔖 My Learning
In today early morning, I read about the last, but not least, challenge that federated networks must address: **Privacy**.  

Even if Federated learning makes a step towards protecting data generated on each device train a machine learning model without sharing their local data, by sharing model
updates and communicating them through the training process can reveal sensitive information, either to a third-party, or to the central server.

> [!IMPORTANT]
> In privacy concerns analysis, must always consider third-party or central server as malicius!

Enhancing privacy in the federated networks is not straightforward. This is why I love working in this fascinating corner where Machine Learning meets Privacy.

Privacy definitions in federated learning can be classified into two categories: **global privacy** and **local privacy**.  

**Global privacy** requires that the global model updates generated at each round are private to all (both data owners and untrusted third parties, other than the central server), 
while **local privacy** further requires that the local updates are also private to the central server.

The three main strategies that the article cites as a enhancement for federated learning to deal with the privacy concerns, are:
1. **differential privacy** to communicate noisy data sketches,
2. **homomorphic encryption** to operate on encrypted data,
3. **secure function evaluation or multiparty computation.**

Among these various privacy approaches, **differential privacy (DP)** is most widely used due to its strong information theoretic guarantees and algorithmic simplicity. And concerning it, I suggest to read about the articles I published with my current company on LinkedIn: [📰 first one](https://www.linkedin.com/posts/giuliagualtieri_ai-innovation-dataprivacy-activity-7174346563937288192-RCf6?utm_source=share&utm_medium=member_desktop) , 
and [📰 second one](https://www.linkedin.com/posts/giuliagualtieri_dataprotection-ai-privacy-activity-7252259201274535936-TMqi?utm_source=share&utm_medium=member_desktop). Check it out and let me know!

The idea behind DP is to randomly perturbing the intermediate updates in each communication rounds or even more, in each local update iteration, such that one cannot draw any conclusions about
whether or not a specific sample is used in the learning process. The hard part in this methodology is finding the right trade-off between differential privacy and model accuracy, as adding more noise
results in greater privacy, but may compromise accuracy significantly.

Beyond differential privacy, **homomorphic encryption (HE)** can be used to secure the learning process by computing on encrypted data. 
Although it has currently been applied in limited settings, for example training linear models or involving only a few entities and values are strictly integers.

When the sensitive datasets are distributed across different data owners, another natural option is to perform privacy-preserving learning via **secure function evaluation (SFE)** 
or **secure multiparty computation (SMC)**. The resulting protocols can enable multiple parties to collaboratively compute an aggregated function without leaking input information
from any party.

SMC is a lossless method, and can retain the original accuracy with a very high privacy guarantee. 
However, the resulting method incurs significant extra communication cost. SMC protocols need to be carefully designed and implemented for each operation in the targeted learning algorithm. 
Then, approaches along these lines may not be applicable to large-scale machine learning scenarios as they incur substantial additional communication and computation costs.
The federated setting poses novel challenges to existing privacy-preserving algorithms. 

Beyond providing rigorous privacy guarantees, it is necessary to develop methods that are computationally cheap, communication-efficient, and tolerant to dropped devices, 
all without overly compromising accuracy.


## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_ai-innovation-dataprivacy-activity-7266372881545129984-DDh9?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is (of course) **Differential Privacy**.
> [!NOTE]
> A randomized mechanism is differentially private if the change of one input element will not result in too much difference in the output distribution;.
