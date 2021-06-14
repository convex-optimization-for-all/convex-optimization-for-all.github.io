---
layout: post
title: 09 Proximal Gradient Descent and Acceleration
chapter: "09"
order: 1
owner: "Kyeongmin Woo"
---

# Proximal Gradient Descent and Acceleration

Non-differentiable한 함수에 대해 최적화를 하기 위해 subgradient method를 사용하게 되면 성능이 다소 느리다는 단점이 있다. 이 성능 문제를 해결하기 위해 제시된 방법이 **proximal gradient descent**이다.

**Proximal gradient descent**는 objective 함수를 미분 가능(differentiable)한 함수와 미분 불가능(non-differentiable)한 함수로 분리한다. 그리고, differentiable한 함수의 다음 위치를 gradient descent로 에측해서 그 위치와 가까우면서 non-differentiable한 함수가 동시에 작아지게 만들 수 있는 가장 좋은 위치로 조정한다.

이 방법은 분석적으로 최적해를 구할 수 있기 때문에 gradient descent와 같은 수렴 속도를 갖게 되며 non-differentiable한 함수가 "simple" 할수록 계산 비용도 gradient descent와 유사해진다.

이 장에서는 **proximal gradient descent**에 전반적인 내용을 살펴보고 추가적인 성능 향상을 위한 여러 **aceleration** 방법들에 대해 살펴보도록 하겠다.
