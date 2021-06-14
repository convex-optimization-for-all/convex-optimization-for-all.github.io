---
layout: post
title: 02-05 Separating and supporting hyperplanes
chapter: "02"
order: "11"
owner: "Wontak Ryu"
---

이 절에서는 convex set의 대표적인 특성을 나타내는 두 theorem인 **separating hyperplane theorem**과 **supporting hyperplane theorem**을 살펴볼 것이다.

## Separating hyperplane theorem

서로 교집합을 갖지 않는 disjoint convex set이 여러 개가 있다고 해보자. 이들을 분리하려면 어떻게 하면 좋을까? 가장 간단한 방법은 convex set 사이에 직선을 그어보는 것이다. 실제 이 방법은 classification에서 가장 많이 그리고 기본적으로 사용하는 방법이다. 그리고, 이 방법을 지지하는 이론이 바로 **separating hyperplane theorem**이다. 

만일, 두 개의 disjoint convex set $$C$$와 $$D$$가 있다고 해보자. 그러면, $$x \in C$$일 때  $$a^T x \le b$$이고 $$x \in D$$일 때  $$a^T x \ge b$$인 $$a \ne 0$$와 $$b$$가 존재하게 된다. 다시 말하면, affine function $$a^T x -  b$$는 $$C$$에서는 nonpositive이고 $$D$$에서는 nonnegative이다. 이때, hyperplane $$ \{ x \mid a^T x =  b\}$$를 $$C$$와 $$D$$에 대한 **separating hyperplane**이라고 한다.

다음 그림은 disjoint convex set인 $$C$$와 $$D$$를 나누는 separating hyperplane을 보여주고 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_01_Seperating_hyperplan_theorem.png" alt="[Fig1] Separating hyperplane theorem [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Separating hyperplane theorem [1]</figcaption>
</p>
</figure>


Separating hyperplane theorems의 역은 성립하지 않는다. 즉, separating hyperplane이 존재한다고 해서 두 convex set이 (교집합이 없는) disjoint convex set은 아닐 수 있다. 가장 간단한 반례로 두 convex set이 $$C = D = $$ {$$0$$} $$\subseteq R$$와 같이 같더라도 $$x = 0$$은 $$C$$와 $$D$$를 분리한다는 것을 알 수 있다.

#### Strict separation

만일 separating hyperplane이 더 강한 조건인 $$x \in C$$일 때  $$a^T x \lt b$$이고 $$x \in D$$일 때  $$a^T x \gt b$$를 만족한다면, 이를 $$C$$와 $$D$$에 대한 **strict separation**이라고 한다. Disjoint closed convex set이 strict serparaton일 필요는 없지만 많은 경우에 이 조건은 성립될 수 있다.


## Supporting hyperplanes theorem

**Supporting hyperplane theorem**은 임의의 nonempty convex set $$C$$와 $$x_0 \in$$ **bd** $$C$$가 있을 때, 점 $$x_0$$에서 $$C$$의 **supporting hyperplane**이 존재하는 것을 말한다. 

그렇다면 supporting hyperplane이란 무엇인가? 먼저 점 $$x_0$$가 boundary **bd** $$C$$의 점이라고 하자. 집합 내의 모든 점 $$x \in C$$에 대해  $$a^T x \le a^T x_0$$ ($$a \ne 0$$)을 만족하면, hyperplane $$\{x \mid a^T x = a^T x_0 \}$$은 점 $$x_0$$에서 집합 $$C$$의 **supporting hyperplane**이라고 한다. 

[참고] boundary는 $$x_0 \in$$ **bd** $$C = $$ **cl** $$C$$ $$\setminus$$ **int** $$C$$와 같이 전체 set에서 interior를 빼서 정의할 수 있다.

기하학적으로 supporting hyperplane $$\{x \mid a^T x = a^T x_0\}$$은 점 $$x_0$$에서 접선으로 공간에서 집합 $$C$$를 분리하며, halfspace $$a^T x \le a^T x_0$$는 집합 $$C$$를 포함한다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_02_Supporting_hyperplane_theorem.png" alt="[Fig 2] Supporting hyperplane [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 2] Supporting hyperplane [1]</figcaption>
</p>
</figure>


