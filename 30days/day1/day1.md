## 📅 Date
**20 November 2024**

## 📰 Resource
[Federated Learning: Challenges, Methods, and Future Directions: 1. Introduction ](https://arxiv.org/pdf/1908.07873)

## 🔖 My Learning

**Introduction** <br>
Federated learning involves training statistical models over remote devices or siloed data centers, such as mobile phones or hospitals, while keeping data localized.

**Current Context** <br>
Mobile phones, wearable devices, and autonomous vehicles are just a few of the modern distributed networks generating lots of data each day.

**Motivation** <br>
Due to the growing computational power of these devices, coupled with concerns over transmitting private information, it is increasingly attractive to store data locally and push network computation to the edge.

**Goals** <br>
Federated learning explores training statistical models directly on remote devices.

**Requirements** <br>
Requirements: undamental advances in areas such as privacy, large-scale machine learning, and distributed optimization

**Canonical Applications** <br>
Several canonical applications of federated learning are:
- **Mobile Phones**:
    - FL helps train models for tasks like next-word prediction, face detection, and voice recognition using data from many smartphones.
    - This approach protects user privacy, reduces bandwidth usage, and preserves battery life by keeping data local.
    - Example: Learning a next-word predictor based on users' historical text data without sharing their personal information.
- **Organizations (e.g., Hospitals)**:
    - FL can be used in predictive healthcare by training models on sensitive patient data across multiple hospitals while adhering to privacy laws and ethical constraints.
    - This allows private and collaborative learning without transferring raw data between institutions.
- **Internet of Things (IoT)**:
    - FL supports IoT systems like wearables, autonomous vehicles, and smart homes by enabling real-time adaptation to new data (e.g., traffic patterns or pedestrian behavior).
    - It maintains privacy and accommodates limited device connectivity while ensuring models remain up-to-date.

**Problem Formulation** <br>
The federated learning problem involves training a single global model using data stored locally on many devices, where only periodic updates (not raw data) are shared with a central server to minimize a weighted global objective function across all devices.

**Core Challenges in Federated Learning** <br>
**1️⃣ Expensive Communication**: Communication is slow and costly in federated networks due to privacy requirements and the need to keep raw data local. Instead of transmitting entire datasets, devices exchange small updates during training. Key solutions include reducing communication rounds and minimizing message sizes.<br>
**2️⃣ Systems Heterogeneity**: Devices could differ in hardware, connectivity, and power levels. Moreover, only a small fraction of devices are active at any time, and some may disconnect unexpectedly. FL systems must adapt to varied hardware, tolerate device dropouts, and function effectively with limited participation.<br>
**3️⃣ Statistical Heterogeneity**: Devices in federated networks collect and generate data in different ways. Therefore, data across devices are non-IID, but could have unique patterns and varying quantities. This complicates model training and evaluation. Personalized approaches like multi-task learning or meta-learning can address this by tailoring models to individual devices.<br>
**4️⃣ Privacy Concerns**: Sharing model updates instead of raw data enhances privacy but still risks exposing sensitive information. Techniques like _differential privacy_ or _secure multiparty computation_ mitigate these risks, though often at the cost of performance or efficiency. But balancing privacy with functionality remains a key challenge.<br>

👉 Next Chapter: _2.1 Communication Efficiency_ will be studied tomorrow! 

## 📮 Post

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7265094998910509056-fJnH?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Edge Computing**.
> [!NOTE]
> **Edge Computing** refers to processing data near the source where it is generated, instead of sending it all to a central server or data center. In Federated
> Learning, edge computing allows devices like smartphones and IoT gadgets to locally train parts of a machine learning model.

