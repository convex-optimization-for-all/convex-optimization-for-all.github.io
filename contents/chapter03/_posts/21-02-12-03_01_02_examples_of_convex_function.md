---
layout: post
title: 03-01-02 Examples of convex functions
chapter: "03"
order: "04"
owner: "Minjoo Lee"
---
이 절에서는 대표적인 convex function에 대해 살펴본다. Convex fnuction에는 다음과 같은 것들이 있다.

* Exponential function
* Power function
* affine
* quadratic
* least squares loss
* norm
* indicator function
* support function
* max function 

## Univariate function
* Exponential function: 
임의의 실수 $$a$$에 대해서, $$e^{ax}$$ 는 convex 이다.<br>
> $$e^{ax}$$ is convex for any $$a \in \mathbb{R}$$

* Power function: 
음수가 아닌 실수 $$x, a \in \mathbb{R}_{+}$$ 에 대해서, $$a$$가 속한 구간에 따라 $$x^a$$는 convex 혹은 concave이다. <br>
> $$x^{a}$$ is convex on $$\mathbb{R}_{+}$$ for any $$a \geq 1$$ or $$a \leq 0$$
> $$x^{a}$$ is concave on $$\mathbb{R}_{+}$$f for any $$0 \leq a \leq 1$$


## Aﬃne function
[03-01-01]({% post_url contents/chapter03/21-02-12-03_01_01_convex_functions_definition %}) 절에서 언급한 바와 같이 모든 affine function은 convex이면서 동시에 concave 이다.

* on $$\mathbb{R}$$ and $$\mathbb{R}^n$$ <br> 
> $$a^Tx + b$$ is convex and concave

* on $$\mathbb{R}^{m \times n}$$ <br>
> $$\text{tr}(A^TX) + b = \sum_{i=1}^m\sum_{j=1}^n A_{ij}X_{ij} + b$$ is convex and concave


## Quadratic function
이차 함수 $$f(x)={1\over 2}x^TPx+q^Tx+r$$를 살펴보면, $$∇f(x)= Px+q$$ 이고 $$∇^2f(x) = P$$ 이다. 만일 $$P$$가 positive semideﬁnite이면 $$f(x)$$는 convex이다.
주어진 $$P \succeq 0$$ 에 대해
>$$f(x)={1\over 2}x^TPx+q^Tx+r$$ is convex with $$P \in \mathbb{S}^n, q \in \mathbb{R}^n, r \in \mathbb{R}$$

**Q : $$P$$가 positive semideﬁnite이면 왜 $$f(x)$$는 convex인가?** <br>
A : 2차 함수에서 2차항의 계수는 함수의 2차 미분인 Hessian matrix이다. 
Hessian matrix는 함수의 곡률(curvature)을 결정하며 positive semidefinite이면 함수가 아래로 볼록하다는 의미이다. (즉, Hessian matrix의 eigen vector 방향으로의 곡률이 0이상이 된다.) 
따라서 2차 함수에서 2차항의 계수가 positive semidefinite이면 함수는 convex이다.
## Least squares loss
임의의 $$A$$에 대하여 $$A^TA$$는 항상 positive semideﬁnite이므로 $$\left \| Ax - b \right \|_{2}^{2}$$ 는 언제나 convex 이다. 

> $$f(x) = \left \lVert Ax - b \right \Vert_{2}^{2}$$ is convex for any $$A$$


## Norm
모든 $$\mathbb{R}^n$$ 상의 Norm은 Convex 이다. 
$$f:\mathbb{R}^n -> \mathbb{R}$$를 norm이라 하고 정의에 의해

>$$
\begin{aligned}
f(\theta x+(1−\theta)y) \le \theta f(x)+(1−\theta)f(y), \text{  with } \theta \le \theta \le 1, \text{ for all } x,y \in dom f,\\
\end{aligned} 
$$
>$$
\begin{aligned}
\|x\|_{p} = (\sum_{i=1}^{n} x_i^p)^{1/p} \text{ for } p ≥ 1, \|x\| = max_{i=1,.., n} |x_i|\\
\end{aligned} 
$$


## Indicator function
임의의 집합 $$C$$가 convex이면 이에 해당하지 않는 $$x$$에 대해 무한대($$∞$$)로 정의한 indicator 함수도 convex 이다.

즉. 정의 되지 않는 부분을 정의된 부분보다 항상 크게하여 convex의 성질을 가지게 한다.

>$$
I_{C} (x) =
\begin{cases}
0, & \text{x ∈ C}\\
∞, & \text{x ∉ C}\\
\end{cases}
>$$


## Support function
임의의 집합 $$C$$가 있다고 가정하자. 집합 $$C$$가 Convex 이건 아니건 상관 없이 $$C$$의 support 함수는 convex 이다
> $$I_{C}^{*} (x)$$ = $$\max_{y∈C} x^Ty$$ is convex

Support function의 정의는 [Wikipedia 정의](https://en.wikipedia.org/wiki/Support_function)를 참고하라.

## Max function
연속된 Convex 함수들의 Max 함수는 Convex 이다.
즉, 연속된 Convex 함수들의 최댓값들을 이은 외각은 Convex가 된다.
> $$f(x) = \max \{x_1,..., x_n\}$$ is convex
