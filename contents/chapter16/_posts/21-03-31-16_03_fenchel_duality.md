---
layout: post
title: 16-03 Fenchel duality
chapter: "16"
order: "04"
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

[13-04 Conjugate function]({% post_url contents/chapter13/21-04-05-13_04_Conjugate_function %})에서 conjugate function을 이용해 dual problem를 유도하는 방법에 대해 알아보았다. Fenchel duality는 conjugate function으로 유도되는 dual problem 중에서도 아래의 형태를 한 것을 지칭한다.

$$
\max_{v} -f^*(A^Tv) - g^*(-v)
$$

이 형태의 문제가 어디서부터 유도되는 것인지 알아보도록 하자.

#### Primal problem

> $$
> \min_{x} \quad f(x) + g(Ax)
> $$

주어진 문제는 equality constraint가 추가된 형태로 재정의 할 수 있다.

#### Primal problem rewrited
> $$
 \begin{align}
 \min_{x,z} &\quad f(x) + g(z)\\\\
 \text{subject to} &\quad Ax = z.
 \end{align}
 $$

Conjugate function을 이용하여 재정의한 primal problem의 dual problem을 유도해보자. <br/>

* **Recall:** $$f^*(s) \doteq  \max_{x} \big( s^Tx - f(x) \big) = \min_{x} \big( f(x) - s^Tx \big)$$

<br/>
$$
\begin{align}
&\max_{v} \min_{x, z} \quad L(x,z,v)\\\\
= &\max_{v} \min_{x, z} \quad f(x) + g(z) + v^T (z - Ax) \\\\
= &\max_{v} \min_{x, z} \quad v^Tz + g(z) - (A^Tv)^Tx + f(x)\\\\
= &\max_{v} \quad  -f^*(A^Tv) - g^*(-v)\\\\
\end{align}
$$

#### Fenchel duality
> $$
> \max_{v} -f^*(A^Tv) - g^*(-v)
> $$

* **Nice Property:** $$f, g$$가 convex이고 닫혀있으면(closed), dual의 dual은 다시 primal이 된다. (Symmetric)

## Example: conic programming

#### Primal problem of CP in standard form
>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
    \text{subject to} &\quad Ax = b \\\\
    &\quad x \in K
\end{align}
$$

위 문제는 두 함수 $$f(x) = c^Tx + I_K(x)$$와 $$g(z) = I_{\{b\}}(z)$$를 이용하여 재정의할 수 있다.<br/>

* **Note:** $$\begin{equation}
    f(x) + g(Ax) = 
    \begin{cases}
      0, & \text{if}\ Ax=b, x \in K \\\\
      \infty, & \text{otherwise}
    \end{cases}
  \end{equation}$$

#### Primal problem of CP rewrited
> $$
> \begin{align}
> \min_{x, z} &\quad  f(x) + g(z)\\\
> \text{subject to} &\quad z  =Ax \\\
> \end{align}
> $$

#### Deriving dual problem of CP

재정의된 CP의 primal problem으로부터 dual problem을 유도해보자. 우선 함수 $$f$$와 $$g$$를 전개하면 아래와 같다.
> $$
> \begin{align}
> \min_{x, z} & \; c^Tx + I_K(x) + I_{\{b\}}(z)  \\\
> \text{subject to} & \;  z   =Ax \\
> \end{align}
> $$

Dual problem의 정의로부터 conjugate function을 이용하여 문제를 전개해보자.

> $$
> \begin{align}
> & \max_{y} \; \min_{x, z} \;  L(x, z, y) \\\
> = \; & \max_{y} \; \min_{x, z} \;  c^Tx + I_K(x) + I_{\{b\}}(z) + y^T(z-Ax) \\\
> = \; & \max_{y}  \;\min_{x, z} \; (c - A^Ty)^Tx  + I_K(x) \;+ \;  y^Tz + I_{\{b\}}(z) \\\
> = \; & \max_{y} \;  \min_{x, z} \; -( (A^Ty - c)^Tx  - I_K(x)) \;  - \; ( - y^Tz - I_{\{b\}}(z) ) \\\
> = \; & \max_{y} \; - I_K^*(A^Ty - c)  -  I_{\{b\}}^*(-y)  \\\
> = \; & \max_{y} \; - I_{-K^*}(A^Ty - c)  - I_{\{b\}}^*(-y)  \\
> \end{align}
> $$

$$I_{-K^*}(A^Ty - c)$$는 constraint로 표현될 수 있다.

> $$
> \begin{align}
> A^Ty - c & = -s, \; -s \in -K^* \\\
> \Leftrightarrow A^Ty + s & = c, \; s \in K^* \\\
> \end{align}
> $$

$$I_{\{b\}}^*(-y) = \max_{b} -b^Ty - I_{\{b\}}(b)$$이므로 문제는 다음과 같이 정리된다.
> $$
> \begin{align}
> \max_{y, s} &\quad -(-b^Ty - I_{\{b\}}(b)) \\\
> \text{subject to} &\quad y^TA + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$

$$I_{\{b\}}(b) = 0$$이므로 문제에서 제거할 수 있다.

#### Dual problem of CP

> $$
> \begin{align}
> \max_{y, s} &\quad  \;  b^Ty  \\\
> \text{subject to} &\quad y^TA + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$ 

* Primal problem과 dual problem중 하나라도 strictly feasible하다면 strong duality를 만족한다.
* Primal problem과 dual problem 둘 다 strictly feasible하다면 strong duality를 만족하고 primal & dual optima가 존재한다.

## Example: semidefinite programming
SDP에 대한 primal & dual problem과 SDP의 barrier problem에 대한 primal & dual problem의 형태를 살펴보도록 하자.

#### Primal problem of SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{X} &&{tr(CX)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>    & &&{X \succeq 0},\\\\
>    & \text{where } C, A_1, \dotsc, A_p \in \mathbb{S}^n.
>\end{align}
>$$

* **Recall:** $$tr(CX) = \sum_{i,j=1}^n C_{ij}X_{ij}$$
* **Note:** SDP는 LP와 달리 항상 strong duality를 만족하는 것은 아님을 유의하자.

#### Dual problem of SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{y} &&{b^Ty} \\\\
>    &\text{subject to } &&{\sum_{i=1}^m y_i A_i + S = C} \\\\
>    & &&{S \succeq 0}.\\\\
>\end{align}
>$$

* **Note:** Positive semidefinite cone은 self-dual cone이다. ($$(\mathbb{S}_{+}^n)^* = \mathbb{S}_{+}^n$$)

#### Primal problem of Barrier problem for SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{X} &&{tr(CX) - \tau \log \big( det(X) \big)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>    & \text{where } C, A_1, \dotsc, A_p \in \mathbb{S}^n.
>\end{align}
>$$

#### Dual problem of Barrier problem for SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{y, S} &&{b^Ty +  \tau \log \big( det(S) \big)} \\\\
>    &\text{subject to } &&{\sum_{i=1}^m y_i A_i + S = C}.
>\end{align}
>$$