---
layout: post
title: 02-04 Generalized inequalities
chapter: "02"
order: 10
owner: "Wontak Ryu"
---

1차원 실수 공간 $$R$$에서는 두 개의 숫자 1과 2가 있을 때 1보다 2가 크다고 말할 수 있다. 그러면, n차원 실수 공간 $$R^n$$에서 두 점 $$x_1$$과 $$x_2$$가 있을 때 두 점 중 어떤 점이 더 크다고 말할 수 있을까? 그렇다고 말하기는 어렵다. 

이 절에서는 n차원 실수 공간 $$R^n$$에서 두 점의 순서를 비교하기 위한 **generalized inequality**를 살펴보고, set의 minimum과 minimal도 함께 살펴볼 것이다.

## Proper cone

Convex cone $$K \subseteq R^n$$가 다음 성질을 만족하면 **proper cone**이라고 한다.

* K is closed. (boundary를 포함한다.)
* K is solid. (interior가 empty가 아니다.)
* K is pointed. (직선을 포함하지 않는다.) (또는  $$x \in K, − x \in K \implies x = 0$$)

$$n$$차원 공간에서 pointed & closed convex cone이 $$n-1$$차원 이하의 subspace에서 정의된다면 interior가 비게 된다. 왜냐하면, $$n-1$$차원 이하의 cone은 $$n$$ 차원의 open ball을 포함하지 못하기 때문에 interior가 정의되지 않는다. 따라서, cone은 solid하지 않게 되고 proper cone이 될 수 없다. 예를 들어, $$R^3$$에 정의된 2차원 파이 모양의 pointed & closed convex cone은 proper cone이 아니다.

Interior의 정의는 *[Wikipedia 정의](https://en.wikipedia.org/wiki/Interior_(topology))*를 참고하라.


## Generalized inequality

Proper cone을 이용하면$$R^n$$의 partial ordering인 **generalized inequality**를 다음과 같이 정의할 수 있다.  Generalized inequality는 $$R$$의 standard ordering과 비슷한 속성을 갖는다.

>$$x \preceq_{K} y \iff y − x \in K$$

비슷하게 strict partial ordering을 다음과 같이 정의할 수 있다.

>$$x \prec_{K} y \iff y − x \in $$ **int** $$K$$

만일 $$K = R_{+}$$이라면 $$\preceq_{K}$$는 $$R$$에서의 일반적인 $$\le$$과 같다.

#### Properties of generalized inequalities

Generalized inequality $$\preceq_{K}$$는 다음과 같은 속성을 만족한다.


* $$\preceq_{K}$$ is **preserved under addition**: if $$x \preceq_{K} y$$ and $$u \preceq_{K} v$$, then $$ x+u \preceq_{K} y +v$$.
* $$\preceq_{K}$$ is **transitive**: if $$x \preceq_{K} y$$ and $$y \preceq_{K} z$$ then $$x \preceq_{K}  z$$.
* $$\preceq_{K}$$ is **preserved under nonnegative scaling**: if $$x \preceq_{K} y$$ and $$α ≥ 0$$ then $$αx \preceq_{K} αy$$.
* $$\preceq_{K}$$ is **reflexive**: $$x \preceq_{K} x$$.
* $$\preceq_{K}$$ is **antisymmetric**: if $$x \preceq_{K} y$$ and $$y \preceq_{K} x$$, then $$x = y$$.
* $$\preceq_{K}$$ is **preserved under limits**: if $$x_i \preceq_{K}  y_i$$ for $$i = 1, 2, . . ., x_i \to x$$ and $$y_i \to y$$ as $$i \to ∞$$, then $$x \preceq_{K} y$$.

Strict generalized inequality 위의 속성에 대응하는 속성을 갖는다.

## Minimum and minimal elements

$$R$$의 ordering과 $$R^n$$의 generalized ordering의 가장 큰 차이는 **linear ordering**이다. $$R$$에서는  $$x \lt y$$ 또는 $$x \gt y$$와 같이 두 점을 비교할 수 있지만  generalized inequality는 그렇지 못하다. 따라서, generalized inequality 문맥으로 maximum과 minimum 개념을 정의하는 것이 훨씬 더 복잡할 것으로 예상해 볼 수 있다.

#### Minimum elements

$$x \in S$$이 모든 $$y \in S$$에 대해 $$x \preceq_{K} y$$이면 $$x$$는 집합 $$S$$의 **minimum** element이다. 비슷한 방식으로  **maximum**도 정의할 수 있다. 어떤 집합에서 minimum이 존재한다면 unique하다. 즉, minimum은 오직 하나만 존재한다. 

어떤 점 $$x \in S$$가 $$S$$의 minimum이라면 $$S \subseteq x + K$$이다. 여기서 $$x + K$$의 의미는 ($$\preceq_{K}$$에 따라) 모든 점들은 $$x$$와 비교할 수 있으며 $$x$$와 같거나 크다는 의미이다.

#### Minimal elements

비슷한 개념으로 **minimal**이 있다. $$x \in S$$이 모든 $$y \in S$$에 대해 $$y \preceq_{K} x$$인 경우는 $$y=x$$인 경우뿐이라면 $$x$$는 집합 $$S$$의 **minimal** element이다. 비슷한 방식으로  **maximal**도 정의할 수 있다. 집합은 여러 개의 minimal element를 가질 수 있다.

어떤 점 $$x \in S$$가 $$S$$의 minimal이라면 $$(x - K) \cap S = $$ {$$x$$}이다. 여기서 $$x - K$$의 의미는 ($$\preceq_{K}$$에 따라) 모든 점들은 $$x$$와 비교할 수 있으며 $$x$$와 작거나 같다는 의미이다.

$$K = R_{+}$$의 경우 minimal과 minimum은 동일하며 일반적인 minimum의 정의에 부합한다.

#### $$R^2_{+}$$ cone에서 minimum과 minimal

$$R^2_{+}$$ cone $$K$$를 고려해 보자. Inequality $$x \preceq_{K} y$$는 y가 x보다 오른쪽 위에 있다는 의미이다.  $$x \in S$$일 때 $$x$$가 minimum이란 이야기는 $$S$$의 모든 점이 $$x$$보다 오른쪽 위에 있다는 의미이다. $$x$$가 minimal이란 이야기는 $$S$$에는 $$x$$의 왼쪽 아래에 있는 점이 없다는 의미이다.

아래 그림에서 $$S_1$$은 minimum $$x_1$$을 갖는다. 집합 $$x + K$$은 옅은 회색으로 표시되어 있으며 집합 $$S_1$$은 $$S_1 \subseteq x + K$$이기 때문에 $$x_1$$은  minimum이다. $$S_2$$은 minimal $$x_2$$을 갖는다. 집합 $$x - K$$은 옅은 회색으로 표시되어 있으며 집합 $$S_2$$은 $$(x - K) \cap S = $$ {$$x$$}이기 때문에  $$x_2$$는 minimal이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_01_Minimum_and_minimal.png" alt="[Fig1] Minimum and minimal elements [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Minimum and minimal elements [1]</figcaption>
</p>
</figure>


