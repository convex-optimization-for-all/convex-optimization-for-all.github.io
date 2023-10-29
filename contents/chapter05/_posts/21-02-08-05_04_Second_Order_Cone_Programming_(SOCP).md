---
layout: post
title: 05-04 Second-Order Cone Programming (SOCP)
chapter: "05"
order: 5
owner: "Hooncheol Shin"
---

General LP에서 inequality constraint가 우항이 affine function인 second-order cone costraint로 교체되면, 이는 *Second-Order Cone Program*(SOCP)이다.

### Second-Order Cone Program

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } &&{\| A_i x + b_i \|_2 \leq c_i^T x + d_i, i = 1, \dotsc, m}\\\\
>    & &&{Fx = g},\\\\
>    & \text{where } &&x \in \mathbb{R}^n \text{ is the optimization variable, } A_i  \in \mathbb{R}^{n_i \text{ x n}}, \text{ and } F \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$

### Recall: Norm cone
*Norm cone*은 반경 $$t$$ 이내인 점들로 이뤄진 cone으로 $$(x,t)$$로 정의되는 $$R^{n+1}$$차원의 convex cone이다. 이때, 반경은  임의의 norm으로 정의된다.

>$$\left\{(x, t) : \left \Vert x \right \| \le t \right\} \text{, for a norm } \left \Vert  · \right \|$$

아래 그림에는 $$l_2$$ norm $$\left \Vert  · \right \|_2$$에 대한 norm cone이 그려져 있다. 이를 *second-order cone* 또는 ice cream cone이라고도 부른다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_04_Norm_Cone.png" alt="[Fig1] Norm Cone [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Norm Cone [1]</figcaption>
</p>
</figure>

## QCQP and equivalent SOCP
QCQP는 다음의 유도과정을 거쳐 SOCP의 한가지 특수한 경우로 변형된다. (즉, QCQP $$\subseteq$$ SOCP)

### Recall: Quadratically Constrained Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m \text{, and } A \in \mathbb{R}^{\text{p x n}}
>\end{align}\\
>$$
>

**Step1.** 유도과정의 편의를 위해 약간 다른 형태로 QCQP를 재정의한다.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{x^T P_0 x + 2q_0^T x + r_0} \\\\
>    &\text{subject to } &&{x^T P_i x + 2q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } && P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m \text{, and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$
>

**Step2.** $$P_0$$는 positive semidefinite matrix이므로 $$P_0 = \tilde{P_0}\tilde{P_0}$$를 만족하는 $$ \tilde{P_0}$$ 또한 positive semidefinite matrix이다[[5](https://en.wikipedia.org/wiki/Positive-definite_matrix#Further_properties)]. $$\tilde{P_0}$$는 eigendecomposition[[6](https://en.wikipedia.org/wiki/Matrix_decomposition#Eigendecomposition)]에 의해 $$Q_0 \Lambda_0 Q_0^{-1}$$($$ = Q_0 \Lambda_0 Q_0^T$$ [[7](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix#Real_symmetric_matrices)])로 분해될 수 있는데 이를 이용하여 QCQP의 objective function을 변형하면 다음과 같다.

* $$P_0 = Q_0 \Lambda_0 \Lambda_0 Q_0^T$$
* $$I = Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^{-1} = Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^{-1}$$

> $$
> \begin{align}
> {x^T P_0 x + 2q_0^T x + r_0} &= {x^T P_0 x + q_0^T x + x^T q_0 + q_0^T P_0^{-1} q_0 - q_0^T P_0^{-1} q_0 + r_0}\\\\
> &= {x^T Q_0 \Lambda_0 \Lambda_0 Q_0^T x} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^{-1} x} + {x^T Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^{-1} q_0} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0^{-1} Q_0^T q_0} - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> &=(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0)^T(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0) - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> &=\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> \end{align}
> $$

**Step3.** Inequality constraint function에도 Step2와 같은 방법을 적용한뒤, Step1의 QCQP에 대입한다.

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - {q_0^T P_0^{-1} q_0 + r_0}} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i}}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$
>

**Step4.** 목적함수의 $${q_0^T P_0^{-1} q_0 + r_0}$$는 상수이므로 생략되어도 무방하다.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i} }, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

**Step5.** Scalar variable t를 도입하여 Step4에서와 동일한 문제를 정의할 수 있다.
>$$
>\begin{align}
>    &\text{minimize}_{x, t} &&{t} \\\\
>    &\text{subject to } &&\lVert{\Lambda_{0} Q_0^T x + \Lambda_0^{-1} Q_0^T q_0} \rVert_2^2 \leq t\\\\
>    & &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i} }, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

위는 SOCP의 한가지 특수한 경우에 해당한다. 즉, QCQP $$\subseteq$$ SOCP의 관계가 성립한다.
