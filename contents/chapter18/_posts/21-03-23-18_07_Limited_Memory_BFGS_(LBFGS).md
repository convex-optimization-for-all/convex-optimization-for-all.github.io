---
layout: post
title: 18-07 Limited Memory BFGS (LBFGS)
chapter: "18"
order: 8
owner: "Hooncheol Shin"
---

## Introduction

LBFGS는 Limited-memory quasi-Newton methods의 한 예시로써, Hessian 행렬을 계산하거나 저장하기 위한 비용이 합리적이지 않을 경우 유용하게 사용된다. 이 방법은 밀도가 높은 $$n \times n$$의 Hessian 행렬을 저장하는 대신 $$n$$차원의 벡터 몇 개만을 유지하여 Hessian 행렬을 추정(approximation)하는 방식이다. 

LBFGS의 알고리즘은 그 이름이 시사하는 것처럼 BGFS를 기반으로 한다. 주요한 아이디어는 Hessian에 대한 추정을 하기위해 가장 최근의 iteration들에서의 curvature information을 이용하자는 것이다. 반면 오래된 iteration들의 curvature information은 현재 iteration의 Hessian이 보이는 동향(behavior)과 다소 거리가 있을 것이므로 저장공간을 아끼는 측면에서 사용하지 않도록 한다.

여담으로 동일한 기법을 통해 다른 quasi-Newton 알고리즘(가령, SR1)의 limited-memory version도 유도 가능하다 [14].

## LBFGS

LBFGS를 본격적으로 설명하기에 앞서 BFGS method에 대해 다시 살펴보자. 각 step에서 BFGS는 다음과 같이 $$x$$를 업데이트 한다.
>$$
>x^+ = x - t H \nabla f, \\\\
>\text{where } t \text{ is the step length and } H \text{ is updated at every iteration by means of the formula, }\\\\
>\text{     }\\\\
>H^+ =  \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}.\\\\
>$$

$$H$$에 대한 업데이트 식을 이용하면 $$H^+q, q \in \mathbb{R}^n$$를 임의의 스칼라 $$\alpha, \beta \in \mathbb{R}$$와 임의의 벡터 $$p, s \in \mathbb{R}^n$$를 사용해 표현할 수 있다. 

>$$
>\begin{align}
>H^+q &=  \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big)q + \frac{ss^Tq}{y^Ts}\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) \underbrace{H \\big( q - \frac{s^T q}{y^Ts} y \big)}_{p} + \underbrace{\frac{s^Tq}{y^Ts}}_{\alpha} s\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) p + \alpha s\\\\
> &= p - \underbrace{\frac{y^Tp}{y^Ts}}_{\beta}s + \alpha s \\\\
> &= p + (\alpha - \beta) s,\\\\
>& \text{where } \alpha = \frac{s^Tq}{y^Ts}, q^+ = q - \alpha y, p = Hq, \beta = \frac{y^Tp}{y^Ts}.
>\end{align}\\\\
>$$

$$H$$가 k번의 BFGS update를 통해 얻이진다고 할때, $$Hq= -H\nabla f(x)$$는 length k의 반복문 2개로 계산할 수 있다 (아래 알고리즘 참고). 단, 메모리의 효율적인 사용을 위해 가장 최근 $m$개 iterations에서의 curvature information만을 이용한다. ($$k \ge m$$)

## Algorithm
<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/22155/algorithm_quasi-newton.png" alt="[Fig1] The algorithm of LBFGS [3]" width="90%">
  <figcaption style="text-align: center;">[Fig1] The algorithm of LBFGS [3]</figcaption>
</p>
</figure>

보통 inverse Hessian approximation $$H_k$$는 dense하며, 변수의 개수가 많은 경우 저장 및 연산 비용이 매우 높아지게 된다. 반면 LBFGS는 $$H_k \nabla f_k$$을 연속한 벡터합과 벡터곱으로 얻어냄으로써 $$H_k$$의 계산 및 유지를 위한 비용문제를 완화시킬 수 있다. 뿐만 아니라 이 계산에 사용되는 initial Hessian approximation $$H^{0,k}$$는 보통 (실전에서 매우 효과적으로 작동한다고 검증된) identity matrix에 어떤 상수를 곱한 형태($$H^{0,k} = \gamma_k I$$)를 띄기 때문에 유지 및 계산에 그다지 큰 비용이 발생하지 않는다 ([14]의 7.2).
> $$
> H^{0,k} = \gamma_k I, \\\\
> \text{where } \: \gamma_k = \frac{s^T_{k-1}y_{k-1}}{y^T_{k-1}y_{k-1}}.
> $$

* **Note:** $$H^{0,k}$$는 매 iteration마다 다르게 선택될 수 있다.