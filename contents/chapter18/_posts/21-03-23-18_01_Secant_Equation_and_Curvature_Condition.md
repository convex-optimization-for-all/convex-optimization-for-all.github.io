---
layout: post
title: 18-01 Secant Equation and Curvature Condition
chapter: "18"
order: 2
owner: "Hooncheol Shin"
---

## Secant Equation
앞서 $$B$$는 $$\nabla^2 f(x)$$를 근사하는 행렬이라고 했다. 행렬 $$B$$가 Hessian $$\nabla^2 f(x)$$와 비슷한 성질을 갖기 위해서는 secant equation이라는 조건을 만족해야 한다. $$x^{k+1} = x^k + s^k$$이고 $$f$$가 두 번 이상 미분 가능할 때, $$\nabla f(x^k + s^k)$$에 대한 first-order Taylor expansion은 true Hessian이 다음의 성질을 가짐을 보인다.

>$$\nabla f(x^k + s^k)  \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k$$

이때 $$\nabla^2 f(x^k)$$에 대한 근사 행렬을 $$B^{k+1}$$이라 한다. 이 행렬은 다음의 등식을 만족시킨다.

>$$\nabla f(x^k + s^k)  = \nabla f(x^k) + B^{k+1} s^k$$

$$x^{k+1} = x^k + s^k, y^k = \nabla f(x^{k + 1})  - \nabla f(x^k)$$이면 위 등식은 아래와 같이 정리되고, 이를 secant equation이라 부른다.

>$$
>B^{k+1} s^k = y^k
>$$

## The Intuition of Secant Equation

$$x$$축은 $$x^k$$를, $$y$$축은 $$\nabla f(x^k)$$를 나타낸다고 할때 $$B^{k+1}$$은 $$(x^k, \nabla f(x^k))$$와 $$(x^{k+1}, \nabla f(x^{k+1}))$$를 통과하는 직선의 기울기와 같다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/22150/intuition_of_secant_eq.png" alt="[Fig1] The intuition of secant equation" width="70%">
  <figcaption style="text-align: center;">[Fig1] The intuition of secant equation</figcaption>
</p>
</figure>

## Conditions to Determine $$B^+$$
행렬 $$B$$를 기반으로 계산된 $$B^+$$는 다음의 3가지 조건을 만족해야한다.

1. $$B^+$$ is symmetric: Hessian에 대한 추정이기 때문이다.
2. $$B^+$$  close to $$B$$: 유일한 $$B^+$$를 결정하기 위한 조건. $$B$$가 이미 유용한 정보를 가지고 있으므로 secant equation을 만족하는 $$B^+$$ 중에서 $$B$$와 최대한 가까운 행렬을 고른다.
3. $$B$$ is positive definite $$\Rightarrow B^+$$ is positive definite: Global optimum을 보장하기 위해서 문제의 convexity를 유지한다. (참고: [Analyzing the hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf))

## Curvature Condition
$$B^+$$가 positive definite이면서 $$B^+ s = y$$라는 것은 다음의 사실을 암시한다.
>$$s^T y = s^T B^+ s > 0.$$

(참고: [positive definite in WikiPedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

여기서 $$s^T y > 0$$을 curvature condition이라 부른다. Curvature condition을 만족하면, secant equation $$B^+ s = y$$은 항상 solution($$B^+$$)을 갖는다.
