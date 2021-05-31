---
layout: post
title: 08-01-04 Convergence rate
chapter: "08"
order: 6
owner: "Kyeongmin Woo"
---

# Convergence rate

Convergence rate는 알고리즘이 $$\epsilon$$ 오차 범위 내 suboptimal point에 도달하기까지 필요한 시행 수의 경향성을 [Big-O 표기법](https://en.wikipedia.org/wiki/Big_O_notation)으로 나타낸 것이다. 예를들어 $$\epsilon$$이 $$10^{-2}$$이고 알고리즘의 convergence rate가 $$O(1/\epsilon)$$라면, $$\epsilon$$-suboptimal point까지 도달하는데 필요한 시행 횟수의 경향성은 대략 $$1/10^{-2}=10^2$$를 따른다.

[08-01-02 Basic inequality]({% post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %})를 이용하여 fixed step sizes의 subgradient method에 대한 convergence rate를 구해보자.

>$$Recall:$$
>\begin{align}
> f^{k}_{best} - f^{*} \quad \le \quad \frac{R^{2}}{2kt} + \frac{G^{2}t}{2}
\end{align}

임의의 $$\epsilon$$이 $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$와 $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$를 만족한다고 할 때 ($$\epsilon$$은 suboptimality gap, $$G$$는 Lipschitz constant, $$R$$은 알고리즘의 시작점과 optimal point간의 거리),  $$ \frac{R^{2}}{2kt} + \frac{G^{2}t}{2} \le \epsilon$$이다. 만약 $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$이라면 $$t \le \frac{\epsilon}{G^{2}}$$이고 $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$는 결국 $$\frac{R^2G^2}{\epsilon^2} \le k$$를 도출할 수 있다. 이는 시행 횟수가 최소 $$\frac{R^2G^2}{\epsilon^2}$$ 이상이 되면 $$f^{k}_{best} - f^{*} \le \epsilon$$을 만족하게 된다는 의미이다.

이 알고리즘의 convergence rate는 $$O(1/\epsilon^2)$$이므로 이는 gradient descent method의 convergence rate인 $$O(1/\epsilon)$$보다 현저히 많은 시행 횟수가 필요로 한다는 것을 시사한다.