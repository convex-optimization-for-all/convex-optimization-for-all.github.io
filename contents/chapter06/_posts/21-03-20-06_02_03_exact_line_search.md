---
layout: post
title: 06-02-03 Exact line search
chapter: "06"
order: "06"
owner: "Kyeongmin Woo"
---

Gradient descent에서 곡면의 특성에 맞춰 step size를 적응적으로 선택하는 방법 중 또 다른 하나가  **exact line search**이다. 

#### Exact line search 방법이란?
**Exact line search** 방법에서는 gradient 음수 방향의 직선을 따라가며 가장 좋은 step size를 선택한다. 

다음 식에서 알 수 있듯이 $$s$$는 0보다 큰 값으로 $$s$$를 키우면 다음 step 위치인 $$x - s \nabla f(x)$$도 현재 위치에서 멀어진다. 따라서, $$s$$를 키우면서 $$f$$가 최소가 되는 지점의 step size $$t$$를 찾을 수 있다.

> $$t = argmin_{s \ge 0}$$ $$f(x - s \nabla f(x) )$$

**Exact line search** 방법은 변수가 하나인 최소화 문제를 푸는 비용이 검색 방향을 계산하는 비용보다 저렴할 때 사용될 수 있지만, step size를 exhaustive하게 탐색하는 방식때문에 실용적이진 않다. 실제 **backtracking** 방법보다 효율적이지 않으며 잘 사용되지 않는다.