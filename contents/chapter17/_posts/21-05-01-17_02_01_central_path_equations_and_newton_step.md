---
layout: post
title: 17-02-01 Central path equations and Newton step
chapter: "17"
order: "04"
owner: "Minjoo Lee"
---
**Primal-dual interior-point method**는 barrier method와 마찬가지로 central path를 찾아서 해를 구하는 방식이다. 그러기 위해 perturbed KKT conditions를 residual 함수로 정의하고 이를 0으로 만드는 해를 찾는다. 이 절에서는 이와 같은 접근 방식을 설명하려고 한다.

## Central path equations
앞의 [17-01 Optimality conditions]({% post_url contents/chapter17/21-05-01-17_01_barrier_method_duality_optimality_revisited %})에서 설명했던 central path equations에서 우항을 좌항으로 옮기면 다음과 같이 정리할 수 있다. (Central path equations의 optimality condition을 perturbed KKT conditions라고도 한다.)
> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv & = & 0 \\\
>  Uh(x) + \tau\mathbb{1}  & = & 0 \\\
> Ax−b & = & 0 \\\
> u,−h(x)  & > & 0
> \end{array}
> $$

원래 문제에 대한 KKT conditions에서의 complementary slackness와 inequality constraint가 perturbed KKT conditions에서와 다르다는 점을 유의해서 보자. 원래 문제의 경우 $$Uh(x) = 0$$ 그리고 $$u,−h(x)  \ge 0$$이지만, perturbed KKT conditions에서는 $$Uh(x) = - \tau\mathbb{1}$$ 그리고 $$u,−h(x)  \gt 0$$이다.

이렇게 정리된 비선형 방정식인 perturbed KKT conditions는 Newton's method의 root finding 버전을 이용해서 선형 방정식으로 근사해서 해를 구할 수 있다.

## Newton step
그러면 perturbed KKT conditions를 선형으로 근사하여 해를 구해는 방법에 대해 알아보자. Perturbed KKT conditions 식을 다음과 같은 residual의 함수 $$r(x, u, v) = 0$$로 정의할 수 있다. (함수 이름이 residual인 이유는 이 값들이 0이 되어야 optimal이 되기 때문이다.)

> $$r(x,u,v) :=
> \begin{bmatrix}
> ∇f(x) +∇h(x)u + A^Tv \\\
> Uh(x) + τ\mathbb{1} \\\
> Ax−b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

함수의 근을 찾기 위해 $$r(x, u, v)$$을 Taylor 1차식으로 근사하면 다음과 같다. (이 과정은 non-linear equation을 linear equation으로 근사하는 과정으로 자세한 내용은 [14-02-01 Root finding]({% post_url contents/chapter14/2021-03-26-14_01_newton_method %})을 참조)
>$$\begin{align}
0 & = r(x + \Delta x, u + \Delta u, r + \Delta v)  \\\\
  & \approx r(x, u, v) + \nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} \\\\
\end{align}$$

이에 따라 함수 $$r(x, u, v)$$은 다음과 같이 정리할 수 있다.

>$$\begin{align}
\nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} = -r(x, u, v) \\\\
\end{align}$$

$$r(x, u, v)$$을 $$x, u, v$$에 대해 미분하여 Jacobian matrix $$\nabla r(x, u, v)$$을 구한 후 위의 식을 대입해 보면 아래와 같다.
> $$\begin{bmatrix}
> \nabla^2f(x) + \sum_i u_i \nabla^2h_i(x) & \nabla h(x) & A^T \\\
>  U \nabla  h(x)^T & H(x) & 0 \\\
> A & 0 & 0
> \end{bmatrix}
> \begin{bmatrix}
> \Delta x \\\
> \Delta u \\\
> \Delta v
> \end{bmatrix} = −r(x,u,v)$$
> where
> $$r(x,u,v) :=
> \begin{bmatrix}
> \nabla f(x) +\nabla h(x)u + A^Tv \\\
> Uh(x) + τ\mathbb{1} \\\
> Ax−b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

이 식의 해인 $$(\Delta x, \Delta u, \Delta v)$$는 primal, dual 변수의 업데이트 방향이다. 이 장에서 소개할 방법을 **Primal-Dual** interior point method라고 부르는 이유는 residual 함수를 이용해서 primal, dual 변수를 동시에 업데이트하기 때문이다.