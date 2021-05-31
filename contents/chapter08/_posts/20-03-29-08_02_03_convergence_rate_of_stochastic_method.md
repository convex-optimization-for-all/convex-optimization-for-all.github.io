---
layout: post
title: 08-02-03 Convergence Rate of Stochastic Method
chapter: "08"
order: "01"5
owner: "Kyeongmin Woo"
---

# Convergence Rate of Stochastic Method

Cyclic 방법과 randomized 방법은 convergence rate의 차이를 보인다.

Batch subgradient method의 [convergence rate]({% post_url contents/chapter08/20-03-29-08_01_04_convergence_rate %})는 $$O(G_{batch}^{2}/\epsilon^{2})$$이다. ($$G_{batch}$$는 $$\sum\text{ }f_i$$에 대한 Lipschitz constant)

- **Cyclic method**: Cyclic method의 iteration complexity는 $$O(m^{3}G^{2}/\epsilon^{2})$$이다. 만약 $$m$$번의 cyclic stochastic subgradient method를 한 번의 batch subgradient method로 가정한다면 각 cycle에서 $$O(m^{2}G^{2}/\epsilon^{2})$$ 만큼의 시행이 필요하다. ($$G$$는 하나의 함수 $$f_i$$의 Lipschitz constant)

- **Randomized method**: Randomized method의 iteration complexity는 $$O(m^{2}G^{2}/\epsilon^{2})$$이다. 즉, randomized method는 $$O(mG^{2}/\epsilon^2)$$번의 시행이 필요하므로 batch method와 cyclic method의 $$O(m^2G^2/\epsilon^2)$$보다 $$m$$배 빠르게 수렴하는 것을 알 수 있다. 결과적으로 Big-O 표기법으로는 $$m$$의 값이 크면 randomized method이 convergence rate가 더 빠르다고 할 수 있다.

Randomized method와 cyclic method의 convergence rate는 Big-O 표기법으로는  $$m$$ 배 만큼의 차이가 있지만 사실 cyclic method의 Big-O표현은 worst-case bounded이고 randomized method은 average-case bounded이다. 즉, 어떠한 경우엔 두 방식의 convergence rate의 차이가 Big-O 표기법에서 보이는 것과 같이 그리 크게 차이나지 않을 수 도 있다는 점을 기억하자.
