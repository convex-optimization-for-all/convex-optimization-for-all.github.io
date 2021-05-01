---
layout: post
title: 16-01 Lagrangian duality revisited
chapter: "16"
order: 2
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

이번 절에서는 Lagrangian을 이용하여 primal problem과 dual problem을 정의할 수 있음을 보이고, 이 정의를 이용하여 standard form의 linear programming 및 quadratic programming의 dual problem을 유도해볼 것이다. 나아가 barrier problem이 적용된 linear programming의 dual problem을 유도해봄으로써, 그 형태가 linear programming의 dual problem에 대한 barrier problem과 같음을 보일 것이다.

<br/>
우선 primal problem과 Lagrangian을 다음과 같이 정의해보자.

#### Primal problem
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

#### Lagrangian
>$$
>L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i (x) + \sum_{j=1}^r v_j l_j (x)
>$$

<br/>
이때 primal problem과 dual problem은 Lagrangian에 대한 문제로 재정의할 수 있다.

#### Rewrited primal problem
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

재정의된 primal problem은 제약조건을 명시하고 있지 않지만, 제약조건을 위반하는 임의의 infeasible $$x$$에 대해 indicator function처럼 동작하는 효과가 있다.

1. 어떤 $$i \in [1, m]$$에 대해 $$h_i(\hat{x}) \gt 0$$이면 $$\hat{x}$$는 infeasible point다. 이때 $$\max_{u,v}$$에 의해 $$u_i h_i(\hat{x})$$는 $$\infty$$로 발산하므로 inequality constraint를 위반하는 임의의 $$\hat{x}$$에 대해 indicator function으로 동작한다.
2. 어떤 $$i \in [1, r]$$에 대해 $$l_i(\hat{x}) \neq 0$$이면 $$\hat{x}$$는 infeasible point다. 이때 $$\max_{u,v}$$에 의해 $$v_i l_i(\hat{x})$$는 $$\infty$$로 발산하므로 equality constraint를 위반하는 임의의 $$\hat{x}$$에 대해 indicator function으로 동작한다.

#### Rewrited dual problem
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

Dual problem에서는 정의역에 대한 relaxation이 필요하므로 primal problem의 제약조건에 대해 indicator function으로 동작해서는 안된다. 고정된 $$u, v$$에 대해 $$\min_x$$를 하는 것으로는 primal problem의 제약조건을 강제할 수 없기 때문에 재정의된 dual problem에서 또한 정의역을 relaxation하는 효과가 있다. (참고: [11-02 Lagrange dual function]({% post_url chapter11/21-03-24-11_2_Lagrange_dual_function %}))

## Weak and strong duality
Weak duality와 strong duality에 대해 다시 살펴보도록 한다.

#### Theorem: weak duality
$$p$$와 $$d$$가 primal problem과 dual problem에 대한 각각의 optimal value라고 할때, 항상 다음을 만족한다.


$$
p \ge d
$$

#### Theorem: strong duality (refined Slater's condition)
정의역 집합 $$D$$에 대해, $$f, h_1, \dots, h_p$$가 convex이고 $$h_{p+1}, \dots, h_m, l_1, \dots, l_r$$이 affine이라고 가정해보자. 만약 다음을 만족하는 $$\hat{x} \in \text{relint}(D)$$가 존재하면,
> $$
\begin{align}
h_i(\hat{x}) \lt 0, i=1, \dots, p \\
h_i(\hat{x}) \le 0, i=p+1, \dots, m \\
l_j(\hat{x}) = 0, j = 1, \dots, r
\end{align}
$$

primal problem과 dual problem의 optimal value $$p, d$$에 대해 $$p = d$$가 보장된다.

## Example: linear programming
앞서 정의한 dual problem을 이용하여 linear programming의 dual problem을 유도해보자.

#### Primal problem of LP in standard form
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

앞선 정의에 따라 위 문제의 dual problem은 다음과 같다.
$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \: c^Tx - s^Tx + (b-Ax)^T y$$

$$\nabla_x L = 0$$을 정리하여 얻은 관계식 $$c=A^Ty +s$$를 dual problem에 대입한다.

$$\mathop{\max_{s,y}}_{s\ge0} \: (A^Ty + s)^Tx - s^Tx + (b-Ax)^Ty \quad \text{ s.t. } c=A^Ty +s$$

이는 아래와 같이 정리된다.

#### Dual problem of LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = 0 \\\\
>    &\quad s \ge 0
>\end{align}
>$$


## Example: convex quadratic programming
이번엔 앞서 정의한 dual problem을 이용하여 quadratic programming의 dual problem을 유도해보겠다.

#### Primal problem of QP in standard form
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad \frac{1}{2} x^T Q x + c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0,
>\end{align} \\
>\text{where } Q \text{is symmetric and positive semidefinite.}$$


앞선 정의에 따라 위 문제의 dual problem은 다음과 같다.
$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \:  \frac{1}{2} x^T Q x + c^Tx - s^Tx + (b-Ax)^T y$$

$$\nabla_x L = 0$$을 정리하여 얻은 관계식 $$Qx = A^Ty +s - c$$를 dual problem에 대입한다.

$$
\begin{align}
&\mathop{\max_{s,y,x}}_{s\ge0} \: \frac{1}{2} x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0} \: x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y -  \frac{1}{2} x^T (A^Ty +s - c) \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T (A^Ty +s - c) \quad  \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T Q x \quad \text{ s.t. } Qx = A^Ty +s - c
\end{align}
$$

이는 아래와 같이 정리된다.

#### Dual problem of QP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y,x} &\quad b^Ty - \frac{1}{2} x^T Q x\\\\
>    \text{subject to} &\quad A^Ty +  s - c = Qx \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Quadratic 문제의 dual problem은 또한 quadratic 문제가 된다.

## Example: barrier problem for linear programming
Linear programming에 대한 barrier problem은 다음과 같이 정의한다.

#### Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\\\
>    \text{subject to} &\quad Ax = b, \\\\
>\end{align}
>\text{where }\tau > 0$$.

앞선 정의에 따라 위 문제의 dual problem은 다음과 같다.
$$
\begin{align}
\max_{y} \min_{x} \: L(x,y) &= \max_{y} \min_{x} \:  c^Tx - \tau \sum_{i=1}^n \log(x_i) + (b-Ax)^T y\\\\
&=  \max_{y} \min_{x} \:  \underbrace{(c-A^Ty)}_{s \doteq c-A^Ty}x - \tau \sum_{i=1}^n \log(x_i) + b^Ty\\\\
&= \max_{y} \min_{x} \: \sum_{i=1}^n \big( s_i^Tx_i - \tau  \log(x_i) \big) + b^Ty  \quad \text{ s.t. } A^Ty +s = c
\end{align}
$$

여기서 $$\sum_{i=1}^n \big( s_i^Tx_i - \tau  \log(x_i) \big) + b^Ty$$는 $$x_i = \frac{\tau}{s_i}$$일때 최소화될 것이다. 그러므로 $$\frac{\tau}{s_i}$$를 dual problem의 $$x_i$$에 대입해보자.

$$
\begin{align}
&\max_{s,y} \: b^Ty + n\tau - \tau \sum_{i=1}^n log(\frac{\tau}{s_i}) \quad \text{ s.t. } A^Ty +s = c\\\\
&= \max_{s,y} \: b^Ty + \tau \sum_{i=1}^n log(s_i) + n\tau - n\tau\log(\tau) \quad \text{ s.t. } A^Ty +s = c\\\\
\end{align}
$$

$$n\tau - n\tau\log(\tau)$$는 문제에서 생략되어도 무방하므로, dual problem은 다음과 같이 정리된다.

#### Dual problem of Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

Linear programming의 dual problem에 대한 barrier problem과 문제가 동일함을 알 수 있다.