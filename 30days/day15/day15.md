 ## 📅 Date
**4 December 2024**

## 📰 Resource
[Federated Learning and Privacy](https://dl.acm.org/doi/pdf/10.1145/3500240)

## 🔖 My Learning

### Privacy for Federated Computations
Regarding the data minimization principle: the raw data stays on the device, and updates sent to the server are focused on a particular purpose and aggregated as soon as possible.  Aggregation approach limits the influence of any individual client on the output, but algorithms need to be carefully designed if the goal is to provide more formal guarantees such as differential privacy.

**Key Focus**: In analyzing the privacy properties of a federated system, it is useful to consider access points and threat models. 

Looking at the image below, some questions may raises, like:
- *With access to the physical device or network?*
- *With root or physical access to the servers providing the FL service?* 
- *To the models and metrics released to the ML engineer?*
- *To the final deployed model?*

So I discovered that the number of potentially malicious parties varies dramatically as information flows through this system.
> [!IMPORTANT]
> A very small number of parties should have physical or root access to the coordinating server, for example, but nearly anyone might be able to access the fi-nal model shipped out to a large fleet of smartphones.

Privacy claims must therefore be assessed for a complete end-to-end system. Required guarantees:
- the final deployed model has not memorized user data
- security precautions must be taken to protect the raw data on the device or on any intermediate computation state in transit. 
- data minimization (minimizing the retention of data) and anonymous aggregation (protects individuals’ data from parties with access to these released outputs) must be applied.


### Data Minimization for Aggregation
> [!IMPORTANT]
> FL systems can be viewed as a kind of privacy-preserving technology in themselves, structurally preventing the server from accessing anything about a client’s data that was not included in the update submitted by that client.

In the aggregation phase of FL there is a challenge that I wasn't aware of. An idealized system would like to have a completely trusted third party who aggregates the clients’ updates and reveals only the final aggregate model to the central server. In reality, no such mutually trusted third party typically exists to play this role, but various technologies allow an FL system to simulate such a third party under a wide range of conditions. Privacy enhancing Technolgies are under research to make the central server in a FL system acting like also the third party trusted by everyone. Howveer this is not straightforward.

Let's see some of the technologies cited in the paper:
1. **Secure Enclave**, a specially constructed piece of hardware that can not only prove to the clients what code it is running, but also ensure no one (not even the hardware’s owner) can observe or tamper with the execution of that code. 
2. Distributed cryptographic protocols for **Secure Multiparty Computation** (SMC)can be used collaboratively to simulate a trusted third party without the need for specialized hardware, so long as a sufficiently large number of the participants behave honestly. However, secure multiparty computation remains computationally prohibitive in most cases. 
3. **Specialized secure aggregation algorithms for vector summation** in the federated setting have been developed that provably preserve privacy even against an adversary that observes the server and controls a significant fraction of the clients, while maintaining robustness against clients dropping out of the computation. Such algorithms seem to be both: **Communication efficient**, communication per client; and **Computation efficient**, computation per client. 
4. **Cryptographic secure aggregation protocols** have been deployed in commercial federated computing systems for years. Moreover, beyond private aggregation, privacy preserving technologies can be used to secure other parts of an FL system. For example, cryptographic techniques, like **zero-knowledge proofs**, can be used to ensure that the server can trust that clients have preprocessed faithfully. 

### Computing and Verifying Anonymous Aggregates

While secure enclaves and private aggregation techniques can strengthen data minimization, they are not designed specifically to produce anonymous aggregates. The paper suggests that to protect individual contributions to the federated model in order to ensure anonymity and prevent sensitive information leakage. The gold-standard approach to data anonymization is differential privacy (DP).

**Differential Privacy** (DP): Introduces noise to ensure no single user's data significantly impacts the aggregated outcome. For example, DP-SGD clips gradients and adds noise during training.

Depending on the FL systems, the application of DP could vary. n the context of cross-device FL, a record is defined as all the training examples of a single user/client.In the context of cross-silo FL, the unit of privacy can take on a different meaning. 

**Distributed DP**, can be used. The goal is to render the output differentially private before it becomes visible.

DP assumes a “worst-case adversary" with infinite computation and access to arbitrary side information. These assumptions are often unrealistic in practice. Thus, there are substantial advantages to training using a DP algorithm that limits each user’s influence. Nevertheless, designing practical **FL and FA algorithms enhanced with DP-algorithm** is an important area of ongoing research.

Model auditing techniques can be used to further quantify the advantages of training with DP. However, quantifying the gap between DP’s worst-case adversaries and realistic ones with limited computational power and side information is not strainghtfoward.
For example, empirical auditsare model memorization tests, to verify that models do not retain identifiable data traces.

**User-Level DP**: aims to ensure anonymity for all data contributed by an specific individual, as a record is defined as all the training examples of a single user/client.
**Example-level DP**: aims to ensure privacy protection to each training examples, as a record corresponds to a single training example.
The key point is that in general one user may contribute many training examples. 

**Verification of Anonymity**: Empirical audits (e.g., model memorization tests) verify that models do not retain identifiable data traces, even under the assumption of worst-case adversaries.

**Trade-Offs**: Achieving strong DP guarantees often requires adding significant noise, which can degrade model accuracy. Balancing privacy and utility is an ongoing research challenge.

Both chapters highlight the importance of combining advanced privacy-preserving technologies with practical considerations to protect data and ensure compliance in federated systems. These approaches mitigate risks of privacy breaches while supporting robust federated analytics and machine learning.

### ✨ What's Next?
- **Federated Analytics**.

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7270154692289056769-6Nhi?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Data Minimization**.
> [!NOTE]
> Data Minimization principle is a privacy principle that states that organizations should only collect, use, and retain personal data that is necessary for the completion of a specific purpose.
