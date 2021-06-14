---
layout: post
title: 18-06 Superlinear convergence
chapter: "18"
order: "07"
owner: "Hooncheol Shin"
---

#### Assumption1: 
> The Hessian matrix $$G$$ is Lipschitz continuous at $$x^∗$$, that is, 
> $$\| G(x) − G(x^∗)  \le L \| x − x^∗ \|,$$
> for all $$x$$ near $$x^∗$$, where $$L$$ is a positive constant.

#### Assumption2: Wolfe conditions
> Assume $$t$$ is chosen (via backtracking) so that
> $$ f(x + tp) \le f(x) + \alpha_1 t \nabla f(x)^T p$$
> and
> $$ \nabla f(x + tp)^T p \ge \alpha_2 \nabla f(x)^T p$$
> for $$0 < \alpha_1 < \alpha_2 < 1.$$

* Wolfe conditions의 첫 번째 조건은 너무 큰 $$t$$가 선택되지 않게끔 한다.
* Wolfe conditions의 두 번째 조건은 너무 작은 $$t$$가 선택되지 않게끔 한다.

DFP와 BFGS는 위 두 가정하에 superlinear convergence를 보인다. (참고: [Rate of convergence in Wikipedia](https://en.wikipedia.org/wiki/Rate_of_convergence))
>$$
>\lim_{k \rightarrow \infty} \frac{ \| x^{k+1} - x^\ast \| }{ \| x^k - x^\ast \| } = 0.
>$$





## Theorem (Dennis-Moré)

다음은 Quasi-Newton method의 search direction이 Newton direction을 충분히 잘 근사하고 있을때, solution으로 수렴하는 과정에서 step length가 Wolfe conditions를 만족함을 보인다. Superlinear convergence를 보이기 위해 search direction이 만족해야하는 조건이라고도 할 수 있다 [14].

>$$f$$가 두 번 미분 가능하고 $$x^k \rightarrow x^\ast$$ s.t. $$\nabla f(x^\ast) = 0$$이며 $$\nabla^2 f(x^\ast)$$가 positive definite이라고 가정하자. 
>
>$$\lim_{k \rightarrow \infty} \frac{\| \nabla f(x^k) + \nabla^2 f(x^k) p^k \| }{\| p^k \|} = 0.$$
>
>만약 search direction $$p^k$$가 위 조건을 만족하면, 다음 두 가지 항목을 만족하는 $$k_0$$가 존재한다.
> 
> 1. $$k \ge k_0$$에 대해 step length $$t_k=1$$은 Wolfe conditions를 만족한다.
> 2. 만약 $$k \ge k_0$$에 대해 $$t_k = 1$$이면 $$x^k \rightarrow x^\ast$$는 superlinear convergence를 보인다.
 