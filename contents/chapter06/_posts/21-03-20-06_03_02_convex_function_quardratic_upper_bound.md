---
layout: post
title: 06-03-02 Convex function quardratic upper bound
chapter: "06"
order: "08"
owner: "Kyeongmin Woo"
---

## Quardratic upper bound
함수 $$f$$가 convex이고 $$\nabla f$$는 Lipschitz continuous하면 다음과 같은 \quadratic upper bound를 갖는다. (단, $$L$$은 Lipschitz constant이다.)

> $$ \begin{align}
f(y) & \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2  \space \space \forall x, y
\end{align} $$

또한, 다음 함수 $$g$$가 convex이면 함수 $$f$$는 \quadratic upper bound를 갖는다.

> $$ \begin{align}
g(x) & = \frac{L}{2} \lVert x \rVert^2_2 - f(x) \space \text{is convex, } \space \forall x \space \space \text{with dom g = dom f }\\\
\end{align} $$

## Proof

#### Monotone Operator
함수 $$f$$는 convex이므로 다음과 같이 $$\nabla f(x)$$에 대한 monotone operator를 갖는다.

> $$(\nabla f(y) - \nabla f(x))^T (y-x) \ge 0$$

[참고] Vector space $$X$$에서 operator $$T : X \to X^{*}$$가 다음 조건을 만족하면 monotone operator라고 한다.

>$$(Tu - Tv, u-v) \ge 0$$, $$\forall u. v \in X$$

#### Lipschitz continuous
$$\nabla f$$는 다음과 같이 Lipschitz constant $$L$$에 대해  Lipschitz continuous하다.

>$$ \lVert \nabla f(x) - \nabla f(y) \rVert_2 \le L \lVert x - y \rVert_2$$  for any $$x, y$$ and $$L \gt 0$$

#### $$g$$가 convex임을 증명
이제 $$g(x) = \frac{L}{2} \lVert x \rVert^2_2 - f(x)$$가 convex임을 보이도록 하자.

함수 $$f$$가 convex이고 $$\nabla f$$는 Lipschitz continuous이므로 Cauchy-Schwarz inequality를 적용해서 다음과 같이 식을 전개해 볼 수 있다.

>
$$ \begin{align}
(\nabla f(x) - \nabla f(y))^T (x-y) & \le \lVert \nabla f(x) - \nabla f(y) \rVert \lVert x - y \rVert \le L \lVert x - y \rVert^2
\end{align} $$

$$\nabla g(x) = Lx - \nabla f(x)$$이므로 위의 식에 $$\nabla f(x)$$ 대신 $$Lx - \nabla g(x)$$를 대입해보자.

>
$$ \begin{align}
(Lx - \nabla g(x) - Ly + \nabla g(y))^T (x-y) & = L(x-y)^T (x-y) - (\nabla g(x)  - \nabla g(y))^T (x-y) 
 \le L \lVert x - y \rVert^2 \\\
\end{align} $$

이제 이 식에서 $$\nabla g$$가 monotone operator가 되도록 좌변과 우변의 항들을 정리해보자.

>
$$ \begin{align}
L(x-y)^T (x-y) -  L \lVert x - y \rVert^2  &\le (\nabla g(x)  - \nabla g(y))^T (x-y) \\\
\end{align} $$

이 식의 좌변을 정리하면 다음과 같이 0이 된다.
>
$$ \begin{align}
L(x-y)^T (x-y) -  L \lVert x - y \rVert^2 & = L(x-y)^T (x-y)  - L(x-y)^T (x-y)  = 0 
\end{align} $$

따라서, $$\nabla g$$는 monotone operator이며 이에 따라 $$g$$는 convex라고 할 수 있다.
>
$$ \begin{align}
(\nabla g(x)  - \nabla g(y))^T (x-y) \ge 0
\end{align} $$

#### $$g$$가 convex일때 $$f$$가 quadratic upper bound를 가짐을 증명
$$g$$가 convex이므로 다음과 같이 first order convexity 성질을 만족한다.
>
$$ \begin{align}
g(y) \gt g(x) + \nabla g(x)^T (y - x)
\end{align} $$


$$g(x)$$를 좌변으로 넘기고 $$g(x) = \frac{L}{2} \lVert x \rVert^2_2 - f(x)$$와 $$\nabla g(x) = Lx - \nabla f(x)$$를 대입해보자.
>
$$ \begin{align}
\frac{L}{2} y^Ty - \frac{L}{2} x^Tx + f(x) - f(y) & \ge (Lx - \nabla f(x))^T (y - x) \\
& = Lx^Ty - Lx^Tx - \nabla f(x)^T (y - x) \\
\end{align}
$$

$$f(y)$$를 우변으로 옮기고 나머지 항들을 좌변으로 옮겨보자.

>
$$ \begin{align}
\frac{L}{2}  (y^Ty  - 2 x^Ty + x^T x) + f(x) + \nabla f(x)^T (y - x)  \ge f(y) \\\
\end{align} $$

이 식을 정리해 보면 다음과 같이 된다.

> $$ \begin{align}
f(y) & \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2  \space \space \forall x, y
\end{align} $$

이로써 함수 $$f$$가 convex이고 $$\nabla f$$는 Lipschitz continuous하면 \quadratic upper bound를 갖는다는 것이 증명되었다.