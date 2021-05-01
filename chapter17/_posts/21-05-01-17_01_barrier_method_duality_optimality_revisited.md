---
layout: post
title: 17-01 Barrier method & duality & optimality revisited
chapter: "17"
order: 2
owner: "Minjoo Lee"
---

15장에서 barrier method에 대해, 13장과 16장에서는 duality에 대해 살펴보았다.
본 장의 내용을 다루기 전에 barrier method와 duality에 대해 간단하게 다시 정리해 보고자 한다.



## Barrier method
아래와  같은 primal 문제가 convex이고 $f, h_i , i = 1, . . . m$가 미분가능 할 때,   
> $$\begin{align}
\min_{x} & \quad f(x) \\\
\text{subject to } & \quad h_{i}(x) \leq 0, i = 1, \dotsc, m \\\
& \quad Ax = b \\\
\end{align}$$

Log barrier function을 사용하여 다음과 같이 primal 문제를 barrier 문제로 바꿀 수 있다.

> $$\begin{align}
\min_{x} & \quad f(x) + \frac{1}{t} \phi(x) & & \min_{x} & \quad tf(x) + \phi(x) \\\
\text{subject to } & \quad Ax = b & \iff \qquad & \text{subject to } & \quad Ax = b \\\
\end{align}$$

> where $\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}$

알고리즘은 $t > 0$를 만족하는 $t = t^{(0)}$에서 시작해서 $\frac{m}{t}$가 $\epsilon$보다 작거나 같아질 때까지 증가시킨다. 이때, Newton's method를 이용해 초기값 $x^{(0)}$에 대한 $x^{\star}(t)$를 구하고 $k = 1, 2, 3, . . .$에 대해 각 단계에서  $x^{(k+1)} = x^{\star}(t)$를 구하는 과정을 반복 한다.

알고리즘을 간략히 정리하면 다음과 같다.

1. $t^{(0)} \gt 0$이고 $k := 0$을 선택한다.
2. $t = t^{(0)}$에서 barrier problem을 풀어서 $x^{(0)} = x^{\star}(t)$을 구한다.
3. While $m/t \gt \epsilon$ <br>
  3-1. $t^{(k+1)} = µt$로 업데이트 한다. $(µ > 1)$ <br>
  3-2. Newton's method를 $x^{(k)}$로 초기화한다. (warm start)<br>
        $t = t^{(k+1)}$에서 barrier problem을 풀어서 $x^{(k+1)} = x^{\star}(t)$을 구한다.<br>
  end while<br>

* 자세한 내용은  [15-01-02 Log barrier function & barrier method](https://wikidocs.net/21305) 참조
## Duality
다음과 같은 primal 문제가 주어졌을 때, 
>$$
>\begin{align}
>    \mathop{\text{minimize}}\_x &\quad f(x) \\\\
>    \text{subject to} &\quad f Ax = b \\\\
>    &\quad h(x) \le 0
>\end{align}
>$$

이를 Lagrangian 형태로 바꾸면 다음과 같이 바꿀 수 있다.
>$$
>L(x,u,v) = f(x) + u^Th(x) + v^T(Ax - b)
>$$

이와 같이 정의된 Lagrangian을 이용해서 primal과 dual problem을 다음과 같은 형태로 다시 정의할 수 있다. 자세한 내용은 16장을 다시 살펴보기 바란다.</br>
#### Primal Problem
>$$
>\min_x \mathop{\max_{u,v}}\_{u \geq 0} L(x,u,v)
>$$

#### Dual problem
>$$
>\mathop{\max_{u,v}}\_{u \geq 0} \min_x L(x,u,v)
>$$

## Optimality conditions

$f,h_1,...h_m$은 convex 이고 미분 가능하고, 또한 주어진 문제가 strong duality를 만족한다고 가정할 때, 이 문제에 대한 KKT 최적 조건(optimality condition)은 아래와 같다.

> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv & = & 0 & \text{(Stationarity)}\\\
>  Uh(x) & = & 0 & \text{(Complementary Slackness)} \\\
> Ax & = & b & \text{(Primal Feasibility)}\\\
> u,−h(x)  & ≥ & 0 & \text{(Dual Feasibility)}
> \end{array}
> $$

여기서 $U$는 $\text{diag}(u)$를 뜻하며, $∇h(x)$는 $ \[ ∇h_1(x) ··· ∇h_m(x) \]$를 의미한다.

* 자세한 내용은 [12장 KKT conditions](https://wikidocs.net/20959) 참조

## Central path equations
함수 $f(x)$를 barrier 문제로 아래와 같이 재정의 할 수 있다.</br>
아래 수식에서 $τ$는 $\frac{1}{t}$이며 $\tau$를 점점 0에 가깝게 해서 반복적으로 해를 구함으로써 최종적으로 원래 문제의 해를 구하게 된다.

>$$
>\begin{align}
>    &\min_{x} && {f(x) + τ\phi(x)} \\\\
>    & &&{Ax = b} \\\
>\end{align}
>$$
> $$\text{where } \phi(x) = −\sum_{i=1}^m \log(−h_i(x)).$$

즉, 위 식에서 $τ$에 따라 primal 문제와의 차이가 발생하며, $τ$에 따라 생기는 궤적 즉, barrier 문제에 대한 해의 집합을 central path라고 한다.

그리고 이 barrier 문제에 대한 optimality conditions은 다음과 같다.
> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv  & = & 0 \\\
> Uh(x) & = & −τ\mathbb{1} \\\
> Ax & = & b \\\
> u,−h(x)  & > & 0
> \end{array}
> $$
 
* 자세한 내용은 [16-02 Optimality conditions](https://wikidocs.net/22012) 참조

이번 장에서 소개할 **Primal-Dual interior point method**는 위의 처음 세 가지 식을 residual로 정의하고 이를 $0$으로 줄이면서 해를 구하는 방식이다.

##### Useful fact
솔루션 $(x(τ),u(τ),v(τ))$는 다음의 $mτ$ 즉 $\frac{m}{t}$ 크기 만큼의 duality gap을 갖는다.
> $f(x(τ))−\min_x L(x,u(τ),v(τ)) = mτ= \frac{m}{t}$

