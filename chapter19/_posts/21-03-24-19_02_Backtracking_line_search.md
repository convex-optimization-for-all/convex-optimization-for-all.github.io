---
layout: post
title: 19-02 Backtracking line search
chapter: "19"
order: 6
owner: "Hooncheol Shin"
---

**Proximal newton method**는 newton's method와 같이 pure step size $$t_k=1, k=1,2,3, \cdots$$인 경우에 수렴하지 않을 수 있다. 따라서, backtracking line search를 통해 step size를 optimize해야 한다.

## Backtracking line search 알고리즘

1. 파라미터를 초기화한다. ($$0 \lt \alpha \le 1/2, 0 \lt \beta \lt 1$$)
2. 각 반복에서 $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$로  Proximal newton direction을 계산한다.
3. $$t=1$$로 초기화 한다.
4. $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ 조건을 만족하면 $$t=\beta t$$로 줄인다. 이 조건이 만족되는 동안 단계4를 반복한다. ($$f = g + h$$)
5. Proximal newton update $$x^+ = x + tv$$를 실행한다.
6. 종료 조건을 만족하지 않으면 단계2로 간다.

직관적으로 $$x$$에서 함수 $$f$$의 선형 근사를 $$\alpha$$배 내에 있는 위치로 direction $$v$$를 따라 이동하도록 step size $$t$$를 찾는다. 그리고, $$f$$에서 $$h$$ 파트는 미분이 되지 않기 때문에 discrete derivative $$h(x + tv) - h(x)$$를 구했다.

## Efficientcy of algorithm
Backtracking line search를 수행하기 위한 방법들이 많이 있으며 여기서는 그 중 한 방법을 소개했다. 

이 방법의 경우 $$v$$를 계산할 때 prox operator를 한번만 계산한다. Proximal gradient descent의 경우 inner loop에서 prox operator의 계산을 반복해야 했는데 이 점과 확연히 구분되는 특징이다. 따라서, 이 방법은 prox operator의 계산이 복잡할 경우 매우 효율적으로 backtracking line search를 할 수 있다.

#### [참고] Method 별  backtracking line search
* Gradient descent [06-02-02 Backtracking line search](https://wikidocs.net/18184)
* Proximal gradient descent [09-02 Convergence analysis](https://wikidocs.net/19033)
* Newton's method [14-04 Backtracking line search](https://wikidocs.net/21334)
