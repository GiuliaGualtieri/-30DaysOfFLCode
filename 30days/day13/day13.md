## 📅 Date
**2 December 2024**

## 📰 Resource
[Federated Learning and Privacy](https://dl.acm.org/doi/pdf/10.1145/3500240)

## 🔖 My Learning

**Main topic** of the article: Building privacy-preserving systems for machine learning and data science on decentralized data.

Let's start with a brief recap of *what is Federated Learning*. **Federated learning** is a machine learning setting where multiple entities (clients) collaborate in solving a machine learning problem, under the coordination of a central server or service provider. Each client’s raw data is stored locally and not exchanged or transferred; instead, focused updates intended for immediate aggregation are used to achieve the learning objective.

### Privacy Principles for Learning and Analytics

**Privacy** is an inherently multifaceted concept. The key components of privacy are: 

1. **Transparency** and **consent**, which are foundational to privacy. They are how users of the product/service both understand and approve of the ways in which their data will be used. 


2. **Data Minimization** principle, which, as applied to aggregations, includes the objective to collect only the data needed for the specific computation (focused collection), to limit access to data at all stages, to process individuals’ data as early as possible (early aggregation), and to discard both collected and processed data as soon as possible (minimal retention). That is, data minimization implies restricting access to all data to the smallest set of people possible, often accomplished via security mechanisms, such as encryption at rest and on the wire, access-control lists, and technologies such as secure multiparty computation and trusted execution environments. 
 
3. **Data Anonymization** principle, which captures the objective that the final released output of the computation does not reveal anything unique to an individual. When this principle is specialized to anonymous aggregation, the goal is that data contributed by any individual user to the computation has only a small (limited, measured, and/ or mitigated) influence on the final aggregate output. For example, aggregate statistics, including model parameters, when released to an engineer should not vary significantly based on whether any particular user’s data was included in the aggregation. The XKCD comic shown here illustrates a humorous example where this principle is not respected, but this memorization phenomenon has been shown to be a real issue for [modern deep networks](https://arxiv.org/pdf/2012.07805). 

![XKCD comic](../images/FL_Memorization_Attack_Meme.png)

Another way to view these principles is that data minimization pertains to how the computation is executed and data is handled, while data anonymization pertains to what is computed and released.

By design, FL structurally embodies data minimization. 

FL can be combined with other techniques (particularly **differential privacy** and **privacy/memorization auditing**, treated in more depth later) to ensure released aggregates are sufficiently anonymous. 

This situation contrasts the privacy relationship you might have with a bank or healthcare provider, where the data anonymization principle may not apply since direct access by the provider to an individual’s sensitive data cannot be avoided; in these interactions, trust in the provider to use the data only for the intended purpose is the fundamental tenet.


What's Next?
- **Federated Learning Settings and Applications**.
- **Cross-Device Federated Learning**.
- **Data Minimization for Aggregation**.
- **Federated Analytics**.

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7269314357153439744-egZN?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Privacy**.
> [!NOTE]
> **Privacy** is an inherently multifaceted concept. The key components of privacy are: **Transparency** and **consent**, **Data Minimization** principle and **Data Anonymization** principle.

