---
layout: post
title: 09-02 Convergence analysis
chapter: "09"
order: 3
owner: "Kyeongmin Woo"
---

# Convergence analysis
이 절에서는 proximal gradient descent의 수렴을 분석한다. 

## Convergence Analysis
Objective 함수 $$f(x) = g(x) + h(x)$$에 대해 다음 사항을 가정한다.

* $$g$$는 convex, differentiable하며 **dom**$$(g) = \mathbb{R}^n$$, $$\nabla g$$는 Lipschitz continuous하다 ($$L \gt 0$$).
* $$h$$는 convex이고 $$\text{prox}_{t}(x) = \underset{z} {\text{argmin}} \{ \parallel x - z \parallel_2^2/ (2t) + h(z) \}$$가 계산되어야 한다.

#### Convergence Theorem
> **Proximal gradient descent**는 fixed step size $$t \le 1/L$$에 대해 다음 식을 만족한다. 
>\begin{align}
f(x^{(k)}) - f^{\*} \le  \frac{ \lVert x^{(0)} - x^{\*} \rVert^2\_2 }{2tk}
\end{align}

Proximal gradient descent는 $$O(1/k)$$ 또는 $$O(1/\epsilon)$$의 수렴 속도를 갖는데 이는 gradient descent와 동일한 성능이다. 단, 이 성능은 반복 횟수 기준이지 연산 횟수 기준이 아니라는 점을 유념하자. (연산 횟수는 함수 $$h$$에 따라 적을수도 많을 수도 있다.)

## Backtracking line search
Proximal gradient descent의 backtracking line search 방법은 gradient descent와 비슷하지만 함수 $$f$$가 아닌 smooth 파트인 $$g$$에 대해서만 작동한다. 

먼저 파라미터를 $$0 \lt \beta \lt 1$$로 설정하고 $$t=1$$로 시작한다. 각 반복에서 다음 조건을 만족하는 동안 $$t$$를 $$t = \beta t$$로 줄이고, 다음 조건을 만족하지 않으면  proximal gradient descent를 update한다.
> \begin{align}
g(x - tG_t(x)) \gt g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2
\end{align}

이 backtracking 조건은 다음 step 위치인 $$x - tG_t(x)$$에서의 함수 $$g$$의 값이 함수 $$g$$의 Taylor 2차 근사 함수의 값보다 클 때를 의미한다.

이 식에서 $$G_t(x) = \nabla g(x)$$이라면 $$g(x - t \nabla g(x)) \gt g(x) - \alpha t \lVert \nabla g(x) \rVert_2^2 $$가 되므로 gradient descent의 backtracking 조건과 동일해진다는 것을 알 수 있다. 

**참고 :** Gradient descent의 backtracking에 대한 자세한 내용은 [06-02-02 backtracking line search]({% post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %}) 참조

#### Backtracking line search 알고리즘
이 내용을 알고리즘으로 정리하면 다음과 같다. (단, $$\nabla x = - t G_t(x)$$)

1. 파라미터를 초기화한다. ($$0 \lt \beta \lt 1$$, $$0 \lt \alpha \le 1/2$$)
2. 각 반복에서 $$t = t_{\text{init}}$$로 초기화 한다. ($$t_{\text{init}} = 1$$)
3. 조건 $$g(x - tG_t(x)) \gt g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2 $$을 만족하면 $$t = \beta t$$로 줄인다. 이 조건이 만족되는 동안 3을 반복한다.
4. Gradient descent update $$ x^+ = x - t G_t(x) = \text{prox}_t(x - t \nabla g(x))$$를 실행한다.
5. 종료 조건을 만족하지 않으면 2로 간다.

Proximal gradient descent에서 backtracking을 할 때 $$G_t(x)$$이 반복적으로 계산되기 때문에 실제  $$G_t(x)$$ 안에 포함된 proximal mapping이 반복적으로 계산된다. Proxmal mapping은 계산 비용이 매우 높기 때문에 전체적인 backtracking 계산 비용은 높다고 할 수 있다.

#### Convergence Theorem
앞의 가정과 동일한 가정 하에 backtracking line search 방식도 같은 성능을 구할 수 있다.

>**Proximal gradient descent**는 backtracking line search에 대해 다음 식을 만족한다. Step size는 $$t_{\text{min}} = \text{min} \{1,\beta /L \}$$이다.

> $$
f(x^{(k)})−f^{\star} ≤ \frac{\lVert x^{(0)} − x^{\star} \rVert_{2}^{2}}{2 t_{min}k}, \space t_{\text{min}} = \text{min} \{ 1, \beta / L \} \\
$$
