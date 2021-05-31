---
layout: post
title: 06-03-05 A look at the conditions & Practicalities
chapter: "06"
order: 11
owner: "Kyeongmin Woo"
---

# A look at the conditions & Practicalities

## Lipschitz continuity & Strong convexity conditions
$$f(β) = \frac{1}{2} \lVert y−Xβ \rVert_2^2$$를 예로 Lipschitz continuity와 Strong convexity에 대한 조건을 살펴보자

#### Lipschitz continuity of $$∇f$$ :
* $$\nabla^2f(x) \preceq LI$$를 의미한다. <br>
* $$∇^2f(β) = X^TX$$이므로 $$L = \sigma^2_{max}(X)$$ 이다.<br>


#### Strong convexity of $$f$$ :
* $$\nabla^2f(x) \succeq mI$$를 의미한다.<br>
* $$\nabla^2f(β) = X^TX$$이므로, $$m = \sigma_{min}^2(X)$$이다.<br>
* 만약 $$X$$가 $$n \times p$$ 행렬일 때 $$p > n$$이면 $$\sigma_{min}(X) = 0$$이 되어, $$f$$는 strongly convex일 수 없다.<br>
* $$\sigma_{min}(X) > 0$$이더라도 condition number $$L/m = \sigma_{max}^2(X)/\sigma_{min}^2(X)$$가 매우 클 수 있다.


함수 $$f$$가 strongly convex하고 Lipschitz gradient를 갖는다면 다음을 만족한다. $$f$$가 두 2차 방정식 사이에 있다고 생각하면 된다.

>$$mI \preceq \nabla^2f(x) \preceq LI \text{ for all } x ∈ \mathbb{R}^n$$ and $$L > m > 0$$


모든 $$x$$에 대해 두 조건을 만족한다는 것은 매우 강력한 것일 수 있다. 하지만 좀 더 고민해보면 다음의 sublevel set에 대해서만 이 조건이 필요하다는 것을 알 수 있다.

> $$S = {x : f(x) \leq f(x^{(0)})}$$

## Practicalities
#### Stopping rule: $$\lVert ∇f(x) \rVert_2$$가 작을 때 종료한다.
$$x^{\star}$$가 해라면 $$\nabla f(x^{\star}) = 0$$이다. 만약  $$f$$가 strong convex라면 다음과 같다.
> $$\lVert \nabla f(x) \rVert_2 ≤ \sqrt{2m \epsilon} ⇒ f(x)−f^{\star} ≤ \epsilon$$ </br>

#### [참고] 유도과정
위의 식이 도출되는 과정은 다음과 같다.
$$f$$가 Strong Convexity를 만족하므로 다음과 같은 상수 $$m \ge 0$$이 존재한다.
> $$ \begin{align}
\nabla^2 f(x) \succeq mI \\
\end{align} $$

함수 $$f$$를 2차 Talyor 식으로 전개해보자.
> $$ \begin{align}
f(y) = f(x) + \nabla f(x)^T(y−x) + \frac{1}{2} (y−x)^T \nabla^2 f(x) (y−x), \space \forall x, y
\end{align} $$

그러면, 위의 $$\nabla f(x) \succeq mI $$에 따라 마지막 항을 lower bound 조건으로 정리할 수 있다.
> $$ \begin{align}
f(y) &  \ge f(x) + \nabla f(x)^T(y−x) + \frac{m}{2} \lVert y−x \rVert_2^2, \space \forall x, y
\end{align} $$

$$f(y)$$를 $$y$$에 대해서 미분을 하면 $$\tilde{y} = x - (1/m) \nabla f(x)$$가 된다. $$\tilde{y}$$를 Tayor 전개에 대입해 보면 다음과 같다.

> $$ \begin{align}
f(y) &  \ge f(x) + \nabla f(x)^T(\tilde{y}−x) + \frac{m}{2} \lVert \tilde{y}−x \rVert_2^2 \\
&  = f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

따라서, $$f(y)$$를 $$f^{*}$$로 대체하면 다음과 같이 정리될 수 있다.
> $$ \begin{align}
 f^{*}  \ge f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

위의 Stopping rule이 다음과 같이 도출되었다.

> $$ \begin{align}
f(x) - f^{*} \le \frac{1}{2m} \lVert \nabla f(x) \rVert^2_2 & \le \epsilon \\
\lVert \nabla f(x) \rVert^2_2 & \le 2m\epsilon \\
\lVert \nabla f(x) \rVert_2 & \le \sqrt{2m\epsilon} \\
\end{align} $$


### Gradient descent의 장단점

#### Pros
* 알고리즘이 단순하며 iteration의 비용이 낮다.
* Well-conditioned, strongly convex 문제에 대해서는 매우 빠르다.

#### Cons
* 많은 문제가 strongly convex이거나 well-conditioned가 아니기 때문에 일반적으로 느리다.
* 미분 불가 함수는 다룰 수 없다.