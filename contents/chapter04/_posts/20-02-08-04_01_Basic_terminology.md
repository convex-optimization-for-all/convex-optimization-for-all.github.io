---
layout: post
title: 04-01 Basic terminology
chapter: "04"
order: 2
owner: "YoungJae Choung"
---
## Convex Optimization Basic

Convex optimization 문제에서 사용되는 기본적인 용어들을 살펴보자. <br>
일단 convex optimization 문제는 다음과 같이 정의된다.

>$$
\begin{aligned}
&\text{minimize}_{x \in D} &&{f(x)} \\
&\text{subject to} &&{g_{i}(x) \leq 0, \,\,\,\,\, i = 1, \dotsc, m} \\
&&&{h_{j}(x) = 0, \,\,\, j = 1, \dotsc, r},\\\\
\end{aligned}
$$

>where $$f$$ and $$g_{i}$$, $$\, \, i=1,\dotsc, m$$ are all convex,
>$$h_j, \, \, j = 1, \dotsc, r$$ are all affine,
>and the optimization domain is $$D = dom(f) \cap \bigcap_{i=1}^{m} dom(g_{i}) \cap  \bigcap_{j=1}^r dom(h_{j})$$.


* $$f$$는 **criterion** 또는 **objective function**이라 부른다.  
* $$g_{i}(x)$$는 **inequality constraint function**이라고 한다. 
* $$h_{j}(x)$$는 **equality constraint function**이라고 한다. 
* 만약 $$x \in D$$이고,
  $${g_{i}(x) \leq 0, \, i = 1, \dotsc, m} \, $$와
  $${h_{j}(x) = 0, j = 1, \dotsc, r}$$를 만족하면 $$x$$는 **feasible point**다.
* 모든 feasible point $$x$$에 대해  $$f(x)$$의 최솟값을 **optimal value**라 부르고, $$f^{\star}$$으로 쓴다.
* $$x$$가 feasible하고 $$f(x) = f^{\star}$$일때, $$x$$는 **optimal**, **solution**, 또는 **minimizer**라 부른다.
* $$x$$가 feasible하고 $$f(x) \le f^{\star} + \epsilon$$일때, $$x$$는 **$$\epsilon$$-suboptimal**이라 부른다.
* $$x$$가 feasible하고 $$g_i(x) = 0$$일때, $$g_i$$는 $$x$$에서 **active**하다고 한다.
* Convex minimization 문제는 concave maximization 문제로 변환할 수 있다.

>$$
\begin{aligned}
&\text{maximize}_{x \in D} \, \, \, &&-f(x)\\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&h_{j}(x) = 0, j = 1, \dotsc, r,\\\\
\end{aligned}
$$

>where $$f$$ and $$g_{i}$$, $$\, \, i=1,\dotsc, m$$ are all convex,
>$$h_j, \, \, j = 1, \dotsc, r$$ are all affine,
>and the optimization domain is $$D = dom(f) \cap \bigcap_{i=1}^{m} dom(g_{i}) \cap  \bigcap_{j=1}^r dom(h_{j})$$.
