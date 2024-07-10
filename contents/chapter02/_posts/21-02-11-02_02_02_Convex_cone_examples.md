---
layout: post
title: 02-02-02 Convex Cone examples
chapter: "02"
order: 8
owner: "Wontak Ryu"
---


다음은 convex cone의 예로는 norm cone, normal cone, positive semidefinite cone 등이 있다.

## Norm cone

**Norm cone**은 반경 $$t$$ 이내인 점들로 이뤄진 cone으로 $$(x,t)$$로 정의되는 $$R^{n+1}$$차원의 convex cone이다. 이때, 반경은  임의의 norm으로 정의된다.

>$$C = \{(x, t) : \| x \| \le t\} \subseteq \mathbb{R}^{n+1}$$, for a norm $$\|·\|$$ 

아래 그림에는 $$l_2$$ norm $$\|  · \|_2$$에 대한 norm cone이 그려져 있다. 이를 second-order cone 또는 ice cream cone이라고도 부른다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.08_Norm_Cone.png" alt="[Fig1] Norm Cone [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Norm Cone [1]</figcaption>
</p>
</figure>

## Normal Cone

집합 $$C$$에 대해서 $$x \in C$$일 때, 다음 식을 만족하면 **normal cone**이라고 한다.
Normal cone은 $$C$$에 상관 없이 항상 convex cone이다.


>$$N_C(x) = \{ g: g^T (y - x) \le 0, \text{ for all } y \in C \}$$

Normal cone은 집합 $$C$$에 속하는 임의의 점 $$x$$와 집합 $$C$$의 모든 점 $$y$$와이 차 벡터인 $$y-x$$와 내적이 항상 0보다 작은 벡터인 $$g$$로 정의되는 cone을 말한다. 벡터 $$g$$와 $$y-x$$의 내적이 0보다 작다는 의미는 두 벡터의 각도가 (즉, $$cos\theta$$가 음수인 구간인) $$ 90 \le \theta \le 270$$이란 것을 의미한다. 

* $$x$$가 boundary에 포함된 점일 경우 모든 $$y-x$$ 벡터와의 각도가 $$ 90 \le \theta \le 270$$인 벡터 $$g$$는 supporting hyperplane의 normal뿐이다. 
* $$x$$가 꼭지점일 경우 supporting hyperplane이 여러개 존재하기 때문에 벡터 $$g$$는 파이 모양이 된다. 
* $$x$$가 non-boundary 영역의 점일 경우 $$g$$는 영벡터뿐이다. 

다음 그림에 normal vector이 그려져 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.04_2_Normal_Cone.png" alt="[Fig2] Normal Cone [3]" width="70%">
  <figcaption style="text-align: center;">[Fig2] Normal Cone [3]</figcaption>
</p>
</figure>


## Positive semidefinite cone

**Positive semidefinite** $$\mathbb{S}^n_+$$의 정의는 다음과 같다. 이때 $$\mathbb{S}^n$$는  $$n × n$$ symmetric matrix이다.
>$$\mathbb{S}^n_+ =$$ { $$ X \in \mathbb{S}^n : X \succeq 0 $$} 

$$\mathbb{S}^n_+$$는  $$\theta_1, \theta_2 \ge 0$$, $$A, B \in  \mathbb{S}^n_+$$이면 $$\theta_1 A + \theta_2 B \in  \mathbb{S}^n_+$$를 만족하기 때문에 convex cone이며 **positive semidefinite cone**이라고 부른다.

다음 그림은 $$S^2_+$$에서의 positive semidefinite cone의 boundary를 $$ (x, y, z) \in R^3$$ 상에서 그린 그림이다. 행렬 $$X$$는 positive semidefinite이기 때문에 determinant가 0이상 이어야 한다.

$$
X = 
\begin{bmatrix}
x, y \\\
y, z
\end{bmatrix}
\in \mathbb{S}^2_+ \iff x \ge 0, z \ge 0, xz \ge y^2$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.10_Positive_Semidefinite_Cone.png" alt="[Fig3] Positive semidefinite cone [1]" width="70%">
  <figcaption style="text-align: center;">[Fig3] Positive semidefinite cone [1]</figcaption>
</p>
</figure>


