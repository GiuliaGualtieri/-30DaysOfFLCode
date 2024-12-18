## 📅 Date
**18 December 2024**

## 📰 Resource
[RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response](https://arxiv.org/pdf/1407.6981)

## 🔖 My Learning
Once of my best PETs simple and efficace is RAPPOR. Published on 2014, it is a privacy-preserving mechanism for collecting statistics from end-user clients. It is based on the idea of randomized response, a technique for collecting aggregate statistics about sensitive data while preserving the privacy of individual users.

### RAPPOR
**Randomized Aggregatable Privacy-Preserving Ordinal Response = RAPPOR**, is a technology for crowdsourcing statistics from end-user client software, anonymously, with strong privacy guarantees.

### Example
A question on a sensitive topic, such as “Are you a member of the Communist party?” [28]. For this question, the survey respondent is asked to flip a fair coin, in secret, and answer an untruthful answer if it comes up heads, but tell the truth otherwise (if the coin comes up tails). The untruthful answer is chosen again by flipping another coin in secret, and return “Yes” and “No” as answers if they get head or tail respectively.

**Analysis**: It is easy to see that he true number of “Yes” answers can be accurately estimated by 2(Y − 0.25), where Y is the proportion of “Yes” responses. In expectation, respondents will provide the true answer 75% of the time, as is easy to see by a case analysis of the two fair coin flips.

The respondents will have differential privacy at the level eps = ln(0.75/(1 − 0.75)) = ln(3). This said, this privacy guarantee degrades if the survey is repeated—e.g., to get fresh, daily statistics—and data is collected multiple times from the same respondent. In this case, to maintain both differential privacy and utility, better mechanisms are needed, like those we present in this paper.

### Applications
Here's some examples of usage of RAPPOR in our daily life, without even knowing it:
- **Chrome**: RAPPOR is used in Chrome to collect statistics about the browser usage.
- **Android**: RAPPOR is used in Android to collect statistics about the usage of the operating system.

### Code
Google released the code of this PETs: https://github.com/google/rappor

### Problem Settings
RAPPOR addresses the challenge of collecting aggregate statistics from users while ensuring strong privacy guarantees. Traditional methods risk exposing individual data, especially when centralized systems store raw user inputs. The core problem lies in balancing the need for meaningful data analysis with robust privacy protections, particularly in environments with untrusted servers or adversaries.

### The Fundamental RAPPOR Algorithm
RAPPOR leverages randomized response techniques combined with advanced encoding methods to address these challenges. Key strategies include:
- **Data Encoding with Bloom Filters**: User data is encoded into **Bloom filters**, which represent items as a set of hashed bits. In general, client’s value `v` is hashed onto the Bloom filter `B` of size `k` using `h` hash functionsThis step ensures that original data is never directly exposed.
- **Permanent Randomized Response (PRR)**: Each user's data is perturbed once using PRR to introduce randomness that prevents individual identification while preserving aggregate patterns.
- **Instantaneous Randomized Response (IRR**): Additional noise is applied during each data reporting event to further obfuscate individual contributions. The Instantaneous randomized response indeed plays several important functions. Instead of directly reporting the same report on every request, the client reports a randomized version. This modification significantly increases the difficulty of tracking a client based on the PRR result, which could otherwise be viewed as a unique identifier in longitudinal reporting scenarios.
- **Aggregation with Differential Privacy**: The aggregated data maintains statistical significance while adhering to differential privacy principles.

> [!TIP]
> Bloom filters serves not only to make reports compact, but also to complicate the life of any attacker (since any one bit in the Bloom filter may have multiple data items in its pre-image).


### PETs in Action
RAPPOR introduces a multi-step process to ensure secure data collection:
- **Data Encoding**: User data is hashed into a Bloom filter, reducing the risk of leakage by converting raw inputs into an abstract representation.
- **Randomized Response Mechanisms**: PRR and IRR are applied to introduce randomness. This dual-stage process ensures individual privacy at both permanent and reporting levels.
- **Secure Aggregation**: The noisy, randomized data from all users is aggregated, allowing analysts to infer population-level trends without accessing individual-level data.

### Applications
RAPPOR is well-suited for large-scale, privacy-preserving telemetry systems and other scenarios requiring secure data collection:
- **Browser Telemetry** Measuring browser usage trends, crash reports, or feature adoption without compromising user anonymity.
- **Healthcare Data**: Aggregating sensitive patient data for population-level studies while protecting individual privacy.
- **IoT Devices**: Collecting data from connected devices in smart homes or industrial settings while ensuring compliance with privacy standards.
- **Behavioral Analytics**: Understanding user behavior in apps or websites without tracking or storing identifiable data.

### Key Insights:
- It's been built on the ideas of randomized response.
- It does not require a trusted third party
- it's performed locally on the client.
- it's possible to compute mathematical proof to assess DP guarantees.

### Drawback:
- fits for crowdsourcing statistics.
- works only for few shots, if the survey is repeated to get fresh, daily statistics and data is collected multiple times from the same respondent, the privacy guarantee degrades.
- practical implementation of the RAPPOR algorithm requires specification of a number of parameters

## 📮 Post 

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is **Randomized Response Mechanisms**.
> [!NOTE]
> **Randomized Response Mechanisms** is Bloom filters, which represent items as a set of hashed bits. This step ensures that original data is never directly exposed.
