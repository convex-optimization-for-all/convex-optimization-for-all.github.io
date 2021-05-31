---
layout: post
title: "25-01-01 Convexification"
chapter: "25"
order: "03"
owner: "YoungJae Choung"
---

Integer program을 동일한 convex problem으로 변환하는 것을 convexification이라고 한다. Convexification을 하게 되면 feasible set이 polyhedron 형태가 되어 cutting plane 알고리즘에서 valid한 cutting plane을 쉽게 찾을 수 있다.

## Convexification
Integer program을 convexification하려면 objective function이 linear해야 한다. 이때, Integer program의 constraint는 convex set인 $$C$$와 integer set인 $${x_j}$$로 구성된다.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

이때, feasible set은 convex hull $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$로 재정의할 수 있다. 이 convex hull $$S$$로 정의된 feasible set을 이용해 원래 문제와 동일한 convex problem을 다음과 같이 정의할 수 있다. 그리고, 이러한 과정을 convexification이라고 한다. 

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in S \\
> \end{align}
> $$

아래 그림을 보면 파란색 영역이 $$C$$이고 빨간색 점들이 $${x_j}$$이며, 이 두 집합으로 구성된 convex hull $$S$$는 빨간색 영역이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/23719/09.01_01_cutting_plane_concept.PNG" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>
출처: https://commons.wikimedia.org/wiki/File:Cutting_plane_algorithm2.png <br><br>

이 두 식이 동일한 이유는 objective function이 linear하기 때문이다. 

## Special case: integer linear programs
위의 convexification 과정을 다음과 같은 integer linear program에 적용해보자.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  Ax \le b \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

Integer linear program에서 convex hull $$S$$는 다음과 같이 정의된다.

> **Theorem** : 만일 $$A, b$$가 유리수라면 다음 집합은 polygon이다.
$$S := \text{conv} \left \{ x : Ax \le b,  x_j \in \mathbb{Z}, j \in J \right \}$$

그렇다면 integer linear program은 linear program일까? 물론 그렇다. 하지만, 이때 polyhedron $$S$$의 형태는 부등식이 기하급수적으로 많은 매우 많은 복잡한 다각형이 될 수 있다. 따라서, 일반적으로 linear program을 풀기 위한 방법과는 다른 방법으로 문제를 풀어야 한다.
