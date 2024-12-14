## 📅 Date
**14 December 2024**

## 📰 Resource
[Understanding the Types of Federated Learning](https://blog.openmined.org/federated-learning-types/) 

## 🔖 My Learning
Today I read this post about *Understanding the Types of Federated Learning* , posted by OpenMined on September 21st, 2020.

Main Question is **How many different Federated Learning scenarios and implementations are there ❓**

In the past days I read terms like: **Model-Centric Federated Learning**, **Data-Centric Federated Learning**, and even terms like **Cross-Silo Federated Learning**, **Cross-Device Federated Learning**, **Horizontal Federated Learning**, **Vertical Federated Learning**,** Federated Transfer Learning**.
But beware — those building the software that will deliver the benefits of this technology are not limited by, or overly influenced by these terms. To quote OpenMined’s Patrick Cason, such terms "matter very little in the art of engineering solutions".
However, understanding these federating learning terms may help us orientate and navigate the strange world of Federated Learning, where we can build machine learning models using data we don’t own and can’t see.

### Federated Learning
In the corresponding [2016 paper](https://ar5iv.labs.arxiv.org/html/1602.05629), the Google team describe: a specific topology — a central server, with a federation of participating end user devices with local training sets.

### Model-Centric Federated Learning
Federated Machine Learning can be categorised in to two base types, **Model-Centric** & **Data-Centric**. Model-Centric is currently more common.
for any Federated Learning solution that has a goal of delivering better centrally administered models, they can be considered **Model-Centric**.
> “Data is generated locally and remains de-centralised. Each client stores its own data and cannot read the data of other clients. Data is not independently or identically distributed.”
 
It turns out that we can further qualify Model-Centric with the terms Cross-Device or Cross-Silo. There’s some alignment here also with the terms Horizontal and Vertical.

### Cross-Device Federated Learning
Learning takes place remotely: each device computes the updating step on their local data for the global mode. Updating the central model is made by a suitable federation technique, such as averaging the model updates from each device. I suggest you to read [Day 14](../day14/day14.md) of my learning path to learn more! ;) Cross-devices is tipycal when the clients are a large numbers, for example mobile or IoT devices, while cross-silo is when the clients are a typically smaller number of organizations, institutions, or other data silos.

Typically, the data in this scenario of model-centric and cross-device is partitioned Horizontally.

### Horizontal Federated Learning
How you data is split matters in terms of how Federated Learning is implemented and the practical and technical challenges.
> “Horizontal federated learning, or sample-based federated learning, is introduced in the scenarios that data sets share the same feature space but different in sample.”

Example: *Google GBoard* as utilising **Model-Centric**, **Cross-Device**, **Horizontal Federated Learning**.

### Cross-Silo Federated Learning
It represents the value of data that is more widely distributed, for example between hospitals, banks, perhaps distributed aggregate data from consumer wearables in different fitness app businesses.

Whilst the goal is typically stated as the same for **Cross-Silo**, to update and improve a central, and in this case shared, model, there are arguably greater challenges on the security side.

Its typical scenario is is represented by **Multiple Organisations**, **Model Centric** & **Cross-Silo Federated Learning**, and in some cases the data being partitioned Vertically.

### Vertical Federated Learning
> “Vertical federated learning or feature-based federated learning … is applicable to the cases that two data sets share the same sample ID space but differ in feature space.” 

Cross-silo FL with data partitioned by features, employs a very different training architecture compared to the setting with data partitioned by example. It may or may not involve a central server as a neutral party, and based on specifics of the training algorithm, clients exchange specific intermediate results rather than model parameters, to assist other parties’ gradient calculations.

Example: **Multiple Organisations** having same patients but collecting different features, so **Vertical Data** (Data Split by Features).

### Example
The **FedAI Technology Enabler (FATE)** platform has case studies associated with examples of both [Horizontal](https://www.fedai.org/cases/utilization-of-fate-in-anti-money-laundering-through-multiple-banks/) and [Vertical](https://www.fedai.org/cases/utilization-of-fate-in-risk-management-of-credit-in-small-and-micro-enterprises/) implementations. A neutral 3rd party is utilised (‘a collaborator’) to orchestrate federation.

### Federated Transfer Learning
Unlike the Convolutional Neural Network transfer techniques that I have to be honest, I’m not familiar with, but I quickly read they essentially drop the last few layers from a network trained on big data, then re-tune the model to recognise your labels on a small data set, the descriptions given for Federated Transfer Learning are more involved, comprising intermediate learning to map to a common feature subspace. So it's not straightforward neither to understand neither to explain.

Example: [**FedHealth**](https://jd92.wang/assets/files/a15_ijcai19.pdf) which seems to use Federated Transfer Learning, and although at first glance looks to be Model-Centric, Vertical, Cross-Device, data is aggregated at each wearable service provider making it Model-Centric, Vertical, Cross-Silo.

### Data-Centric Federated Learning
This is an emerging type of Federated Learning, and in some ways may be outgrowing the Federated term, having a more peer-to-peer feel.
An owner, or in future — owners, of private data can provide access for external organisations to build models on their data without sharing that data.
The most likely scenario for data-centric is where a person or organisation has data they want to protect and instead of hosting the model, they host data. A data scientist (who is not the data owner!) makes requests for training his model or inference against that data.

In the model centric world, certainly where horizontal data is concerned, there’s typically a pre-configured, pre-trained model ready to be improved. But here, in the data-centric approach, in order to fully unlock the power of the data in the network, techniques and tools will be needed to allow sufficient data discovery, wrangling and preparation. At the same time, it will be necessary to meter, limit and control any data leakage.

### What's Next?
I’ve already mentioned **Federated Transfer Learning**, but expect to see papers on **Self-Supervised**, **Few shot learning**. Outside of supervised learning, expect also **Reinforcement Federated Learning** to appear.

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7273662254481330176-ZuTY?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is up to you 😉 you can choose among the several type of diverse implementations of FL !
