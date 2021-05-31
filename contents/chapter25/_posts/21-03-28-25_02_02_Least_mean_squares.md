---
layout: post
title: "25-02-02 Least mean squares"
chapter: "25"
order: "09"
owner: "YoungJae Choung"
---

지금까지는 regression 문제를 residual의 $$l_2$$ norm이나 $$l_1$$ norm을 최소화하는 문제로 풀었었다. 이들 방법보다 좀 더 robust한 방법이 있을까?

Residual의 median을 최소화하도록 regression을 할 경우 좀 더 robust한 regression을 할 수 있다. 이를 **Least Median of Squares**라고 하는데 데이터의 50% 정도가 corrupt되어도 estimator는 corrupt되지 않을 만큼 robust하다. 하지만 이 문제는 NP-Hard 문제이기도 하다!

이 절에서는 Least Median of Squares 문제를 일반화한 **Least Quantile of Square**문제를 Integer programming으로 어떻게 푸는지 소개한다.
## Least mean squares
$$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$이고 $$y \in \mathbb{R}^{n}$$이라고 하자. 그리고 $$\beta \in \mathbb{R}^{p} $$일 때 $$r : = y - X\beta $$이라고 하자.

#### Observe
* Least squares (LS) : $$\beta_{LS} : = \underset{\beta}{\text{argmin}} \sum_{i} r^2_i$$
* Least absolute deviation (LAD) : $$\beta_{LAD} : = \underset{\beta}{\text{argmin}} \sum_{i} \lvert r_{i} \rvert$$
#### Least Median of Squares (LMS)
>$$\beta_{LMS} : = \underset{\beta}{\text{argmin}} (\text{median} \lvert r_{i} \rvert )$$

## Least quantile regression
Least Median of Squares 문제를 일반화한 Least Quantile of Square문제는 다음과 같이 정의할 수 있다. 여기서 $$r_{q}$$는 $$q$$번째 ordered absolute residual이다. 
#### Least Quantile of Squares (LQS)
>$$\beta_{LQS} : = \underset{\beta}{\text{argmin}} (\lvert r_{(q)} \rvert ), \quad 1 \le q \le n, \quad \lvert r_{1} \rvert \le \lvert r_{2} \rvert \le \cdots \le \lvert r_{n} \rvert$$

#### Key step in the formulation
이제 Least Quantile of Square문제를 Integer Programming으로 재정의해보자. 이때, $$r$$의 각 entry $$i$$에 대해 다음과 같은 binary variable을 사용한다.

>$$ \lvert r_{i} \rvert \le \lvert r_{(q)} \rvert$ or $\lvert r_{i} \rvert \ge \lvert r_{(q)} \rvert $$

#### Integer programming formulation
$$\bar{\mu_{i}}$$와 $$\mu_{i}$$은 threshold로 각각의 개수는 $$k$$개, $$n-k$$개이다.

> $$
> \begin{align}
>   \min_{\beta, \mu, \bar{\mu}, z, \gamma} & \quad {\gamma} \\
>   \text{subject to} & \quad  \gamma \le \lvert r_{i} \rvert + \bar{\mu_{i}}, \quad i = 1, ..., n \\
>   & \quad  \gamma \le \lvert r_{i} \rvert -  \mu_{i}, \quad i = 1, ..., n \\
>   & \quad \bar{\mu_{i}} \le M \cdot z_{i}, \quad i = 1, ..., n \\
>   & \quad \mu_{i} \le M \cdot (1-z_{i}), \quad i = 1, ..., n \\
>   & \quad \sum^{p}_{i=1} z_{i} = q \\
>   & \quad \mu_{i}, \bar{\mu_{i}} \ge 0, \quad i = 1, ..., n \\
>   & \quad z_{i} \in \{0, 1\},  \quad i = 1, ..., n \\
> \end{align}
> $$

이 문제에서 첫번째와 두번쨰 제약조건을 보면 residual의 절대값 $$\lvert r_{i} \rvert$$이 포함되어 있어서 convex relaxation으로 풀 수가 없다. 따라서, 첫번째와 두번쨰 제약조건을 convex function으로 변환해 주어야 한다.


## First-order algorithm
$$\lvert r_{i} \rvert$$는 다음과 같은 형태로 convex function $$H_{q}(\beta)$$로 재정의할 수 있다.
>
$$ \lvert r_{q} \rvert = \lvert y_{(q)} - x^{T}_{(q)} \beta \rvert = H_{q}(\beta) - H_{q+1}(\beta)$$

이때 $$H_{q}(\beta)$$는 다음과 같이 정의된다.

> $$
> \begin{align}
> H_{q}(\beta) = \sum^{n}_{i=q} \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert  = &
> \max_{w} \sum^{n}_{i=1} w_i \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert \\
> & \text{subject to} \sum^{n}_{i=1}  w_i  = n − q + 1 \\
> &0 \le w_i \le 1, i = 1, ..., n \\
> \end{align}
> $$

$$H_{q}(\beta)$$는 앞서 정의된 $$\lvert r_{i} \rvert$$을 작은것부터 큰 순으로 나열할 때, $$q$$번째 이상의 모든 residual의 합이다. 따라서, $$q$$번째 이상의 residual의 합에서 $$q+1$$번째 이상의 residual의 합을 빼면 $$q$$번째의 residual 된다는 것을 알 수 있다.

Subgradient 알고리즘으로 $$H_{q}(\beta) - H_{q+1}(\beta)$$의 local minimum을 구할 수 있다.

* 자세한 내용은 논문 [LEAST QUANTILE REGRESSION VIA MODERN OPTIMIZATION](https://arxiv.org/pdf/1310.8625.pdf) 참조
## Computational results
위의 논문에서  Least Quantile of Square문제를 실험한 결과는 다음 그래프에서 볼 수 있다.

#### Mixed integer programming gap
<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/23721/09.01_06_LQS_results1.PNG" alt="[Fig1] Mixed integer programming gap [3]">
  <figcaption style="text-align: center;">[Fig1] Mixed integer programming gap [3]</figcaption>
</p>
</figure>
<br>

#### Cold vs Warm Starts
<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/23721/09.01_07_LQS_results2.PNG" alt="[Fig2] Cold vs Warm Starts [3]">
  <figcaption style="text-align: center;">[Fig2] Cold vs Warm Starts [3]</figcaption>
</p>
</figure>
<br>