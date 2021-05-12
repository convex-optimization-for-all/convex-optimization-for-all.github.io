---
layout: post
title: 17-05 Optimality conditions for semideﬁnite programming 
chapter: "17"
order: 9
owner: "Minjoo Lee"
---
이 절에서는 SDP(semideﬁnite programming) 문제에 대한 Primer-Dual method의 예시를 살펴보려고 한다.

## SDP (semideﬁnite programming)
SDP의 primal 문제는 다음과 같이 정의한다.
>$$
>\begin{align}
>    &\min_{x} && {C \cdot X} \\\\
>    &\text{subject to } && {A_i \cdot X = b_i, i = 1,...,m} \\\\
>    & &&{X \succeq 0}
>\end{align}
>$$


SDP의 dual 문제는 다음과 같이 정의한다.
>$$
>\begin{align}
>    &\max_{y} && {b^Ty} \\\\
>    &\text{subject to } && {\sum^m_{X_i=1} y_iA_i + S = C} \\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

참고로 $$\mathbb{S}^n$$의 trace inner product는 다음과 같이 표기한다.
> $$X \cdot S = \text{trace}(XS)$$

## Optimality conditions for SDP
SDP의 primal과 dual 문제는 다음과 같이 linear map을 이용해서 정의할 수 있다.

>$$
>\begin{align}
>    &\min_{x} && {C \cdot X} & \qquad \qquad \qquad & \max_{y,S}  && {b^Ty} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} & \qquad \qquad \qquad & \text{subject to } && {\mathcal{A}^{∗}(y) + S = C} \\\\\
>    & &&{X \succeq 0} & \qquad \qquad \qquad & &&{S \succeq 0}
>\end{align}
>$$


여기서 $$\mathcal{A}: \mathbb{S}^n → \mathbb{R}^m$$ 는 linear map을 의미한다.

Strong duality를 만족한다고 가정했을 때,  $$X^{\star}$$ 와 $$(y^{\star}, S^{\star})$$는 $$(X^{\star}, y^{\star}, S^{\star})$$의 솔루션은 primal과 dual의 최적 솔루션이며 그역도 성립한다.

> $$
> \begin{array}{rcl}
> \mathcal{A}^∗(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & 0 \\\
> X,S & \succeq & 0
> \end{array}
> $$


## Central path for SDP
**Primal barrier problem**
>$$
>\begin{align}
>    &\min_{x} && {C \cdot X−τ \log(det(X))} \\\\
>    &\text{subject to } && {A(X) = b} 
>\end{align}
>$$


**Dual barrier problem**
>$$
>\begin{align}
>    &\max_{y, S} && {b^Ty + τ \log(det(S))} \\\\
>    &\text{subject to } && {\mathcal{A}^∗(y) + S = C} 
>\end{align}
>$$


**Primal & dual을 위한 Optimality conditions**
> $$
> \begin{array}{rcl}
> \mathcal{A}^∗(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & τI \\\
> X,S & \succ & 0
> \end{array}
> $$


## Newton step
Primal central path equations 
> $$
> \begin{array}{rcl}
> \mathcal{A}^∗(y) + \tau X^{−1} & = & C \\\
> \mathcal{A}(X) & = & b \\\
> X & \succ & 0
> \end{array}
> $$


Newton equations
> $$τX^{−1}\Delta XX^{−1} +\mathcal{A}^∗(\Delta y) = −(\mathcal{A}^∗(y) + \tau X^{−1} −C)$$
> $$\mathcal{A}(\Delta X) = −(\mathcal{A}(X)−b)$$

Dual에 대한 central path equation과 Newton equation도 $$(y,S)$$를 포함해서 이와 유사하게 정의된다.

## Primal-dual Newton step 
Primal central path equations 
> $$\begin{bmatrix}
\mathcal{A}^∗(y) + S - C  \\\
\mathcal{A}(X) - b \\\
XS
\end{bmatrix} =
\begin{bmatrix}
0 \\\
0 \\\
τI
\end{bmatrix}
, X, S \succ 0
$$

Newton step:
> $$\begin{bmatrix}
0 & \mathcal{A}^∗ & I \\\
\mathcal{A} & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
\Delta X \\\
\Delta y \\\
\Delta S
\end{bmatrix}= −
\begin{bmatrix}
\mathcal{A}^∗(y) + s−c \\\
\mathcal{A}(x) − b \\\
XS − \tau I 
\end{bmatrix}$$

