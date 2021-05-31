---
layout: post
title: 19-07 Projected Newton method
chapter: "19"
order: "01"1
owner: "Hooncheol Shin"
---

## What's wrong with projected Newton?
$$h$$가 convex set $$C$$의 indicator function $$h = I_c(x)$$일 때 문제는 다음과 같이 정의될 수 있다.

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  x \in C$$

따라서,  $$h(x) = I_c(x)$$이면 proximal gradient descent는 **projected gradient descent**가 된다. 즉, projected gradient descent는 proximal gradient descent의 special case이다.

$$h(x) = I_c(x)$$일 때 proximal Newton의 경우엔 어떠한가? 이 경우 update 식은 다음과 같이 정의된다.

> $$
> \begin{align}
> z^{+} & =\underset{z \in C}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2  \\\\
> &= \underset{z \in C}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x)  \\\\
> \end{align}
> $$

$$H = I$$이면 $$x - \nabla g(x)$$를 set $$C$$에 projection한 결과가 되지만, 일반적인 $$H \neq I$$에 대해서는 projection이 아니다. ($$H = I$$이면 $$l_2$$-norm이 되기 때문에 H-norm이 아닌 $$l_2$$-norm 이었다면 projection이 되었을 것이다.) 
따라서, projected Newton method는 proximal Newton method의 special case가 아니다.

## Projected Newton for box constraints
특별한 경우 box constraint를 갖는 문제에 대해 projected Newton를 적용할 수 있다. (Bertsekas, 1982; Kim et al., 2010; Schmidt et al., 2011).

문제가 다음과 같다고 하자.

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  l \le x \le u $$

Projected Newton method의 시작 점 $$x^{(0)}$$와 작은 상수 $$\epsilon \gt 0$$라고 할 때  다음 단계를 반복한다 ($$k = 1, 2, 3, ...$$).

* 단계1: Binding set을 정의한다.

> \begin{align}
B_{k-1} & = \\{ i : x_i^{(k-1)} \le l_i + \epsilon \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \gt 0 \\} \quad  \cup \quad 
\\{ i : x_i^{(k-1)} \ge u_i - \epsilon  \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \lt 0 \\} 
\end{align}

최적화 step에서 이 변수들을 box constraint의 경계로 밀어낸다. 이들을 점점 더 많이 밀어낼수록 목적 함수는 줄어든다.

* 단계2: Free set $$F_{k-1} = \left\{1,....,n \right\} \backslash B_{k-1}$$을 정의한다.
* 단계3: Free variable을 따라서 Hessian의 주요 submatrix의 inverse를 정의한다.

>$$ S^{(k-1)} = [(\nabla^2 g(x^{(k-1)}))_{F_{k-1}}]^{-1}$$

* 단계4: Fee variable을 따라 Newton step을 실행하고 projection을 한다.

> $$
> \begin{align}
> x_{(k)} = P_{[l, u]} \left( x^{(k-1)} - t_k \begin{bmatrix} S^{(k-1)} & 0 \\
> 0 & I \end{bmatrix} 
> \begin{bmatrix} \nabla F_{k-1} g(x^{(k-1)}) \\ \nabla B_{k-1} g(x^{(k-1)}) \end{bmatrix}
> \right)
> \end{align}
> $$

여기서 $$P_{[l,u]}$$는 $$[l, u] = [l_1, u_1] \times \cdots [l_n, u_n]$$로의 projection이다.

행렬식을 보면 free varaible에 대해서는 Newton step을 실행하지만 binding variable의 경우 변하지 않는 것을 알 수 있다. 또한, projection은 box 범위 밖에 있는 점들에 대해서 각 좌표에 대해 적절한 $$l_i$$ 또는 $$u_i$$를 지정해주는 간단한 작업이다.

이 방법은 문제가 매우 크고 (ex, 차원이 큰 경우) 대부분의 variable이 boundary 근처에 있어서 free set이 매우 작을 때 최적화를 하는 방법이다.

어떤 종류의 문제가 box constraint를 갖는가? 다음과 같이 이런 종류의 문제는 매우 많은 것으로 알려져 있다.

*  Nonnegative least squares
*  Support vector machine dual
*  Graphical lasso dual
*  Fused lasso (total variation denoising) dual

## Convergence properties
* Bertsekas (1982)는 적절한 가정하에 projected Newton으로 유한번 반복을 하면 적절한 binding constraints를 찾을 수 있다는 것을 보였다. 그러면, free variable에 대해 Newton's method와 같아진다.
*  Bertsekas (1982)는 또한  superlinear convergence를 증명하였다.
*  Kim et al. (2010), Schmidt et al. (2011)은 BFGS-style update를 사용한 projected quasi-Newton method를 제안했다.