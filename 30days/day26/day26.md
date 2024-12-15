## 📅 Date
**15 December 2024**

## 📰 Resource
[Federated CPU Tracker](https://syftbox-documentation.openmined.org/tutorials/cpu-tracker/)

## 🔖 My Learning
Today I studied the solution to address one the current challenge for modern organizations. Nowdays, most of them, often need to monitor CPU usage across their network to optimize performance and resource allocation. This presents a significant security challenge: raw CPU data can be exploited by sophisticated attacks like Hertzbleed and PLATYPUS to extract sensitive information, including cryptographic keys.

OpenMined has developed a solution that uses **Differential privacy** - a mathematical framework that protects sensitive data by adding carefully calibrated noise. This approach strikes an optimal balance: it prevents malicious actors from accessing exact CPU measurements while preserving the statistical utility of the aggregated data for legitimate monitoring purposes.

Using [**SyftBox's API framework**](https://syftbox-documentation.openmined.org/), they built a system that:
- Collects CPU usage data securely
- Applies differential privacy protection automatically
- Enables safe sharing of protected metrics across the SyftBox network

### Project Overview
Two components:
1. The Member API collects raw CPU metrics from individual devices, applies differential privacy, and stores the protected data locally. [`cpu_tracker_member`](https://github.com/OpenMined/cpu_tracker_member)
2. The Aggregator API collects and aggregates privacy-protected CPU metrics across distributed clients, calculating network-wide statistics and presenting them through an interactive dashboard. [`cpu_tracker_leader`](https://github.com/OpenMined/cpu_tracker_leader)

Check the Dashboard : https://syftbox.openmined.org/datasites/aggregator@openmined.org/!

### API Workflow

The execution of the [`cpu_tracker_member`](https://github.com/OpenMined/cpu_tracker_member) API follows these main steps:

1. **Directory Initialization**

2. **Set up shared directories with appropriate permissions**.

3. **CPU Data Collection**
  - Sample CPU usage every 20 seconds, and calculate mean usage
  - Applies differential privacy to protect the data
  - Stores both raw and protected versions in appropriate directories

The [`cpu_tracker_leader`](https://github.com/OpenMined/cpu_tracker_leader) operates in three phases:

1. **Discovery**: The system identifies and validates active participants in the network, establishing secure channels for data collection.

2. **Data Collection**: Protected CPU metrics are gathered from validated peers, ensuring data freshness and correct formatting before processing.

3. **Aggregation and Visualization**: Network-wide statistics are calculated from collected metrics and displayed through an interactive dashboard that enables peer participation.



### Privacy Considerations

The memeber API system implements several privacy-preserving techniques:

- **Differential Privacy**: Protects individual measurements by adding calibrated noise
- **Access Control**: Restricts access to protected data through SyftBox permissions
- **Local Processing**: Ensures raw measurements never leave the local machine
- **Data Separation**: Maintains strict separation between raw and protected data

Additional privacy enhancements could include:

- Adjusting the epsilon parameter for stronger privacy guarantees
- Implementing additional noise mechanisms
- Adding secure aggregation protocols

The aggregator preserves privacy through:

- Exclusive use of differentially private metrics
- Time-limited data retention
- Aggregation of recent measurements only
- No exposure of individual peer data

Future enhancements could incorporate:

- **Secure multi-party computation**
- **Homomorphic encryption**


## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7274010863353675777-aii8?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Differential privacy**.
> [!NOTE]
> **Differential privacy** is a mathematical framework that protects sensitive data by adding carefully calibrated noise.