## 📅 Date
**11 December 2024**

## 📰 Resource
[SyftBox](https://syftbox-documentation.openmined.org/) library.


## 🔖 My Learning
Expanding beyond the [#RingApp](../day10/day10.md) example of the [SyftBox](https://syftbox-documentation.openmined.org/) library, today I would like to talk of a poject I'm working with other colleagues attending the 30DaysOfFLCode.com.

Our project is called **Federated Browser History Analyzer System**.

With my fellows [Irina](https://github.com/IrinaMBejan), [Gustavo](https://github.com/gubertoli) and [Vivek](https://github.com/VivekSil), as part of the challenge #30DaysOfFLCode like me, we started to implement a Federated Reccomender Systems based on the browser history features. 

Unfortunately, is not a straightforward task, as the data is not directly available even locally and of course highly confidential, so it's super important to keep information locally. 

### The Project
Main steps we've been working on are:

1️⃣ We started working on a way to retrieve the data from the browser history and then process it locally and successively share the feautures with Privacy Enhancing Technologies (PETs) in order to ensure the privacy of the users.

The browsers that've been incorporated in our model so far are: 
  - [Google Chrome](https://www.linkedin.com/company/google-chrome/)
  - [Brave](https://www.linkedin.com/company/brave-software/)
  - [Firefox](https://www.linkedin.com/products/mozilla-corporation-firefox-desktop-mobile-enterprise/)
  - [Safari](https://www.linkedin.com/company/apple/)

2️⃣ We worked on the preprocessing of the data, that is cleaning, filtering and extracting fundamental component of a url. For this goal we exploited the `urllib` python packege, especially the `parse` module.

3️⃣ Use an hashing function to anonymize the data. We used the `SHA-256` hashing function to anonymize the data. To achieve this we use the `hashlib` python package.

4️⃣ Compute a similarity matrix between the users' browser history. We used the `difflib` python package, in particular the `SequenceMatcher` class.

> [!TIP]
> My fellows shared this interesting paper: [Federated Learning for Ranking Browser History Suggestions](https://arxiv.org/pdf/1911.11807) that could be a good study for our project.

### Considerations
Today I went on giving my contributions in the project (both `feat` like implementin the similarity computation, and `doc` like updating the README.md).
I'm happy to see the progress we are making and the results we are achieving.
As soon as possible (I hope on Friday) we will show to the SyftBox community the results of our work!
Looking forward to it! 🚀

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7272676912852840450-MXsL?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is *Data Anonymization with Hashing*.
> [!NOTE]
> **Hashing** is a mathematical process that converts an input (e.g., a string) into a fixed-length output known as a hash. In Federated Learning, hashing is used to anonymize sensitive data, making it difficult to reconstruct the original information from the hash. Algorithms like SHA-256 are commonly employed for this purpose.

