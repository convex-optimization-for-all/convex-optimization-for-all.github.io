---
layout: post
title: 08-02-02 Convergence of Stochastic Methods
chapter: "08"
order: "14"
owner: "Kyeongmin Woo"
---

# Convergence of Stochastic Methods

각 함수 $$f_i, i = 1,...,m$$는 컨벡스이고 Lipschitz continuous with constant G 하다고 가정하자.

Stochastic subgradient method에서 fixed step sizes와 diminishing step sizes에 대해 각각 다음의 성질을 가진다.

- **Fixed step sizes** for $$t_k = t$$, $$k = 1, 2, 3, ...$$

>$$\text{Cyclic과 randomized method는 fixed step sizes일 경우 아래를 만족한다:} \\
\begin{align}
\lim_{k→\infty} f(x_{best}^{(k)}) \le f^{*} + 5m^{2}G^{2}t/2
\end{align}
$$

여기서 $$mG$$는 $$\sum_{i=1}^{m} f_i$$의 Lipschitz constant이다.

- **Diminishing step sizes**

>$$\text{Cyclic과 randomized method는 diminishing step sizes일 경우 모두 아래를 만족한다:} \\
\begin{align}
\lim_{k→\infty} f(x_{best}^{(k)}) = f^{*}
\end{align}
$$

