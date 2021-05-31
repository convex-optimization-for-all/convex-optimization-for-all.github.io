---
layout: post
title: "23-04 Example: Pathwise coordinate descent for lasso"
chapter: "23"
order: 5
owner: "YoungJae Choung"
---

이번 절에서는 Pathwise coordinate descent for lasso에 대한 개요를 간단히 소개하도록 한다 [[Friedman et al. (2007)](https://arxiv.org/pdf/0708.1485.pdf)] [[Friedman et al. (2009)](https://www.jstatsoft.org/article/view/v033i01/v33i01.pdf)]. 

>**Lasso regression problem:**
> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

[07-03-03 Example: Lasso Optimality Condition]({% post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %})에서 lasso regression 문제에 대한 optimality condition을 유도해 보았다. 위 문제에 대한 최적해는 다음의 조건을 만족한다.

>
> $$
> \begin{align}
> X_1^T(y-X\beta) &= \lambda v_1\\
> X_2^T(y-X\beta) &= \lambda v_2\\
> \dots\\
> X_p^T(y-X\beta) &= \lambda v_p
> \end{align}
> $$

**Note:**
$$X_i,i \in \{ 1,2,…,p \}$$는 주어진 행렬 $$X$$의 $$i$$번째 열(column) 데이터를 의미한다.

여기서 $$v=(v_1,v_2,\dots,v_p)$$는 $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$에 대한 subgradient다. 
>
$$
v_i, i \in \{1,2,\dots,p \} = 
\begin{cases}
\{ 1 \}  &\text{if $\beta_i > 0$} \\
\{-1 \}  &\text{if $\beta_i < 0$} \\
[-1,1]   &\text{if $\beta_i = 0$}
\end{cases}
$$

이 optimality condition에 의해 $$\beta$$의 각 원소가 현재 최적상태에 해당하는지 파악할 수 있다. Coordinate descent 알고리즘을 이용하면 아직 최적상태에 도달하지 못한 원소만을 업데이트하는 방식으로 좀 더 효율적으로 lasso 문제를 푸는 것이 가능해진다. 또한 $$\lambda$$의 값이 클수록 lasso regression 문제에서 coordinate descent 알고리즘이 더 빨리 동작하는 경향성을 활용하여 $$\lambda$$를 점점 줄여가는 방식(warm start)으로 해에 더욱 빠르게 접근한다.

## Algorithm

#### Outer loop (pathwise strategy):
* $$\lambda_1 > \lambda_2 > \dots > \lambda_r$$의 순서를 따라 최적해를 계산한다.
* Tuning parameter  $$\lambda_k$$에서 계산된 결과를  $$\lambda_{k+1}$$에 대한 coordinate descent algorithm을 초기화하는데 사용한다. (warm start)

#### Inner loop (active set strategy):
* 하나 혹은 적은 수의 coordinate cycle을 시행한다. 그리고 0이 아닌 $$\beta$$의 원소를 active set $$A$$에 기록한다.
* $$A$$에 기록된 원소들에 대해서만 수렴할 때까지 coordinate cycle을 시행한다.
* $$\beta$$의 모든 원소들에 대해 optimality condition을 확인한다. 조건을 만족하지 않는 원소가 있으면 $$A$$에 추가하고 step 1으로 다시 돌아간다.

## Notes
* 통상적으로 pathwise strategy는 문제에서 주어진 $$\lambda$$에 대한 해를 바로 구하는 것보다 훨씬 효율적으로 동작한다.
* Active set strategy는 sparsity에 대해 이점이 있다. 이 때문에 coordinate descent는 ridge regression보다 lasso regression에서 훨씬 더 빠르게 동작한다. (참고: [ridge regression과 lasso regression의 경향성 분석](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/))
* Pathwise coordinate descent for lasso는 lasso regression 문제에 대해 가장 빠르다고 알려진 다른 알고리즘들에 비견될만큼 빠르게 동작한다.