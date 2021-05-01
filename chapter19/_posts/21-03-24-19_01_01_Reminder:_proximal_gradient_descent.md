---
layout: post
title: 19-01-01 Reminder - proximal gradient descent
chapter: "19"
order: 3
owner: "Hooncheol Shin"
---

이번 장에서 배울 **Proximal newton method**의 살펴보기 전에 먼저 **Proximal gradient descent**를 복습해 보자.

자세한 내용은 [09 Proximal Gradient Descent and Acceleration](https://wikidocs.net/19031) 참조.

## Proximal gradient descent
**Proximal gradient descent** 다음의 문제에 대해 작동한다. 

>$$f(x) = g(x) + h(x)$$ 

* $$g$$는 convex이고 differentiable하다. (**dom**$$(g) = \mathbb{R}^n$$)
* $$h$$는 convex이고 non-differentiable하며 "simple"하다.


#### Algorithm
Proximal gradient descent는 시작점 $$x^{(0)}$$에서 시작해서 다음 과정을 반복한다.

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) ),k=1,2,3,...$$

여기서 $$\text{prox}_{t}(\cdot)$$는 $$h$$와 연관된 proximal operator 이다.

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

Update 식은 generalized gradient $$G_{t}$$를 사용해서 표준화된 형태로 표현할 수도 있다.

> \begin{align}
> x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{where} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\\\
> \end{align}

#### Performance
* **Proximal gradient descent**의 성능은 $$h$$에 따라 달라질 수 있다. 만일, $$h$$가 복잡한 함수이고 특히 closed form이 아니라면 minimize할 때 계산을 많이 해야 하므로 성능이 매우 떨어질 수 있다.

* 또한, $$g$$함수의 convergence rate와 같은 수렴 속도를 갖는다. 단, 반복할 때마다 prox operator를 실행하기 때문에 prox 계산이 효율적인 경우에만 유용하다.

## Motivation
**Proximal gradient descent**에서는 미분 가능한 함수 $$g$$를 Tayor 2차식으로 근사하고 여기에 미분이 되지 않는 함수인 $$h$$를 더하여 목적 함수로 정의한 후 이를 반복적으로 최소화한다. 따라서, 다음과 같이 2차 식으로 정리해 볼 수 있다. 

식에 전개되는 자세한 과정은 [09-01 Proximal gradient descent](https://wikidocs.net/19032) 참고.

> $$
> \begin{align}
x^+ & = \underset{z}{\text{argmin}}  \, \frac{1}{2t} \parallel x - t \nabla g(x) - z \parallel_2 ^2 + h(z) \\\\
> & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\\\
> \end{align}
> $$

두번째 식의 1항과 2항은 $$g$$의 Tayor 2차 근사식으로 부터 유도할 수 있는데, 먼저 상수항 $$g(x)$$은 제거하고 (gradient descent에서와 마찬가지로) Hessian $$\nabla^2 g(x)$$을 $$\frac{1}{t} I$$(spherical curvature)로 대체해서 구할 수 있다.

다음 그림에서는 proximal gradient descent의 update 단계에서 $$g$$를 2차 근사식으로 최소화 하는 과정을 보여주고 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/22431/09.01_01_proximal_gradient_descent.PNG" alt="[Fig 1] Proximal gradient descent updates [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Proximal gradient descent updates [3]</figcaption>
</p>
</figure>

Gradient descent와 newton's method의 차이점는 2차 근사를 할 때 함수의 local hessian인 $$\nabla^2 g(x)$$를 사용하는지 여부이다. 그렇다면, 위의 식에서 $$\frac{1}{t} I$$ 대신에 $$\nabla^2 g(x)$$를 사용하면 어떻게 될까?

이것이 바로 다음 절에서 설명하게 될 **proximal newton method**가 나오게 된 배경이다.
