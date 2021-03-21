---
layout: post
title: 06-03-03 Convergence analysis for backtracking
chapter: "06"
order: 9
owner: "Kyeongmin Woo"
---

# Convergence analysis for backtracking

$$f$$는 convex이고 differentiable하며 **dom** $$f = \mathbb{R}^n$$일 때 다음 식을 만족한다고 하자.

>$$ \lVert \nabla f(x) - \nabla f(y) \rVert\_2 \le L \lVert x - y \rVert\_2$$  for any $$x, y$$ and $$L \gt 0$$

$$\nabla f$$는 Lipschitz constant $$L$$에 대해  Lipschitz continuous하다고 말할 수 있다. 
[[(Wikipedia) Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]
## Convergence Theorem
>**Gradient descent**는 backtracking line search에 대해 다음 식을 만족한다. Step size는 $$t_{\text{min}} = \text{min}\\{1,β/L\\}$$이다.
> \begin{align}
f(x^{(k)})−f^{\star} ≤ \frac{\lVert x^{(0)} − x^{\star} \rVert_{2}^{2}}{2 t_{min}k}, \space t_{\text{min}} = \text{min}\\{1,β/L\\} \\\
\end{align}

Backtracking line search의 수렴 식은 fixsd step size 식과 거의 동일하여 분모의 step size인 $$t$$가 $$t_{\text{min}}$$으로 대체되었다고 보면 된다. 만일 $$β$$가 너무 작지만 않다면 fixsd step size와 비교해서 성능 차이는 크지 않다. $$(β/L $$ vs. $$ 1/L)$$