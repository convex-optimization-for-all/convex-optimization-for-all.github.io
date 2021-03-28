---
layout: post
title: "19-01-02 Proximal Newton method"
chapter: "19"
order: 4
owner: "YoungJae Choung"
---

이전 절에서 **proximal newton method**는 **proximal gradient descent** 식에서 spherical curvature인 $$\frac{1}{t} I$$ 대신에 local hessian인 $$\nabla^2 g(x)$$를 사용하고자 하는 방법임을 설명했다. Proximal newton method는 오래 전에 나온 아이디어로 통계학에서는 local score란 용어로 연구되고 있다.

이제 **proximal newton method**가 어떻게 formulation될 수 있는지 살펴보자.

## Algorithm
Proximal gradient descent 알고리즘은 다음 step의 direction인 $$v$$를 구한 후 step size인 $$t_k$$를 optimization하는 과정으로 이루어져 있다. 

* 1단계 : 시작점 $$x^{(0)}$$에서 시작해서 다음 과정을 반복한다. ($$k=1,2,3,...$$) 

* 2단계 : 다음 step의 direction인 $$v$$를 구한다.

> \begin{align}
v^{(k)} & = \underset{v}{\text{argmin}} \ \nabla g(x^{(k-1)})^T v + \frac{1}{2} v^T H^{(k-1)} v + h(x^{(k-1)} + v)
\end{align}
여기서 $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$은 $$x^{(k-1)}$$에서의 Hessian이다.

* 3단계 : $$v^{(k)}$$ 방향으로 step을 이동하기 위해 step size를 optimization한다. 

> \begin{align}
x^{(k)} & =x^{(k-1)} + t_k v^{(k)}
\end{align}

$$t_k$$는 step size로 $$t_k=1$$이면 pure proximal Newton method이다.

Backtracking line search를 통해 step size를 optimization하는 과정이 있다는 점은 proximal gradient descent method와 다른 점이다.

#### Next position view
위의 식을 direction $$v$$이 아닌 다음 위치인 $z$의 관점에서 표현하면 다음과 같다.

> $$
> \begin{align}
> z^{(k)} &= \underset{z}{\text{argmin}} \ \nabla g(x^{(k-1)})^T (z - x^{(k-1)})^T\\
> &\quad + \frac{1}{2} (z - x^{(k-1)})^T H^{(k-1)} (z - x^{(k-1)}) + h(z) \\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

직관적으로 첫번째 단계에서 목적 함수를 최소화 하는 surrogate point인 $$z$$를 구한다. 그런 다음, $$x^{(k-1)}$$에서 $$z$$의 방향으로 이동하지만 항상 $$z$$로 이동하게 되는 것은 아니다.