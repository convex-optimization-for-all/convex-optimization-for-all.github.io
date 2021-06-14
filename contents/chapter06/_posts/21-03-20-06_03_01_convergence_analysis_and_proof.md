---
layout: post
title: 06-03-01 Convergence analysis & Proof
chapter: "06"
order: "08"
owner: "Kyeongmin Woo"
---

$$f$$는 convex이고 differentiable하며 **dom** $$f = R^n$$일 때 다음 식을 만족한다고 하자.

>$$ \lVert \nabla f(x) - \nabla f(y) \rVert_2 \le L \lVert x - y \rVert_2$$  for any $$x, y$$ and $$L \gt 0$$ <br>

$$\nabla f$$는 Lipschitz constant $$L$$에 대해  Lipschitz continuous하다고 말할 수 있다.

참고 : [[(Wikipedia) Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Convergence Theorem
> **Gradient descent**는 fixed step size $$t \le 1/L$$에 대해 다음 식을 만족한다. 
>$$
\begin{align}
f(x^{(k)}) - f^{*} \le  \frac{ \lVert x^{(0)} - x^{*} \rVert^2_2 }{2tk}
\end{align}
$$

Gradient decent가 fixed step size일때 convergence rate $$O(1/k)$$가 된다. 또한, $$f(x^{(k)}) - f^{*} \le \epsilon$$라면 $$O(1/\epsilon)$$의 반복이 필요하다.

## Proof

$$\nabla f$$는 Lipschitz continuous하며 $$f$$는 Lipschitz constant $$L$$을 계수로 하는 2차 항으로 된 quadratic upper bound를 갖는다. (Upper bound의 증명은  [06-03-02]({% post_url contents/chapter06/21-03-20-06_03_02_convex_function_quardratic_upper_bound %}) 절을 참조)

> $$
\begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2  \space \space \forall x, y
\end{align}
$$

Gradient descent를 현재 위치 $$x$$에서 다음 위치 $$x^+ = x - t \nabla f(x)$$로 진행한다고 해보자. 위의 식에서 $$y = x^+$$라고 하고 전개해보자.


>$$
\begin{align}
f(x^+) & \le f(x) +  \nabla f(x)^T (x^+ - x) + \frac{L}{2} \lVert x^+ - x \rVert^2_2 \\\
& = f(x) +  \nabla f(x)^T (x - t \nabla f(x) - x) + \frac{L}{2} \lVert x - t \nabla f(x) - x \rVert^2_2 \\\
& = f(x) - t \nabla f(x)^T (\nabla f(x)) + \frac{L}{2} \lVert t \nabla f(x) \rVert^2_2 \\\
& =  f(x) - t \lVert \nabla f(x)) \rVert^2_2 + \frac{Lt^2}{2} \lVert \nabla f(x) \rVert^2_2 \\\
& =  f(x) - t ( 1 - \frac{Lt}{2} )\lVert \nabla f(x) \rVert^2_2 \\\
& \le f(x) -  \frac{t}{2} \lVert \nabla f(x) \rVert^2_2 \\\
\end{align}
$$

마지막 라인은 $$t \le 1/L$$이기 때문에 $$Lt/2 \lt 1/2$$이 된다. 따라서 다음과 같이 정리될 수 있으며 $$f(x^+) \lt f(x)$$임을 알 수 있다.

>$$
\begin{align}
f(x^+) & \le f(x) -  \frac{t}{2} \lVert \nabla f(x) \rVert^2_2 \\\
\end{align}
$$

$$f$$는 convex이기 때문에 다음과 같이 1차 미분의 특성을 만족한다. (즉, $$f$$는 convex이기 때문에 $$x$$에서의 접선보다 항상 윗쪽에 존재한다.)

>$$
\begin{align}
f(y)  \ge f(x) + \nabla f(x)^T (y-x) \space \space \forall x,y \in \text{dom} (f) \\\
\end{align}
$$


이 식에서 $$y = x^{*}$$라고 하면 다음과 같이 정리된다.

>$$
\begin{align}
f(x)  \le f(x^{*}) + \nabla f(x)^T (x-x^{*}) \\\
\end{align}
$$

이 convexity를 $$f(x^+)$$ 식과 합쳐서 전개해보자.

>$$
\begin{align}
f(x^+) & \le f(x) -  \frac{t}{2} \lVert \nabla f(x) \rVert^2_2 \\\
& \le f(x^{*}) + \nabla f(x)^T (x-x^{*}) - \frac{t}{2} \lVert \nabla f(x) \rVert^2_2 \\\
& = f(x^{*}) + \frac{1}{2t} ( \lVert x - x^{*} \rVert^2_2 -  \lVert x - x^{*} \rVert^2_2 - t^2 \lVert \nabla f(x) \rVert^2_2 + 2t \nabla f(x)^T (x - x^{*}) )  \\\
& = f(x^{*}) + \frac{1}{2t} ( \lVert x - x^{*} \rVert^2_2 -  (x - x^{*})^T (x - x^{*}) - t^2 \nabla f(x)^T  \nabla f(x) + 2t \nabla f(x)^T (x - x^{*}) )  \\\
& = f(x^{*}) + \frac{1}{2t} ( \lVert x - x^{*} \rVert^2_2 -  [(x - x^{*})^T (x - x^{*}) + t^2 \nabla f(x)^T  \nabla f(x) - 2t \nabla f(x)^T (x - x^{*})] )  \\\
&= f(x^{*}) + \frac{1}{2t} ( \lVert x - x^{*} \rVert^2_2 -  [(x - t \nabla f(x)^T - x^{*})^T (x - t \nabla f(x)^T - x^{*})] )  \\\
& = f(x^{*}) + \frac{1}{2t} ( \lVert x - x^{*} \rVert^2_2 -  \lVert  x - t \nabla f(x)^T - x^{*} \rVert^2_2 )  \\\
& = f(x^{*}) + \frac{1}{2t} ( \lVert x - x^{*} \rVert^2_2 -  \lVert  x^+ - x^{*} \rVert^2_2 )  \\\
\end{align}
$$

마지막 단계는 $$x^+ = x - t \nabla f(x)$$이기 때문이다. 단계 $$i$$에 이 결과를 적용해 보면 다음과 같아진다.
>$$
\begin{align}
f(x^{(i)}) - f(x^{*}) & \le \frac{1}{2t} ( \lVert x^{(i-1)}  - x^{*} \rVert^2_2 -  \lVert  x^{(i)} - x^{*} \rVert^2_2 )  \\\
\end{align}
$$

따라서, 위의 식을 $$i = 1$$에서 $$k$$까지 더하면 다음과 같이 된다.

>$$
\begin{align}
\sum_{i=1}^k f(x^{(i)}) - f(x^{*}) & \le \sum_{i=1}^k \frac{1}{2t} ( \lVert x^{(i-1)}  - x^{*} \rVert^2_2 -  \lVert  x^{(i)} - x^{*} \rVert^2_2 )  \\\
& = \frac{1}{2t} ( \lVert x^{(0)}  - x^{*} \rVert^2_2 -  \lVert  x^{(k)} - x^{*} \rVert^2_2 )  \\\
& \le \frac{1}{2t} ( \lVert x^{(0)}  - x^{*} \rVert^2_2 )  \\\
\end{align}
$$

마지막 단계에서 각 $$i$$의 첫번째 항은 $$i-1$$의 두번째 항으로 소거되어 최종적으로 첫번째 항과 마지막 항만 남게 된다. $$f(x^{(k)})$$가 non-increasing임을 적용하여 정리해 보면 다음과 같다.

>$$
\begin{align}
\frac{1}{k} \sum_{i=1}^k f(x^{(i)}) - f(x^{*}) \ge  \frac{1}{k} \sum_{i=1}^k f(x^{(k)}) - f(x^{*}) = f(x^{(k)}) - f(x^{*})
\end{align}
$$

이에 따라 최종 결과는 다음과 같다.

>$$
\begin{align}
f(x^{(k)}) - f(x^{*}) \le \frac{1}{2tk} ( \lVert x^{(0)}  - x^{*} \rVert^2_2 )  \\\
\end{align}
$$

이로써 Gradient descent의 Convergence Theorm이 증명되었다.