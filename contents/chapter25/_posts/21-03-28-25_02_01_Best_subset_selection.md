---
layout: post
title: "25-02-01 Best subset selection"
chapter: "25"
order: 8
owner: "YoungJae Choung"
---

Integer Programming의 대표적인 예시 중 하나인 best subset selection은 $$p$$개의 entry 중에 k개의 entry를 선택하는 문제이다.

## Best subset selection
$$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$이고 $$y \in \mathbb{R}^{n}$$일 때 best subset selection 문제는 다음과 같다.

> $$
> \begin{align}
> \min_{\beta} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\
> \text{subject to } & \quad \parallel \beta \parallel_{0}  \  \leq  k \\
> \end{align}
> $$

이때 $$\parallel \beta \parallel_{0}$$는 $$\beta$$의 nonzero entry의 개수이다.

지금까지 앞 장에서는 이와 같은 문제를 Lasso problem으로 정의해서 $$l_1$$ norm으로 $$\beta$$를 sparse하게 만들었었다. 이 문제의 경우 $$l_0$$ norm을 사용해서 0이 아닌 entry 개수를 제약하는 문제로
정의 되었는데 제약 조건인 $$\parallel \beta \parallel_{0}  \  \leq  k$$가 non-convex라서 지금까지 배운 convex optimization 기법으로는 문제를 풀 수 없다.

#### Integer programming formulation
그렇다면 이 문제를 Integer programming으로 재정의해보자.

> $$
> \begin{align}
> \min_{\beta, z} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\
> \text{subject to } & \quad \left\vert  \beta_{i} \right\vert  \leq M_{i} \cdot z_{i} \quad i = 1 \dotsc p \\
> & \quad \sum_{i = 1}^{p} z_{i} \leq k \\
> & \quad z_{ji} \in \lbrace 0, 1 \rbrace \quad i = 1 \dotsc p \\
> \end{align}
> $$

Binary 변수 $$z_i$$를 도입해서 $$z_i$$의 합이 $$k$$보다 작게 만듦으로써 위의 문제와 동일해지게 만들었다.  $$M_i$$는 사전에 알고 있는 $$\left\vert  \beta_{i} \right\vert$$의 상한 값으로 $$X$$와 $$y$$를 사전처리해서 계산할 수 있는 값이다.

이제 문제를 Integer Programming으로 정의했으므로 지금부터 Integer Programming 기법으로 풀 수 있다.

## A clever way to get good feasible solutions
문제를 일반화해서 알고리즘을 설명해보자. Objective function $$g : \mathbb{R}^{p} \to \mathbb{R}$$이 smooth convex이고 $$\nabla g$$가 L-Lipschitz이라고 하자.
>
$$\min_{\beta} g(\beta) \quad \text{subject to} \quad \parallel \beta \parallel_{0} \le k$$

Best subset selection의 경우 $$g(\beta) = \frac{1}{2} \parallel X\beta - y \parallel^2_2$$이다.

#### Observation
다음과 같이 정의된 $$H_k(u)$$ 함수를 통해 $$u \in \mathbb{R}^p$$에서 가장 큰 k개 entry를 구할 수 있다.
>
$$ H_k(u) = \underset{\beta : \parallel \beta_{0} \parallel \le k}{\text{argmin}} \parallel \beta - u \parallel^2_2$$

이때, $$H_k(u)$$ 함수는 hard thresholding을 한다. 또한, $$u$$를 집합 $$\beta$$에 projection한 것으로 볼 수도 있다.

#### Discrete first-order algorithm
이제 gradient descent와 함수 $$H_k(u)$$를 이용해서 알고리즘을 정의해보자.

1. $$\beta^{(0)}$$으로 시작
2. for $$k = 0, 1, ...$$ <br>
$$\quad \beta^{(i+1)} = H_k \left(\beta^{(i)} - \frac{1}{L} \nabla g(\beta^{(i)})\right)$$<br>
end for<br>

위의 과정을 반복하면 $$\beta^{(i)} \to \bar{\beta}$$로 수렴하게 된다. 이는 위의 최소화 문제에 대한 local solution이라고 할 수 있다.
>
$$ \bar{\beta} =  H_k \left(\bar{\beta} - \frac{1}{L} \nabla g(\bar{\beta})\right)$$

결과적으로 이 알고리즘은 proximal gradient 알고리즘으로 볼 수 있다. 왜냐하면 함수 $$H_k(u)$$가 proximal operator 역할을 하고 있기 때문이다.
## Computational results
#### Mixed integer programming gap
아래 그림에서 Subset selection problem의 실험 결과를 살펴보자.

왼쪽 그래프에서 upper bound는 바로 optimal이 되었지만 lower bound는 천천히 올라오다가 upper bound와 만나는 지점에서야 optimal임을 알게 된다. 왜냐하면 linear program에서는 solution이 optimal인지 체크할 방법이 없으며 upper bound와 lower bound가 같아졌을 때 optimal임을 알 수 있게 된다.
(참고로 upper bound와 lower bound의 차를 mixed integer programming gap이라고 한다.)

오른쪽 그림은 동일한 실험 결과를 mixed integer programming gap을 작아지는 모습으로 보여주고 있다. 주황색 그래프는 upper bound와 lower bound의 차이인 mixed integer programming gap을 나타내며 점점 줄어들고 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_03_subset_results1.png" alt="[Fig1] Dataset n=350, p = 64, k=6 [3]">
  <figcaption style="text-align: center;">$$[Fig1] Dataset n=350, p = 64, k=6 [3]$$</figcaption>
</p>
</figure>
<br>

#### Cold and Warm Starts
다음 그림에서 warm start가 cold start보다 전체적으로 성능이 매우 우수함을 보여주고 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_04_subset_results2.png" alt="[Fig2] Cold and Warm Starts [3]">
  <figcaption style="text-align: center;">[Fig2] Cold and Warm Starts [3]</figcaption>
</p>
</figure>
<br>

#### Sparsity Detection
다음 그림에서는 MIP (Mixed Integer Programming)과 Lasso, Step regression, Sparsenet의 sparsity를 비교하고 있다. 결과적으로 MIP가 가장 sparse한 결과내고 있음을 알 수 있다.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_05_subset_results3.png" alt="[Fig3] Sparsity Detection (synthetic database) [3]">
  <figcaption style="text-align: center;">[Fig3] Sparsity Detection (synthetic database) [3]</figcaption>
</p>
</figure>
<br>
