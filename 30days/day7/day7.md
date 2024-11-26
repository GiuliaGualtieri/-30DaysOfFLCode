## 📅 Date
**26 November 2024**

## 📰 Resource
[Communication-Efficient Learning of Deep Networks from Decentralized Data](https://arxiv.org/pdf/1602.05629)

## 🔖 My Learning

**Federated Averaging (FedAvg)**, introduced by [McMahan et al. in 2017](https://arxiv.org/pdf/1602.05629), and also known as **Local SGD**, is one of the most popular algorithms in Federated Learning (FL).

Here's my final summary of the paper with focus on the strengths, limitations, and future directions:

### **How the Algorithm Works**:

1. The central server sends the current model state to a random selection of clients.
2. Each client performs local training using their dataset with `E` steps of Stochastic Gradient Descent (SGD).
3. The clients return their locally trained models to the server.
4. The server averages the model updates to produce the new global model state.
5. Repeat the process for `T` communication rounds.

### **Strengths**:

- **Handles non-IID Data**: The training data on a given client is typically based on the usage of the mobile device by a particular user, and hence any particular user’s local dataset will not be representative of the population distribution. Experiments have shown that the algorithm seems to be robust to differences in client data distributions.
- **Deal with unbalanced similarly**, as some users will make much heavier use of the service or app than others, leading to varying amounts of local training data. Experiments have shown that the algorithm appears to handle this issue.
- **Reduces Communication**: `FedAvg` can achieve high accuracy with fewer communication rounds, due to the iterative of local SGD before doing the model averaging of the local weights.
- **Scalability**: It’s applicable to various model architectures: a multi-layer perceptron, different convolutional NNs and LSTM. Plus, the algorithm is applicable to any finite-sum objective.


### **Key Experiment Findings**

**In terms of experiments:** In the article, extensive experiments have been performed with this algorithm, demonstrating it is robust to unbalanced and non-IID data distributions, and can reduce the rounds of communication needed to train a deep network on decentralized data by orders of magnitude.

**In terms of results**: Experiments show that federated learning can be made practical, as FedAvg trains high-quality models using relatively few rounds of communication, as demonstrated by results on a variety of model architectures: a multi-layer perceptron, two different convolutional NNs, a two-layer character LSTM, and a large-scale word-level LSTM.

**In terms of numbers:** From the results in the paper, it could be seen that in both the IID and non-IID settings, keeping a small mini-batch size and higher number of training passes on each client per round resulted in the model converging faster. For all model classes, FedAvg converges to a higher level of test accuracy than the baseline FedSGD models. For the CNN, the B = ꝏ; E = 1 FedSGD model reaches 99.22% accuracy in 1200 rounds, while the B = 10 ;E = 20 FedAvg model reaches an accuracy of 99.44% in 300 rounds.

### **Limitations**:
Below are, in my opinion, the limitations I identified by reading the experiment results in the article, investigating the citations and other online resources about the FedAvg algorithm, without hands-on experience with it:
- **Non-Optimal Convergence**: FedAvg may not always find the global minimum, particularly for complex or non-convex problems (see https://michaelfeil.eu/academicpages/projects/projects-995-blog-fedavg-vs-fedpa-gd/)
- **Standard Averaging**: FedAvg exploit standard aggregation technique, which may not fully utilize the potential of more sophisticated aggregation methods. Current work are exploring alternatives as aggregation methods besides averaging and determine under which conditions an aggregation method is better than others. → [Understanding the Limits of Average Aggregation in Federated Learning Scenarios.pdf](https://rcs.cic.ipn.mx/2023_152_12/Understanding%20the%20Limits%20of%20Average%20Aggregation%20in%20Federated%20Learning%20Scenarios.pdf) or [Reviewing Federated Learning Aggregation Algorithms](https://www.mdpi.com/2079-9292/12/10/2287).

### **Future Directions**:
In conclusion, here are the future directions suggested by the article:
- **Improved Privacy Guarantees**: Integrating differential privacy and secure multiparty computation to strengthen privacy without sacrificing accuracy.
- **Advanced Aggregation Methods**: Exploring alternatives to standard averaging to handle diverse client behaviors and data distributions.

## 📮 Post 

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is **Client Sampling**.
> [!NOTE]
> In Federated Networks, **Client Sampling** refers to the process of selecting a random subset of clients (or devices) to participate in each communication round during federated learning.
