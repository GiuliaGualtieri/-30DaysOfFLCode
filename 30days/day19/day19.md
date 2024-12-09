## 📅 Date
**8 December 2024**

## 📰 Resource
[FEDERATED OPTIMIZATION IN HETEROGENEOUS NETWORKS](https://arxiv.org/pdf/1812.06127)

## 🔖 My Learning

>[!NOTE]
>`FedAvg` and `FedProx` are stochastic algorithms by nature: in each round, only a fraction of the devices are sampled to perform the update, and the updates performed on each device may be inexact.

### FedProx : Convergence Analysis

It is well known that for stochastic methods in order to converge to a stationary point, a decreasing step-size is required. 

This is in contrast to non-stochastic methods, e.g., gradient descent, that can find a stationary point by employing a constant step-size. 

In order to analyze the convergence behavior of methods with constant step-size (as is usually implemented in practice), we need to quantify the degree of dissimilarity among the local objective functions. 

This could be achieved by assuming the data to be IID, i.e., homogeneous across devices. Unfortunately, in realistic federated networks, this assumption is impractical.   

The article proposes a metric that specifically measures the dissimilarity among local functions (**Local dissimilarity**), and then analyze `FedProx`'s training process focusing on this dissimilarity in order to keep it bounded, proving the convergence rate.

**Local dissimilarity**  
The the article they introduce a measure of dissimilarity between the devices in a federated network, which is sufficient to prove convergence through some detailed mathematical proofs. I suggest my readers to read the article as it's reqally good written, expalined and easy to follow.

**B-local dissimilarity**: The local functions `Fk` are `B-locally dissimilar` at `w` if there exists a `B > 0` such that for all `k` and `k'` and for all `w` in the domain of `Fk` and `Fk'`, we have:
```math
E_{k}[ || \nabla F_{k}(w) ||^{2} ] \leq || \nabla f (w) ||^{2}  B^{2}
```
Here `Ek`denotes the expectation over devices with masses `pk = nk/n` and the total sum of `pk` is equal to 1.

Edge cases:
- when all the local functions are the same, we have `B(w) = 1` for all `w`. 
  
Considerations:
- The data distributions are often heterogeneous and B > 1 due to sampling discrepancies even if the samples are assumed to be IID. 

**Assumption: Bounded dissimilarity**. For some `eps > 0`, there exists a `Beps` such that for all the points 
```math
w \in S_{\epsilon}^{c} = \{ w | || \nabla f (w) ||^{2} > \epsilon \} , B(w) \leq B_{\epsilon}
```
where `S_{\epsilon}` is the set of points where the gradient norm is less than `eps`.

Edge cases:
- `B(w) = 1 ` when `Ek[‖∇Fk (w)‖2] = ‖∇f (w)‖2`, i.e. w is a stationary solution that all the local functions `Fk` agree on.

Considerations:
- For most practical machine learning problems, there is no need to solve the problem to highly accurate stationary solutions --> ok for `epsilon`typically not very small 
- Indeed, it is well-known that solving the problem beyond some threshold may even hurt generalization performance due to overfitting --> keep epsilon small
- Although in practical federated learning problems the samples are not IID, they are still sampled from distributions that are not entirely unrelated --> if this were the case, then fitting a single global model `w` across devices would be ill-advised
- We want that the dissimilarity between local functions remains bounded throughout the training process --> proved with exepriments (next study!)

> [!IMPORTANT]
> The smaller the dissimilarity, the better the convergence.

### `FedProx` Analysis
Using the the **assumption** of **bounded dissimilarity**, the article proves with deatiled theorem and remarks the convergence of the FedProx algorithm.
They estimate the amount of expected decrease in the objective when one step of `FedProx` is performed.
Not only! They start showing the results that hold for non-convex `Fk(·)` objective functions, but then they also show how to characterize the convergence for the special case of convex loss functions with exact minimization in terms of local objectives.


### How?
If, like me, you are asking *how*? I tried to investigate it into details, challenging my neurons. My answer is that if you keep bounded the *l2-norm* of your local objective functions, *bounded* in the sense *close* to the l2-norm of the global objective function computed on the same parameter `w`, but sufficiently *close* in the sense not too much, so with un upper bound (the `B` term), fixed and dependent at each iteration of an espilon which decreases all along the FedProx steps, then you achieve convergence. How to control your local objective functions are close to the global objective function? adding into their computation a **proximal term**, introduced [yesterday](../day18/day18.md) ("l2-norm of the difference between the current local parameters and the parameters of the global model").

So here we are!

## 📮 Post 

[📘 LinkedIn Post](https://www.linkedin.com/posts/giuliagualtieri_30daysofflcode-activity-7271432843124244480-6PPf?utm_source=share&utm_medium=member_desktop)

------
The _**Federated Learning Term of the Day**_ is **Stochastic Algorithms**.
> [!NOTE]
> **Stochastich algorithm** is an algorithm that uses randomness as part of its logic. In the context of Federated Optimization Methods
> the randomness is used to sample a subset of the devices to perform the update in each round.

