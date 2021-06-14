---
layout: post
title: 09-05-02 Convergence analysis
chapter: "09"
order: 8
owner: "Kyeongmin Woo"
---

# Convergence analysis

이 절에서는 accelerated proximal gradient method의 수렴을 분석한다.

## Convergence analysis
Objective 함수 $$f(x) = g(x) + h(x)$$에 대해 다음 사항을 가정한다.

* $$g$$는 convex, differentiable하며 **dom**$$(g) = \mathbb{R}^n$$, $$\nabla g$$는 Lipschitz continuous하다 ($$L \gt 0$$).
* $$h$$는 convex이고 $$\text{prox}_{t}(x) = \underset{z}{\text{argmin}} \left \{ \parallel x - z \parallel_2^2/ (2t) + h(z) \right \}$$가 계산되어야 한다.

#### Convergence Theorem
> **Accelerated proximal gradient method**는 fixed step size $$t \le 1/L$$에 대해 다음 식을 만족한다. 
>\begin{align}
f(x^{(k)}) − f^{\star} ≤ \frac{2 \lVert x(0) −x^{\star} \rVert_2^2 }{ t(k + 1)^2}
\end{align}

Frst-order method의 optimal rate인 $$O (1 / k^2)$$의 성능을 가지며 이는 $$O(1/ \sqrt {\epsilon})$$이다.  Subgradient method의 성능은 $$O(1/\varepsilon^{2})$$, proximal gradiant의 성능은 $$O(1/\varepsilon)$$, accelerated proximal gradient의 성능은 $$O(1/\sqrt{ \varepsilon})$$이다.

## Backtracking line search
가속(acceleration)을 사용할 때 Backtracking line search를 하는 복잡한 방법들도 있지만, 여기에서 좀 더 간단한 방법을 알아보자.
 
먼저 $$β <1, t_0 = 1$$로 고정한다. 그리고, $$k$$번째 반복에서 $$t = t_{k-1}$$로 시작을 한다. (Gradient descent에서는 $$t=1$$로 시작을 하는데 accelerated proximal gradient method에서는 이전 단계의 step size부터 시작한다는 점을 유의하라.) 

> $$g(x^+) > g(v) +\nabla g(v)^T(x^+ − v) + \frac{1}{2t} \lVert x+ −v \rVert_2^2$$

그리고 위 수식을 만족하는 동안 $$t = βt$$를 줄이고, $$x^+ = \text{prox}_t (v − t \nabla g(v))$$를 갱신한다. 그 외에는 $$x^+$$를 유지한다.

#### Convergence Theorem
동일한 가정 하에서 같은 성능을 얻을 수 있다.

>**Accelerated proximal gradient method**는 backtracking line search에 대해 다음 식을 만족한다. Step size는 $$t_{\text{min}} = \text{min} \{1,\beta/L \}$$이다.

>$$ \begin{align}
f(x^{(k)})−f^{\star} ≤ \frac{2 \lVert x(0) −x^{\star} \rVert_2^2 }{ t_{min} (k + 1)^2}, \space t_{\text{min}} = \text{min} \{1,β/L \} \\
\end{align}
$$