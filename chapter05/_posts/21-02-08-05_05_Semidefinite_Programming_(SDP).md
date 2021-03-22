---
layout: post
title: 05-05 Semidefinite Programming (SDP)
chapter: "05"
order: 6
owner: "Hooncheol Shin"
---

General LP에서 inequality constraint가 linear matrix inequality(LMI)로 교체되면, 이는 *Semidefnite Program*(SDP)이다.

#### Semidefinite Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{xF_1 + \dotsb + x_nF_n + G \preceq 0} \\\\
>    & &&{Ax = b},\\\\
>&\text{where } G, F_1, \dotsb, F_n \in \mathbb{S}^{k} \text{ and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}
>$$

* $$G, F_1, \dotsb, F_n$$가 모두 diagonal matrices면, 위의 inequality constraint는 n개의 linear inequalities와 동일해진다. 이 경우 SDP는 LP와 같다.
* 복수의 LMI는 다음과 같이 단일의 LMI로 표현된다.
> $$
> x_1\hat{F_1} + \dotsb + x_n\hat{F_n} + \hat{G} \preceq 0, \phantom{5} x_1\tilde{F_1} + \dotsb + x_n\tilde{F_n} + \tilde{G} \preceq 0
> $$
> 
> <center>is equivalent to single LMI: </center>
> 
> $$
> x_1
> \begin{bmatrix}
>     \hat{F_1} & 0 \\\\
>     0 & \tilde{F_1} \\\\
> \end{bmatrix} + 
> x_2
> \begin{bmatrix}
>     \hat{F_2} & 0 \\\\
>     0 & \tilde{F_2} \\\\
> \end{bmatrix} + 
> \dotsb
> +
> x_n
> \begin{bmatrix}
>     \hat{F_n} & 0 \\\\
>     0 & \tilde{F_n} \\\\
> \end{bmatrix} + 
> \begin{bmatrix}
>     \hat{G_1} & 0 \\\\
>     0 & \tilde{G_1} \\\\
> \end{bmatrix}
> \preceq 0
> $$

## SDP in Standard form
다음과 같이 표현될 때, semidefinite program의 standard form이라고 한다.

#### Standard form SDP
>$$
>\begin{align}
>    &\text{minimize}_{X} &&{tr(CX)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>    & &&{X \succeq 0},\\\\
>    & \text{where } C, A_1, \dotsc, A_p \in \mathbb{S}^n.
>\end{align}
>$$

* Recall: $$tr(CX) = \sum_{i,j=1}^n C_{ij}X_{ij}$$

모든 SDP는 아래의 과정에 의해 standard form SDP로 변형될 수 있다.

#### Converting SDPs to standard form
**Step1.**  Slack variable S를 이용하여 inequality constraint를 equality constraint로 바꿔준다.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n F_l x_l+ S = -G} \\\\
>    & &&{Ax = b}\\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

**Step2.** step1에서 유도된 equality constraint를 각 component에 대한 식으로 변형한다.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n (F_l x_l)_{ij} + S_{ij} = -G_{ij}, i,j = 1, \dotsc, k} \\\\
>    & &&{Ax = b}\\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

**Step3.** x를 두 개의 nonnegative variables로 치환한다.
$$x = x^{+}  - x^{-}$$이고, $$x^{+} \text{, } x^{-} \succeq 0.$$
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T (x^{+}  - x^{-}) + d} \\\\
>    &\text{subject to } &&{\sum_{l=1}^n (F_l x^{+} _l)_{ij} - \sum_{l=1}^n (F_l x^{-} _l)_{ij} + S_{ij} = -G_{ij}, i,j = 1, \dotsc, k} \\\\
>    & &&{Ax^{+}  - Ax^{+} = b}\\\\
>    & &&{S \succeq 0}\\\\
>    & &&{x^{+} \text{, } x^{-} \succeq 0}.
>\end{align}
>$$

**Step4.** $$X, C, \tilde{A}, \tilde{b}$$를 정의.

* All the blanks are zero.

> $$
> X = 
> \begin{bmatrix}
> diag(x^{+})\\\\
>  & diag(x^{-})\\\\
> && s_{11}\\\\
> &&& s_{12}\\\\
> &&&&\dotsc\\\
> &&&&&s_{ij}\\\\
> &&&&&&\dotsc \\\
> &&&&&&&s_{kk}\\\\
> \end{bmatrix}
> ,$$
> $$
> C = 
> \begin{bmatrix}
> diag(c)\\\\
> & -diag(c) &\\\\
> & & O_{k^2 \text{ x } k^2}\\\\
> \end{bmatrix}
> ,$$
> $$
> P_{ij} = 
> \begin{bmatrix}
> (F_1)_{ij}\\\\
> &(F_2)_{ij}\\\\
> &&\dotsc\\\\
> &&&(F_n)_{ij}\\\\
> &&&&-(F_1)_{ij}\\\\
> &&&&&-(F_2)_{ij}\\\\
> &&&&&&\dotsc\\\\
> &&&&&&&-(F_n)_{ij}\\\\
> &&&&&&&&0&\\\\
> &&&&&&&&&\dotsc\\\\
> &&&&&&&&&&1 \phantom{1} (\text{ij th position})\\\\
> &&&&&&&&&&&\dotsc\\\\
> &&&&&&&&&&&&0\\\\
> \end{bmatrix}
> ,$$
>
> $$
> Q_{i}= 
> \begin{bmatrix}
> diag(A_i)\\\\
> &-diag(A_i)\\\\
> &&O_{k^2 \text{ x } k^2}\\\\
> \end{bmatrix}
> $$
> ($$A_i$$ is ith row of A),
> $$
> \tilde{A} = 
> \begin{bmatrix}
> P_{11}\\\\
> \dotsc\\\\
> P_{kk}\\\\
> Q_{1}\\\\
> \dotsc\\\\
> Q_{p}\\\\
> \end{bmatrix}
> -G_{ij} = tr(P_{ij}X)
> ,$$
>
> $$
> b_i = tr(Q_iX)
> $$,
>
> $$
> \tilde{b} = 
> \begin{bmatrix}
> -G_{11}\\\\
> \dotsc\\\\
> -G_{kk}\\\\
> b_{1}\\\\
> \dotsc\\\\
> b_{p}\\\\
> \end{bmatrix}
> $$.

**Step5.** *Step3*의 문제를 $$X, C, \tilde{A}, \tilde{b}$$로 치환.

>$$
>\begin{align}
>    &\text{minimize}_{X} &&{tr(CX)} \\\\
>    &\text{subject to } &&{tr(\tilde{A}_iX) = \tilde{b}_i, \phantom{5} i=1,\dotsc,k^2+p} \\\\
>    & &&{X \succeq 0}.
>\end{align}
>$$

## SOCP and equivalent SDP
Schur complement[[8](https://en.wikipedia.org/wiki/Schur_complement)]를 이용하여 SOCP의 inequality constraint를 표현하면 SOCP는 SDP의 어떤 특수한 경우로 변형된다. 즉, SOCP $$\subseteq$$ SDP의 관계가 성립한다.

#### Recall: Second-Order Cone Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } &&{\| A_i x + b_i \|_2 \leq c_i^T x + d_i, i = 1, \dotsc, m}\\\\
>    & &&{Fx = g}.
>\end{align}
>$$

#### SOCP to SDP by Schur complement
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } 
>    &&
>    \begin{bmatrix}
>    (c_i^T x + d)I    & A_i x + b_i \\\\
>    (A_i x + b_i)^T & c_i^T x + d \\\\
>    \end{bmatrix} \succeq 0, i = 1, \dotsc, m\\\\
>    & &&{Fx = g}.
>\end{align}
>$$