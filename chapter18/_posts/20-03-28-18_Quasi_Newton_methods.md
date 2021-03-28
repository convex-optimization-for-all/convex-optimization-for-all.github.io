---
layout: post
title: 18 Quasi-Newton methods
chapter: "18"
order: 1
owner: "YoungJae Choung"
---
## Convex Optimization Basic

1950년대 중반, Argonne 국립 연구소에서 근무 중이었던 물리학자 W.C. Davidon은 coordinate descent method를 이용하여 계산량이 큰 최적화 문제를 풀고 있었다. 불행하게도 당시의 컴퓨터가 불안정했던 탓에 계산이 끝나기도 전에 시스템의 충돌이 빈번히 일어났고, 이에 좌절한 Davidon은 계산속도를 좀 더 향상시킬 수 있는 방법을 찾기로 결심하게 된다. 그렇게 탄생하게 된 것이 바로 최초의 Quasi-Newton 알고리즘이다. 이는 nonlinear optimization을 극적으로 진보시키는 계기가 되었으며, 뒤이어 20여 년 동안 이 방법에 대한 다양한 후속연구들이 등장하였다.

아이러니하게도 [Davidon의 연구](http://www.math.mcgill.ca/dstephens/680/Papers/Davidon91.pdf)는 당시 출판되지 못하고 30년 이상을 technical report로 남아있었다. 그리고 마침내 1991년이 되어서야 [SIAM Jounal on Optimization의 첫 번째 판](https://epubs.siam.org/toc/sjope8/1/1)에 실리게 되었다.

Quasi-Newton methods는 각 반복(iterateration)에서 objective function에 대한 gradient만을 필요로 한다. 이는 이차 미분을 필요로하는 newton methods보다 계산적인 부담이 훨씬 적으며 더불어 superlinear convergence를 보인다는 점에서 충분히 매력적인 방법이라고 볼 수 있다 [14]. 

## Motivation for Quasi-Newton methods

다음과 같은 unconstrained, smooth optimization problem이 있다고 해보자.
>$$
>\min_x \: f(x), \\\\
>\text{where } f \text{ is twice differentiable, and } dom \; f = \mathbb{R}^n.
>$$

위 문제에 대한 Gradient descent method와 Newton's method에서의 x에 대한 업데이트 방법은 각각 아래와 같다.
>**Gradient descent method:**
>$$
>x^+ = x - t \nabla f(x)
>$$

>**Newton's method:**
>$$
>x^+ = x - t \nabla^2 f(x)^{-1} \nabla f(x)
>$$

Newton's method는 quadratic convergence rate ($$O(\log \log 1/ \epsilon)$$)의 수렴속도를 보이는 장점이 있는 반면에 아래 두 과정에 의해 상당히 큰 계산비용이 발생하는 문제가 있다. 

* Hessian $$\nabla^2 f(x)$$의 계산: Hessian matrix를 계산하고 저장하기 위해서는 $$O(n^2)$$의 메모리를 필요로 한다. 이는 고차원의 함수를 다루기에 적절하지 않은 성능이다. (참고: [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix#Use_in_optimization) in Wikipedia)
* 방정식 $$\nabla^2 f(x) p = -\nabla f(x)$$의 풀이: 이 방정식을 풀기 위해서는 Hessian $$\nabla^2 f(x)$$에 대한 역행렬을 계산해야 한다. (참고: [Computational complexity of Matrix algebra](https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra) in Wikipedia)

Quasi-Newton method에서는 대신 $$\nabla^2 f(x)$$를 근사(approximation)한 $$B$$를 이용한다.
>**Quasi-Newton method:**
>$$
>x^+ = x + tp \\\\
>\text{where } Bp = -\nabla f(x).
>$$

이때 B는 계산하기 쉬워야 하며, 또한 방정식 $$Bp = g$$를 풀기에도 용이해야 한다. 

## Quasi-Newton Algorithm
Quasi-Newton algorithm은 다음과 같다.

* Pick initial $$x^0$$ and $$B^0$$
* For $$k = 0, 1, \dots$$
    * Solve $$B^k p^k$$ = $$- \nabla f(x^k)$$
    * Pick $$t\_k$$ and let $$x^{k+1} = x^{k} + t\_k p^k$$
    * Update $$B^k$$ to $$B^{k+1}$$
* End for

Optimal point에 점진적으로 다가갈 수 있도록 $$B$$를 업데이트 해가는 것이 이 방법의 큰 특징이다. 즉, $$B$$를 통해 next step인 $$B^+$$를 구하는 방법에 대해 이번 장에서 주로 논의하게 될 것이다. (**Note:** 편의상 $$B^{k+1}, B^k$$와 $$B^+, B$$ 두 가지 표기를 혼용하여 사용하겠다.)