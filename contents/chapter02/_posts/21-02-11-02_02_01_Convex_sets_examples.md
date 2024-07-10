---
layout: post
title: 02-02-01 Convex set examples
chapter: "02"
order: 7
owner: "Wontak Ryu"
---

Convex set에는 point, line과 같이 trivial한 것부터 hyperplane, halfspace, ball, ellipsoid, polyhedra, cone 형태의 다양한 set들이 있다.

## Hyperplanes

Hyperplane은 $$n$$차원의 공간을 반으로 가르는 $$n-1$$차원의 subset으로 다음과 같이 정의된다. 여기서, $$a$$는 hyperplane의 normal vector이고 $$b$$는 원점에서 offset이다. Hyperplane은 convex set이자 affine set이다.

>{$$x : a^T x = b$$} with $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

다음 그림에 hyperplane이 있다. 이 hyperplane에 속하는 임의의 x에 대해서 $$(x - x_0)$$와 $$a$$는 직교(orthogonal)한다. 따라서, $$a^T (x - x_0) = 0$$이므로  $$a^T x =  b$$라면 $$b$$는 $$a^Tx_0$$이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.05_Hyperplane.png" alt="[Fig1] Hyperplane [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Hyperplane [1]</figcaption>
</p>
</figure>

## Halfspaces

Halfspace는 hyperplane을 포함한 나머지 한쪽 space를 말한다. 따라서, 하나의 hyperplane $$a^T x = b$$은 두 개의 halfspace를 정의한다. Halfspace는 convex set이지만 affine set은 아니다.

>{$$x : a^T x \le b$$} or {$$x : a^T x \ge b$$}  with $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

Hyperplane $$a^T x = b$$일 때 halfspace $$a^T x \ge b$$는 normal vector $$a$$의 방향이 되며, halfspace $$a^T x \le b$$는 $$-a$$의 방향이 된다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.06_Halfspace.png" alt="[Fig2] Halfspace [1]" width="70%">
  <figcaption style="text-align: center;">[Fig2] Halfspace [1]</figcaption>
</p>
</figure>

참고로, $$\{x : a^T x \le b\}$$의 interior인  $$\{x : a^T x \lt b\}$$를 open halfspace라고 한다.

## Euclidean balls

Euclidean ball은 또다른 convex set으로 다음과 같이 정의된다. ($$\| . \|_2$$은 euclidean norm으로 $$\|u\|_2 = (u^T u)^\frac{1}{2}$$이다.) $$x_c$$는 중심이고 $$r$$은 반지름이다. 따라서, $$B(x_c, r)$$은 중심 $$x_c$$에서 반경 $$r$$ 이내의 모든 점들을 포함한다.

>$$B(x_c, r) = \{ x \phantom{1} \mid \phantom{1} \|x - x_c \|_2 \le r \} = \{ x \phantom{1} \mid \phantom{1} (x - x_c)^T (x - x_c) \le r^2 \} \text{ with } \ r \ge 0$$


Euclidean ball을 다르게 표현하면 다음과 같다.

>$$B(x_c, r) = \{ x_c + ru \text{ } \mid \text{ } \| u \|_2 \le 1 \} $$ 

## Ellipsoids

Euclidean ball과 관련된 convex set으로 ellipsoid가 있으며 다음과 같이 정의된다. 

>$$\mathcal{E} = \{x \text{ } \mid \text{ } (x - x_c)^T P^{-1} (x - x_c) \le 1 \} $$ 

여기서 $$P = P^T \succ 0$$로 $$P$$는 symmetric이고 positive definite이다. 벡터 $$x_c \in C$$는 ellipsoid의 중심이며, 행렬 $$P$$는 ellipsoid가 중심 $$x_c$$에서 모든 방향으로 얼마나 멀어지는가를 나타낸다. Ellipsoid의 축은 $$\sqrt{\lambda_i}$$가 되며 $$\lambda_i$$는 행렬 $$P$$의 eigenvalue를 말한다. 따라서, ball은 $$P = r^2 I$$인 ellipsoid의 특별한 case라고 할 수 있다.


다음 그림은 ellipsoid를 보여주고 있다. 중심 $$x_c$$는 점으로 장축과 단축은 line segment로 그려져 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_Ellipsoid.png" alt="[Fig3] Ellipsoid [1]" width="70%">
  <figcaption style="text-align: center;">[Fig3] Ellipsoid [1]</figcaption>
</p>
</figure>

Ellipsoid 식을 다음과 같이  $$x_c$$를 중심으로 $$Au$$ 벡터를 더하는 형태로 표현할 수도 있다.

>$$\mathcal{E} = \{ \ x_c + Au \text{ } \mid \text{ } \|u\|_2 \le 1 \} $$

여기서 $$A$$는 정방 행렬이고 nonsingular이다. 만일 $$A = P^\frac{1}{2}$$라고 하면 위의 식과 동일해져서 symmetric이고 positive definite라고 할 수 있다. 이때, $$A$$가 symmetric positive semidefinite이면  degenerate ellipsoid라고 하며 affine dimension은 $$A$$의 rank와 같다. Degenerate ellipsoid도 역시 convex이다.

## Norm balls

Norm ball이란 $$x_c$$를 중심으로 반경 $$r$$ 이내인 점들의 집합을 말한다. 단, euclidean ball은 euclidean norm으로 정의되는 반면 norm ball은 임의의 norm으로 반경이 정의된다.
$$\|.\|$$을 $$R^n$$의 임의의 norm이라고 할때 norm ball은 다음과 같이 정의된다.

>$$ \{ x \phantom{1} \mid \phantom{1} \|x - x_c \| \le r  \} $$ 

P-norm이 다음과 같이 정의될 때 norm ball의 모양은 다음과 같다.

>$$ \| x  \|_{p} = \left( \sum_{i=0}^n |x_i|^{p} \right)^{1/p} \text{ for  } p \ge 1$$

이 그림은 3D로 $$p$$값에 따라 norm ball의 모양을 보여준다. $$p$$가 1이상이어야 norm ball이 convex set임을 알 수 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_2_norm_ball.png" alt="[Fig4] Norm ball [1]" width="70%">
  <figcaption style="text-align: center;">[Fig4] Norm ball [1]</figcaption>
</p>
</figure>

이 그림은 2D로 p값에 따라 norm ball의 모양을 보여준다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_3_norm_ball2.png" alt="[Fig4] Norm ball [2]" width="70%">
  <figcaption style="text-align: center;">[Fig4] Norm ball [2]</figcaption>
</p>
</figure>


## Polyhedra

Polyhedron은 선형 부등식과 등식의 교집합으로 정의된다. Affine sets (즉, subspaces, hyperplanes, lines), rays, line segments, halfspaces는 모두 polyhedron이다. Polyhedra는 convex set이며 bounded polyhedron를 polytope이라고 부르기도 한다. 

>$$\mathcal{P} = \{ x \mid a^T_i x \le b_i, i = 1, ..., m, c_j^Tx  = d_j, j = 1, ..., p\}$$ 

하나의 등식 $$c_j^Tx  = d_j$$은 두 개의 부등식 $$c^T_jx \le d_j$$과 $$c^T_jx \ge d_j$$을 정의한다. 따라서, 등식 표현은 편의상 추가된 것으로 부등식만으로도  polyhedron을 정의할 수 있다.

다음 그림은 다섯 개 halfspace의 교집합으로 만들어진 오각형 polyhedron이다. 이  polyhedron은 outward normal vectors $$a1, . . . ., a5$$를 갖는다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.09_Polyhedra.png" alt="[Fig5] Polyhedra [1]" width="70%">
  <figcaption style="text-align: center;">[Fig5] Polyhedra [1]</figcaption>
</p>
</figure>

행렬 표현으로 간단히 다음과 같이 정의하기도 한다.

>$$\mathcal{P} =  \{ x \mid A^Tx \preceq b, C^Tx  = d \}$$
where
$$
A = 
\begin{bmatrix}
a^T_1 \\\
\vdots \\\
a^T_m
\end{bmatrix}, 
$$
$$
C = 
\begin{bmatrix}
c^T_1 \\\
\vdots \\\
c^T_p
\end{bmatrix}
$$

#### Simplexes

Simplex는 $$n$$차원 공간에서 만들 수 있는 가장 간단한 다각형으로 $$n+1$$개의 점으로 만들어진다.

만일 $$k + 1$$개의 점 $$v_0, ... , v_k \in R^n$$가 있고 이들이 affinely independent하다면 simplex는 이 $$k+1$$개 점들의 convex hull로 정의된다. 참고로, affinely independent는 $$v_1 − v_0, ... , v_k − v_0$$가 linearly independent하다는 의미이다.

>$$C = \mathbb{conv} \{v_0, ... , v_k\} = \{ \theta_0 v_0 + \cdots + \theta_k v_k  \mid \theta \succeq 0, 1^T \theta = 1 \}$$

다음 그림은 0차원에서 3차원까지의 simplex를 보여주고 있다. 0차원에서는 점, 1차원에서는 선분, 2차원에서는 삼각형, 3차원에서는 사면체가 해당 차원의 simplex이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.02_10_Simplex.png" alt="[Fig6] Simplex [source - wikipedia]" width="70%">
  <figcaption style="text-align: center;">[Fig6] Simplex [source - wikipedia]</figcaption>
</p>
</figure>

대표적인 simplex의 종류에는 probability simplex가 있다.

>$$C = \mathbb{conv} \{e_1, ..., e_n \} = \{ \theta \mid \theta \succeq 0, 1^T \theta = 1\}$$
