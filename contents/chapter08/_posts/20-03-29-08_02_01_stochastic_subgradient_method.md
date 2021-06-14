---
layout: post
title: 08-02-01 Stochastic Subgradient Method
chapter: "08"
order: "12"
owner: "Kyeongmin Woo"
---

다음과 같이 함수의 합을 최소화하는 문제를 고려해보자.

>$$
\begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation}
$$

이 문제에 subgradient method를 적용하면 각 함수 $$f_i$$에 대해 subgradient를 구해서 합산을 해야 한다. ([stochastic gradient descent]({%post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %})에서 도출한 방법과 동일)

정리하면 stochastic subgradient method는 다음과 같은 형태를 가진다. 

>$$
\begin{align}
x^{(k)} = x^{(k-1)} - t_k ⋅ g_{i_k}^{(k-1)}, \quad k = 1, 2, 3, . . . 
\end{align}
$$

여기서 $$i_k \in {1,...,m}$$는 $$k$$번째 시행에서 선택된 하나의 인덱스 값이며, 이는 뒷장에서 stochastic subgradient method의 convergence rate에서 살펴볼  cyclic method 또는 random method에 따라 다르게 결정된다. $$g_{i}^{(k-1)} \in \partial f_{i}(x^{k-1}) $$이며 이 업데이트 방향은 모든 데이터를 사용하는 일반적인 [subgradient method]({%post_url contents/chapter08/20-03-29-08_01_subgradient_method %}) (batch subgradient method 또는 full batch subgradient method라고 부름)에서의 $$\sum_{i=1}^{m} g_i^{(k-1)}$$를 대체한다.

만약 각 $$f_i, i = 1,...,m$$이 모두 미분 가능하다면 이 알고리즘은 stochastic gradient descent이 된다. (stochastic subgradient method가 좀 더 일반적인 형태)