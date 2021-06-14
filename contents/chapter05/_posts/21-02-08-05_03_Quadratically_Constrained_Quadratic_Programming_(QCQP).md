---
layout: post
title: 05-03 Quadratically Constrained Quadratic Programming (QCQP)
chapter: "05"
order: "04"
owner: "Hooncheol Shin"
---

Quadratic program에서 inequality contraint function이 이차식(convex quadratic)으로 교체되면, 이는 *Quadratically constrained quadratic program*(QCQP)이라고 불린다.

### Quadratically Constrained Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m \text{, and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$

## QP and equivalent QCQP
  QCQP의 inequality constraint에서 $$P_i = 0, \text{ for } i = 1, \dotsc, m$$이면 QP의 형태와 동일해짐을 알 수 있다. 즉, QP는 QCQP의 한가지 특수한 경우에 해당하며, QP $$\subseteq$$ QCQP의 관계가 성립한다.

### Recall: Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, G \in \mathbb{R}^{\text{m x n}} \text{, and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$