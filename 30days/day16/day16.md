## 📅 Date
**5 December 2024**

## 📰 Resource
[Federated Learning and Privacy](https://dl.acm.org/doi/pdf/10.1145/3500240)

[Federated Analytics: Collaborative Data Science without Data Collection](https://research.google/blog/federated-analytics-collaborative-data-science-without-data-collection/)

## 🔖 My Learning

The focus of the article I studied so far has primarily been on Federated Learning.  However, another key concept in this setting of machine learning research field is **Federated Analytics**. 
So today my new learning was the acquisition af a distinct subfields in the context of Federated Networks.

### Federated Analytics
Beyond learning ML models, data analysts are often interested in applying data science methods to the analysis of raw data that is stored locally on users’ devices. 
For example, analysts may be interested in learning aggregate model metrics, popular trends and activities, or geospatial location heatmaps. 
All of this can be done using **Federated Analytics** (FA). 

Similar to FL, FA works by running local computations over each device’s data and making only the aggregated results available to product engineers. Unlike FL, however, **FA aims to support basic data science needs**, such as counts, averages, histograms, quantiles, and other SQL-like queries.

FA tasks can differ from FL ones in several ways: 
1. FA algorithms are often **noninteractive and involve rounds** with a large number of clients. In other words, unlike FL applications, there are no diminishing returns from having more clients in a round. Therefore, applying DP is less challenging in FA since each round can contain a large number of clients, and fewer rounds are needed. 
2. There is **no need for the same clients to participate again in later rounds**. In fact, clients that participate again may bias the results of the algorithm. Therefore, an FA task is best served by an infrastructure that limits the number of times any individual can participate. 
3. FA tasks are typically sparse, making **[efficient private sparse aggregation](https://arxiv.org/abs/2007.14861)** a particularly important topic; many open research questions exist in this space. It is worth noting that while limiting client participation and sparse aggregation are particularly relevant to FA, they have applications for FL problems as well.


### My Final Considerations of the article
The world of FL engineers seems to be optimistic that FL will continue to expand, both as a research field and as a set of practical tools and software systems that allow application by more people to more types of data and problem domains. For what I learnt so far, I agree with them. I discovered some intresting tool to develop custom FL solutions, like:

- [SyftBox](https://github.com/OpenMined/syft) - Discover SyftBox, an exciting new project by OpenMined that puts Privacy-Enhancing Technologies at its core.

- [Flower](https://github.com/adap/flower) - An ML framework agnostic friendly Federated AI network developed by Flower Labs.

- [Fedn](https://github.com/scaleoutsystems/fedn) - An enterprise-ready federated learning framework developed by Scaleout Systems.

> [!TIP]
> There is an interesting article that details the recent (up to 2021) [Advances and Open Problems in Federated Learning provides a broad survey](https://arxiv.org/pdf/1912.04977), with coverage of important topics not covered in the article studied so far, including personalization, robustness, fairness, and systems challenges. 

> [!TIP]
> Next hands-on introduction to FL, such as trying out algorithms in a simulation environment on either your own data or standard datasets, the [TensorFlow Federated tutorials](https://www.tensorflow.org/federated/tutorials/tutorials_overview?hl=it) are a great place to start—they can be executed and modified on the fly in the browser using Google Colab.

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7270502943064301569-zJ8I?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Federated Analytics**.
> [!NOTE]
> **Federated Analytics** refers to the practice of running local computations over each device’s data and making only the aggregated results available to product engineers. 
