---
layout: post
title: 21-03 Example - Lasso regression and group lasso Regression
chapter: "21"
order: "04"
owner: "Hooncheol Shin"
---

## Lasso regression
Lasso regression 문제를 ADMM으로 해결해본다.

$$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n\times p}$$ 일때 lasso 문제는 아래와 같다.
>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda||\beta||_{1}
>\end{align}
>$$

이전의 여러 장에서, 우리는 lasso 문제를 여러가지 방법으로 해결해보았다. 대표적으로는 [proximal gradient descent(ISTA)]({% post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}), [accelerated proximal gradient descent(FISTA)]({% post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}), [barrier method]({% post_url contents/chapter15/21-03-28-15_barrier_method %}), [primal-dual interior-point method]({% post_url contents/chapter17/21-05-01-17_primal_dual_interior_point_method %}) 등이 있다. 

ADMM에서는 dual 식을 유도하는 것과 동일하게, 어떤 식으로 보조 변수(auxiliary variable)을 설정하는가에 따라 알고리즘의 성능이 달라진다. 많은 auxiliary variable의 설정 방법 중 아래의 형태가 가장 효과적인 형태 중 하나로 알려져 있다.
>$$
>\begin{align}
>&\min_{\beta, \alpha} &&||y-X\beta||^{2}_{2}+\lambda||\alpha||_{1}\\\\
>&\text{subject to} &&\beta-\alpha= 0.
>\end{align}
>$$

이 식에 대하여 ADMM update는 아래와 같이 유도된다. $$\beta$$에 대한 식은 $$\beta$$가 2차식이므로 미분을 통하여 최솟값을 구할 수 있고, $$\alpha$$에 대한 식은 앞서 [07장(07-03-04)]({% post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %})에서 다루었던 문제와 같이 $$\beta^{+}+w$$의 soft-thresholding의 형태로 해가 됨이 알려져 있다.
>$$
>\begin{align}
>\beta^{+} &= \underset{\beta}{\operatorname{argmin}}\frac{1}{2}||y-X\beta||^{2}_{2}+\frac{\rho}{2}||\beta-\alpha+w||^{2}_{2}\\\\
>&= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= \underset{\alpha}{\operatorname{argmin}}\lambda||\alpha||_{1}+\frac{\rho}{2}||\beta^{+}-\alpha+w||^{2}_{2}\\\\
>&= S_{\frac{\lambda}{\rho}}(\beta^{+}+w)\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

이 결과는 아래와 같은 특징들을 갖는다.

* 행렬 $$X^{T}X+\rho I$$는 $$\rho>0$$이므로 $$X$$에 관계없이 항상 invertible하다.
* 만약 factorization(대표적으로 Cholesky factorization)을 $$O(\rho^{3})$$ flops 안에 계산하면, $$\beta$$에 대한 update는 $$O(\rho^{2})$$ flops가 걸린다.
* $$\alpha$$ update는 soft-thersholding operator $$S_{t}$$를 적용하는 것이 되며, $$S_{t}$$는 [07-03-04]({% post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %})의 내용과 동일하다.
* ADMM 스텝은 ridge regression 계수들을 매번 soft-thresholding하는 것과 "거의" 동일하다.
* $$\rho$$를 다르게 주면 다른 결과가 나온다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/lasso.png" alt="[Fig 1] Comparison of various algorithms for lasso regression (50 instances with n = 100, p = 20) [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Comparison of various algorithms for lasso regression (50 instances with n = 100, p = 20) [3]</figcaption>
</p>
</figure>


[Fig 1]은 lasso regression 문제에 대한 다양한 알고리즘들의 수렴을 비교한 것이다. 모든 알고리즘들은 iteration마다 동일한 계산복잡도를 가지고 있다. 그래프의 수렴 속도에서 볼 수 있다시피, ADMM은 proximal gradient descent(검정)와 비슷한 수렴 속도를 가진다. Accelerated proximal gradient descent(빨강)는 "Nestrov ripples"를 가지지만 조금 더 빠른 수렴 속도를 보인다. 또한  ADMM은 $$\rho$$ 값에 따라 다른 수렴 속도를 보인다는 특성도 확인할 수 있다. 후에 [23장]({% post_url contents/chapter23/21-03-28-23_Coordinate_Descent %})에서 논하게 될 Coordinate descent(초록)의 경우는 문제에서 더 많은 정보들을 사용하고, 따라서 다른 방법들에 비해 빠른 수렴 속도를 가진다. Coordinate descent의 단점은 문제하기 위한 조건들이 존재한다는 것이다.
$$\rho$$값을 너무 크게 설정하면, 목적함수에서 $$f+g$$를 최소화 하는 비중이 작고, $$\rho$$값을 너무 작게 설정하면, feasiblity가 떨어진다. 따라서 적절한 $$\rho$$값의 설정이 중요하다. 자세한 내용은 [21장 reference 논문]({% post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}) 중 [BPCPE]에서 논하고 있다.

## Group lasso regression
위와 동일하게  Group lasso regression 문제 또한 ADMM으로 해결하는 것에 대하여 살펴보고자 한다. Group lasso regression의 문제정의는 아래와 같다. $$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n \times p}$$일때,

>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\beta_{(g)}||_{2}.
>\end{align}
>$$

Lasso regression과 동일하게 문제를 다시 정리할 수 있다.
>$$
>\begin{align}
>&\min_{\beta,\alpha} &&\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\beta_{(g)}||_{2}\\\\
>&\text{subject to} &&\beta-\alpha=0.
>\end{align}
>$$

ADMM step은 다음과 같다.
>$$
>\begin{align}
>\beta^{+} &= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= R_{c_{g}\frac{\lambda}{\rho}}(\beta^{+}_{(g)}+w_{(g)})\qquad \text{g = 1,...G}\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

이 결과는 아래와 같은 특징들을 갖는다.

* 행렬 $$X^{T}X+\rho I$$는 $$\rho>0$$이므로 $$X$$에 관계없이 항상 invertible하다.
* 만약 factorization(대표적으로 Cholesky factorization)을 $$O(\rho^{3})$$ flops 안에 계산하면, $$\beta$$에 대한 update는 $$O(\rho^{2})$$ flops가 걸린다.
* $$\alpha$$ update는 group soft-thersholding operator $$R_{t}$$를 적용하는 것이 되며, $$R_{t}$$는 아래와 같이 정의된다.

>\begin{align}
>R_{t}(x) = (1-\frac{x}{\lVert x \rVert_{2}})_{+}x
>\end{align}

