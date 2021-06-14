---
layout: post
title: 08-01-08 Projected Subgradient Method
chapter: "08"
order: 10
owner: "Kyeongmin Woo"
---

[앞서 본 예제]({%post_url contents/chapter08/20-03-29-08_01_07_example_intersection_of_sets %})의 방법을 projected subgradient method라고 한다. 이 알고리즘은 제약조건이 있는 convex problem에서 이용할 수 있다.  

제약 조건을 만족하는 domain을 집합 $$C$$라고 할 때, 제약조건이 있는 컨벡스 문제는 다음과 같이 정의된다.

>
$$ \begin{align}
\min_x \text{ }f(x) \quad \text{subject to } x \in C
\end{align} $$

Projected subgradient method를 사용하면 위와 같은 문제를 비교적 쉽게 풀 수 있다. Projected subgradient method는 일반적인 subgradient method과 동일하지만 각 시행 마다 집합 $$C$$로 결과 값을 projection 해주는 형태이다. 

>
$$ \begin{align}
x^{(k)} = P_c(x^{(k-1)} - t_k ⋅ g^{(k-1)}), \quad k = 1,2,3,...
\end{align} $$

만약 projection이 가능하다면 이 방법은 subgradient method와 동일한 수렴성과 수렴도를 가진다. 

Projected subgradient method에서 주의할 점은 $$C$$가 단순한 형태의 컨벡스 집합 일지라도 $$P_c$$ 연산이 어려우면 전체 문제 또한 풀기 어려워진다는 것이다. 일반적으로 다음과 같은 집합 $$C$$은 비교적 쉽게 projection할 수 있다:

- Affine images: {$$Ax=b : x \in R^{n}$$} 
 
- Solution set of linear system: {$$x: Ax=b$$}

- Nonnegative orthat: $$R_+^{n} =  $${$$x: x\ge 0$$} 

- Some norm balls: {$$x: \lVert x \lVert _p \le 1 $$} for $$p=1,2,\infty$$

- Some simple polyhedra and simple cones 
