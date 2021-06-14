---
layout: post
title: 08-03 Improving on the Subgradient Method
chapter: "08"
order: 16
owner: "Kyeongmin Woo"
---

Subgradient method는 미분할 수 없는 컨벡스 함수에도 사용할 수 있다는 점에서 범용성이 큰 것이 장점이다 (more general). 하지만 convergence rate가 $$O(1/\epsilon^{2})$$이므로 gradient descent의 convergence rate인 $$O(1/\epsilon)$$보다 훨씬 느리다. 

Gradient descent와 subgradient method 각각의 장점을 잘 조합하는 방법은 없을까? 다음 장에서는 이 두 알고리즘의 장점을 결합한 proximal gradient descent란 방법을 알아보도록 하겠다.