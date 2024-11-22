## 📅 Date
**22 November 2024**

## 📰 Resource
[Federated Learning: Challenges, Methods, and Future Directions: 2.2 Systems Heterogeneity](https://arxiv.org/pdf/1908.07873)

## 🔖 My Learning

Today, I learned about another challenge that federated networks must address. 
In federated settings, there's a significant variation in system characteristics across the network—devices can differ in hardware, network connectivity, and battery life. This is known as **Systems Heterogeneity**.
There are several key directions to handle this.  

1️⃣ **Asynchronous communication**  

For those who aren't familiar, **synchronous communication** is the "benchmark" way to coordinate in workflows. It's straightforward because it makes sure every device waits until all others are finished before moving on to the next step. 
On the contrary, **asynchronous communication** lets faster devices move ahead without waiting for the slower ones, which makes it useful in situations where devices have different speeds or capabilities. 
In traditional data center settings, synchronous and asynchronous schemes are both commonly used. 

However, **in federated learning, asynchronous communication is more challenging compared to data centers because the environment is much less predictable.** 
WHY❓ Think about **device variability**. In data centers, servers usually have similar hardware, network speeds, while in federated learning, devices like smartphones, tablets, or wearables have a wide range of hardware capabilities, internet connections, and battery life. 
Another reason is **unbounded delays**. In federated learning, you never know how much time you need to reach a “stable” update into your device, while in data centers there are usually constraints on how much delay will take. 

2️⃣ **Active device sampling**

An alternative approach involves **actively selecting the participating devices at each round**, based on different criteria, for example systems resource or underlying statistical structure.

3️⃣ **Fault tolerance**

Even though it could be a way to address system heterogeneity issues, fault tolerance has become increasingly critical, as it is common for some participating devices to drop out before the completion of a given training iteration.
One practical strategy is to simply ignore such device failure. However, that may introduce bias into the device sampling scheme if the failed devices have specific data characteristics. 
For instance, devices dropped out due to poor network connections induce the global trained federated model to be biased towards devices with favorable network conditions. That's logic!

4️⃣ **Coded computation**  

[Coded computation](https://arxiv.org/abs/2406.00300#:~:text=Coded%20computing%20has%20emerged%20as,than%20the%20raw%20data%20itself) is another option to tolerate device failures, by introducing algorithmic redundancy. 
The main idea is to add some redundancy into the system, such as replicating different version of data to several nodes, in order to be sure that the main operations will be covered by some of them. 
An example is **Gradient Redundancy**. And here I paste the link to a very interesting article that I will like to go into details in next days: [📃](https://arxiv.org/abs/1612.03301) where it has been shown how replicating data blocks and coding across gradients can provide tolerance to failures and stragglers for **Synchronous Gradient Descent**.

> [!TIP]
> Subject of investigation and study: [Gradient Redundancy](https://arxiv.org/abs/1612.03301).

## 📮 Post

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is **Coded computation**.
> [!NOTE]
> **Coded computation** is a technique used to tolerate device failures by introducing algorithmic redundancy. It involves encoding data across multiple nodes, ensuring that even if some nodes fail, the system can still recover the required computation by using the redundant information.
