---
layout: post
title: 02-03 Operations that preserve convexity
chapter: "02"
order: 8
owner: "Wontak Ryu"
---

이 절에서는 convex set의 convexity를 유지하는 연산에 대해 살펴본다. 집합의 convexity를 판별하거나 hyperplanes, halfspaces, norm balls과 같은 간단한 convex set으로 원하는 convex set을 만들 때 이런 연산들이 유용하다.

Convexity를 유지하는 연산에는 다음과 같은 것들이 있다.

* Intersection
* Affine functions
* Perspective function
* Linear-fractional functions

## Intersection

Convex set의 교집합은 convex이다. 즉, $$S_1$$과 $$S_2$$이 convex라면 $$S_1 \cap S_2$$은
convex이다. 집합이 무한히 존재할 때에도 이와 같은 성질은 유지된다. (참고로 subspaces, affine sets, convex cones도 교집합 연산에 닫혀있다.)

Set의 convexity는 무한한 halfspace의 교집합으로 표현할 수 있으며 그 반대도 성립한다. 
즉, closed convex set $$S$$는 $$S$$를 포함하는 모든 halfspace의 교집합으로 다음과 같이 정의할 수 있다.

>$$S = \bigcap \{\mathcal{H} \mid \mathcal{H} \text{ halfspace }, S \subseteq \mathcal{H}\}$$

## Affine functions

$$A \in R^{m \times n}$$이고 $$b \in R^{m}$$일 때, $$f : R^n \to R^m$$인 $$f(x) = Ax + b$$을 affine function이라고 한다.

이때, $$C \subseteq R^n$$가 convex이고 $$D \subseteq R^m$$가 convex이면

* affine image인 $$f(C) = \{f(x) \mid x \in C\}$$는 convex이다.
* affine preimage인 $$f^{-1}(D) = \{x \mid f(x) \in D\}$$는 convex이다.

Affine function인 **scaling and translation**, **projection**, **sum of two sets**, **partial sum of set**과 같은 연산을 convex set에 적용하면 결과는 convex set이다.

Linear matrix inequality의 해집합 $$\{x \mid x_1 A_1 + \cdots + x_m A_m \preceq B\} (\text{ with } A_i, B \in S^n)$$도 convex이다. 

Hyperbolic cone $$\{x \mid x^T P x \lt (c^T x)^2, c^T x \gt 0\}$$ (with $$P \subseteq S^n_+$$, $$c \in R^n$$)도 convex이다. 

## Perspective function

**Perspective function**은 카메라에 상이 맺히는 것과 같이 멀리 있는 물체는 작게 가까이 있는 물체는 크게 원근에 따라 상을 만드는 함수이다. 따라서, 피사체는 $$R^{n+1}$$차원의 공간에 있고 상은 $$R^n$$ 차원의 평면에 맺히게 된다.

Perspective function을 수식으로 정의하면 $$P : R^{n+1} \rightarrow R^{n}$$로서 **dom** $$P = R^{n} \times R_{++}$$이고 $$P(z,t) = z/t$$와 같다. (여기서 $$R_{++} = \{x \in R \mid x \gt 0\}$$이다.) 함수를 해석해 보면 벡터의 마지막 요소가 1이 되도록 정규화를 하며, 마지막 요소를 제거해서 차원을 $$R^{n+1}$$에서 $$R^n$$로 줄인다. Perspective function은 $$C \subseteq$$ **dom** $$P$$가 convex라면 image $$P(C) = \{P(x) \mid x \in C\}$$도 convex가 만든다.

Perspective function은 pin-hole 카메라가 작동하는 원리와 같다. 멀리 있는 피사체가 pin-hole을 통과하게 되면 pine-hole과 피사체와의 거리에 비례해서 크기가 축소되기 때문이다. 다음 그림에 이런 원리가 그려져 있는데 직관적으로 동일한 captured ray 안에 피사체가 존재하면 상도 동일하게 맺힐 것이라는 것을 알 수 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/17372/02.03_03_pine_hole.png" alt="[Fig 1] pin-hole 카메라 작동 원리" width="70%">
  <figcaption style="text-align: center;">[Fig 1] pin-hole 카메라 작동 원리</figcaption>
</p>
</figure>


아래 그림에서 피사체의 한 점이 좌표 $$(x_1, x_2, x_3)$$로 표현된다고 하면, 검정색 가로선은 $$x_3 = 0 \in R^3$$이고 원점을 포함한다. 이때 원점이 pine-hole이 되며 Image plane인 $$x_3 = −1$$에 피사체가 맺힌다. 피사체의 점은 perspective function에 의해 맵핑되어 Image plane에 점 $$-(x_1 / x_3, x_2 / x_3)$$으로 맺히게 된다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/17372/02.03_04_pine_hole_camera_model.png" alt="[Fig 2] pin-hole 카메라의 perspective function [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 2] pin-hole 카메라의 perspective function [1]</figcaption>
</p>
</figure>

## Linear-fractional functions

Linear-fractional function은 perspective function과 affine function으로 구성된다. 

> $$f(x) = (A x + b)/(c^T x + d), \mathbb{dom} f(x) = \{x \mid c^T x + d \gt 0 \} (A \in R^{m \times n}, b \in R^m, c \in  R^n, d \in R)$$

Linear-fractional function에서 $$c = 0$$이고 $$d \gt 0$$이면 affine function이 된다. 따라서, affine function과 linear function은 linear-fractional function의 special case라고 할 수 있다.

기하학적으로 이 함수는 affine function $$A x + b$$를 적용하고  projection function을 다시 적용한 것으로 볼 수 있다. 단, vector의 마지막 항목이 $$c^T x + d$$인 경우이다.

다음 그림은 linear fractional function $$f(x) = \frac{1}{(x_1 + x_2 + 1)} x$$, **dom** $$f(x) = $$ {$$(x_1, x_2) $$ \mid $$x_1 + x_2 + 1 \gt 0$$}의 domain과 image를 보여주고 있다. $$C \subseteq R^2$$일 때 왼쪽 그림은 domain이며, 점선은 domain $$f$$의 boundary이다. 오른쪽 그림은 $$f$$의 image이며 점선은  domain $$f^{-1}$$의  boundary이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/17372/02.03_05_linear_fractional_function.PNG" alt="[Fig 3] Linear-fractional functions [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 3] Linear-fractional functions [1]</figcaption>
</p>
</figure>