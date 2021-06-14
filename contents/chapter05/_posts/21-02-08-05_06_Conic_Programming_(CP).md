---
layout: post
title: 05-06 Conic Programming (CP)
chapter: "05"
order: 7
owner: "Hooncheol Shin"
---

General LP에서 inequality constraint가 generalized inequality constraint로 교체되면, 이는 *Conic Program*(CP)이다.

#### Conic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Fx + g \preceq_{K} 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&c, x \in \mathbb{R}^{n}, A \in \mathbb{R}^{p \text{ x } n}, \text{and } b \in \mathbb{R}^{p}.
>\end{align}\\
>$$

* $$F: \mathbb{R}^n \rightarrow Y$$ is a linear map, $$g \in Y$$, for Eucliean space Y.
* LP는 $$K = \mathbb{R}_{+}^n$$일때이며, 이는 CP의 special case에 해당한다.
* SDP는 $$K = \mathbb{S}_{+}^n$$일때이며, 이 또한 CP의 special case에 해당한다. 즉, SDP $$\subseteq$$ CP의 관계가 성립한다.