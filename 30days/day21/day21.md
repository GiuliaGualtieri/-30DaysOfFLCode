## 📅 Date
**10 December 2024**

## 📰 Resource
[Privacy Preserving AI (Andrew Trask) | MIT Deep Learning Series](https://www.youtube.com/watch?v=4zrU54VIK6k) 

## 🔖 My Learning

My challenge still goes on. For 30 days, I’m dedicating at least one hour each day to exploring FL. Today I watched the following talk on **Privacy Preserving AI** by [**Andrew Trask**](https://www.linkedin.com/in/andrew-trask-3763ba15b/?original_referer=https%3A%2F%2Fwww.google.com%2F&originalSubdomain=uk), from the MIT Deep Learning Series four years ago.

Here’s a synthesis with key takeaways:

### **Key Points**:

1. **Core Question**: 
   > "Is it possible to answer questions using data we cannot see?"
   This drives the talk about privacy-preserving AI challenges, aiming to work with sensitive data while maintaining privacy.

2. **Privacy Tools**:
    - **Differential Privacy**: a technology that consists by adding noise to data queries to protect individual information.
    - **Homomorphic Encryption**: a technology that allows computation on encrypted data without decryption, preserving privacy.
    - **Secure Multiparty Computation (SMC)**: a method that enables multiple parties to compute a function of their data jointly without revealing their private inputs to one another

3. **Challenges**:
    - **Privacy and Utility tradeoff**: The main challenge for all this techniques in handling private data is that they have to be able to preserve privacy while not compromising accuracy.

4. **Practical Examples**:
    - **Remote Execution**: Computation on data held at remote locations without direct access to the raw data.
    - **Federated Learning**: Model training occurs on devices like smartphones, aggregating only updates—not raw data—to protect privacy of individuals.

5. **Broader Impact**:
    - Creating a system where sensitive information is securely utilized for ML could revolutionize sectors from healthcare to finance.
    - Developing privacy-preserving AI can lower the barriers to accessing crucial datasets for impactful research.

### **Memorable Quotes**:

> "We need to reduce the barrier to make the most important problems accessible for machine learning engineers while ensuring privacy."

Most of our daily life situation we collect very powerful and meaningful data that we are not allowed to use because of privacy concerns. The necessity of a privacy preserving environment where we could use this data is crucial.

> "Differential privacy is about adding noise to provide plausible deniability to individuals in a dataset."

I think these simple words are able to describe the idea behind Differential Privacy for whos is not familiar with the concept. 

> I believe the need is sufficiently significant. If you look at our lives, they are essentially a long process of answering important questions, like figuring out where we’ll get food or understanding what causes cancer. Ensuring that people can answer these questions without their data being exposed or misused—and preventing the wrong people from accessing sensitive information—is crucial.

> I understand that some aspects of the talk might sound a bit ridiculous, but I hope you can at least see that, theoretically, the fundamental building blocks are already in place. What really stands between us and a fundamentally different world is the adoption and maturation of the technology, combined with good engineering.

### **Why It Matters**:

The talk provides an excellent introduction to the topic, and I highly recommend it. It is highly educational and enjoyable to follow.
Moreover, it was very convincing in highlighting the importance of privacy-preserving AI and its potential impact on society.
With the above quotes, I hope to have shown how the talk was highly convincing, engaging, and delivered in a fluent and very pleasant dialect.

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7272506614471946241-aRPS?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Remote Executio**n.
> [!NOTE]
> **Remote Execution** is a technique that allows computation on data held at remote locations without direct access to the raw data. It is a key technology for privacy-preserving AI, enabling the use of sensitive data without compromising individual privacy.
