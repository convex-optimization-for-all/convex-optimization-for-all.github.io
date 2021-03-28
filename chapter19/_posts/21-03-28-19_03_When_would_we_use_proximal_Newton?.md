---
layout: post
title: "19-03 When would we use proximal Newton?"
chapter: "19"
order: 7
owner: "YoungJae Choung"
---


Proximal newton method는 언제 사용해야 좋은가? 

Proximal newton method의 유용성을 이해하기 위해  다음 문제에 대해 proximal newton method와 proximal gradient descent를 비교해 보자.

**Problem** : $$\min_x g(x) + h(x)$$

## Proximal gradient descent vs. proximal newton

| **Proximal gradient descent** |**Proximal Newton** | 
| -------- | -------- |
| $$\frac{1}{2} \parallel b - x \parallel_2^2 + h(x)$$ 최소화  | $$b^T x + x^T A x + h(x)$$ 최소화 | 
| Prox operator가 대부분 closed form으로 정의됨  | Prox operator가 대부분 closed form으로 정의되지 않음 
| 반복이 저렴 | 반복이 아주 비쌈 <br> (newton method보다 비쌈)| 
| Gradient descent 수렴 속도 <br> $$O(1/\epsilon)$$  | Newton's method 수렴 속도 <br> $$O(\log \log 1/\epsilon)$$ | 

두 방법은 비슷해 보이지만 실제 매우 다른 일을 한다. 

따라서, proximal newton method는 아주 적은 반복을 기대할 수 있는 scaled prox operator(quadratic + $$h$$)에 대한 빠른 inner optimizer를 가질 때 사용할 수 있다. $$h$$가 separable function일 때 inner optimizer로 가장 많이 사용되는 방법이 coordinate descent이다.