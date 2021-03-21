---
layout: post
title: 04-04 Partial optimization
chapter: "04"
order: 4
owner: "YoungJae Choung"
---
[Reminder: ](https://wikidocs.net/17268#minimization)
$$C$$가 convex set이고 $$f$$가 $$(x,y)$$에 대해 convex일때, $$g(x) = min\_{y \in C} f(x, y)$$는 x에 대해 convex이다.

즉, 위의 성질에 의해 다변수 함수로 구성된 convex problem에서의 partial optimization이 가능하며 이 과정에서 convexity가 유지된다.
<center>
>![](https://wikidocs.net/images/page/18367/partial-optimization.png)</br>

**[Fig1] partial optimization of a convex problem [3]**
</center>

#### Example: hinge form of SVMs
Non-separable set에 대한 SVM 문제는 다음과 같이 정의된다. 
>$$
>\begin{aligned}
>    \text{min}_{\beta, \beta_{0}, \xi} \quad &\frac{1}{2}\|\beta\|_2^2 + C \sum_{i=1}^{n} \xi_{i} \\
>    \text{subject to} \quad &{\xi}_{i} \ge 0, \\ 
>    &y_{i}(x_{i})^T \beta + \beta_{0}) \ge 1 - {\xi}_{i}, \\
>    &i = 1, .., n \\
>\end{aligned}
>$$


위의 제약조건들은 아래의 제약조건 하나로 표현될 수 있다. <br>
> $$
> \begin{aligned}
>    {\xi}_{i} \ge max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\} \\
> \end{aligned}
> $$
    
    
이때, $$max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\}$$는 $${\xi}_{i}$$의 하한임을 이용하여 $$\tilde{f}$$를 얻을 수 있다.<br>


> $$
> \begin{aligned}
>     &\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} {\xi}_{i} \ge \frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} max({0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})})\\
>    &= min\{\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \xi_{i} \quad | \quad \xi_{i} \ge 0, \ y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - \xi_{i}, \ i = 1, .., n\} \\
> &= \tilde{f}(\beta, \beta_{0}) \\
> \end{aligned}
> $$


그리고 아래와 같이 $$\tilde{f}$$를 objective function으로 사용함으로써 좀 더 간단한 형태로 solution을 얻을 수 있다. 주어진 문제에서 $$\xi$$가 제거되었고, 또한 constrained problem에서 unconstrained problem으로 변환되었다.

> $$
> \begin{aligned}
> \text{min}_{\beta, \beta_{0}} \frac{1}{2} \|\beta\|_{2}^2 + C \sum_{i=1}^{n} max\{0, 1 - y_{i} (x_{i}^{T} \beta + \beta_{0}) \}
> \end{aligned}
> $$
