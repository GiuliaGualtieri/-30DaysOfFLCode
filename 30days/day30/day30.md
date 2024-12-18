## 📅 Date
**19 December 2024**


## 📰 Resource
[Federated Learning in Practice: Reflections and Projections](https://arxiv.org/pdf/2410.08892)


## 🔖 My Learning
As last day of the challenge I started reading the paper Federated Learning in Practice: Reflections and Projections. Nothing better that leave the challenge with a paper that reflects the current state of the art of Federated Learning. The paper is a reflection on the current state of Federated Learning (FL) and its future directions. The authors propose a redefined FL framework that prioritizes privacy principles over rigid definitions and suggest leveraging trusted execution environments and open-source ecosystems to address these challenges and facilitate future advancements in FL. The paper is a great summary of the current challenges and future directions of Federated Learning.

## Abstract

Federated Learning (FL) enables multiple entities to collaboratively train a shared machine learning model without exchanging their local data. Over the past decade, FL systems have scaled to millions of devices across various domains, offering meaningful differential privacy (DP) guarantees. Production systems from organizations like Google, Apple, and Meta demonstrate FL's real-world applicability. However, challenges such as verifying server-side DP guarantees and coordinating training across heterogeneous devices limit broader adoption. Emerging trends, including large multi-modal models and the convergence of training, inference, and personalization, challenge traditional FL frameworks. In response, the authors propose a redefined FL framework that prioritizes privacy principles over rigid definitions and suggest leveraging trusted execution environments and open-source ecosystems to address these challenges and facilitate future advancements in FL. 

## Introduction

Introduced around 2016, Federated Learning (FL) is a privacy-enhancing technique that applies data minimization principles by enabling mobile phones to collaboratively learn a shared prediction model while keeping all training data on-device. This decouples the ability to perform machine learning from the need to store data in the cloud. FL has evolved into a widely acknowledged paradigm of distributed learning from decentralized data, extending beyond on-device training to applications such as collaborative learning across multiple institutions (silos) with substantial computational resources and learning over Internet-of-Things devices with limited resources.

## Evolution of Federated Learning

In 2019, discussions at the Workshop on Federated Learning and Analytics at Google led to a broader definition of FL:

> [!NOTE]
> Federated learning is a machine learning setting where multiple entities (clients) collaborate in solving a machine learning problem under the coordination of a central server or service provider. Each client’s raw data is stored locally and not exchanged or transferred; instead, focused updates intended for immediate aggregation are used to achieve the learning objective.

Federated Analytics (FA) was later introduced as the practice of applying data science methods to analyze raw data stored locally on users’ devices. Like FL, it operates by running local computations over each device’s data, with only aggregated results—never any data from a particular device—made available to product engineers. While this manuscript primarily focuses on FL, the discussions are also applicable to FA, as both paradigms are closely related and share similar privacy principles. :contentReference

## Challenges in Federated Learning

Despite significant progress in theory and practice, production FL systems face several challenges:

1. **Scalability to Large Models**: Very large and often multi-modal models achieve unprecedented performance for various tasks but are typically orders of magnitude beyond what has been considered in classical cross-device FL applications.

2. **Verifiability of Computations**: Current FL systems provide limited verifiability of server-side computations, and verifying client-side work can be challenging. This limitation hinders users or external auditors from confirming the system's privacy properties, affecting trust in the service provider.

3. **Operational Challenges**: Coordinating training across loosely synchronized and heterogeneous devices—differing in compute capabilities, bandwidth, availability for training, data, and software versions—presents numerous operational challenges that impede the broader adoption of FL.


## Redefining Federated Learning

To address these challenges and leverage emerging opportunities, the authors propose a new definition of FL that emphasizes privacy principles over rigid definitions. This redefinition aims to:

- **Enhance Privacy Guarantees**: By focusing on core privacy principles, the redefined FL framework seeks to provide stronger and more verifiable privacy guarantees to users.

- **Improve Scalability**: Adapting the FL framework to accommodate large and complex models will enable the system to scale effectively across diverse applications.

- **Facilitate Operational Efficiency**: Addressing the operational challenges associated with heterogeneous device coordination will streamline FL processes, promoting broader adoption.

## Future Directions

The authors suggest several pathways to advance FL:

- **Trusted Execution Environments (TEEs)**: Leveraging TEEs can enhance the security and verifiability of computations within FL systems, building greater trust among users and auditors.

- **Open-Source Ecosystems**: Developing and participating in open-source ecosystems can foster collaboration, innovation, and transparency in FL research and implementation.

- **Integration of Large Models**: Adapting FL frameworks to effectively handle large, multi-modal models will expand the applicability of FL to more complex and diverse tasks.

- **Enhanced Coordination Mechanisms**: Improving methods for coordinating training across heterogeneous devices will address operational challenges, facilitating smoother and more efficient FL processes.

## Conclusion

Federated Learning has made significant strides in enabling privacy-preserving collaborative machine learning. However, challenges related to scalability, verifiability, and operational efficiency remain. By redefining FL to prioritize privacy principles and leveraging technologies like trusted execution environments and open-source ecosystems, the field can address these challenges and continue to advance, broadening the adoption and impact of FL across various domains.


## 📮 Post 

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is **Trusted Execution Environments**.
> [!NOTE]
> Trusted Execution Environments, aka TEEs, can enhance the security and verifiability of computations within FL systems, building greater trust among users and auditors.
