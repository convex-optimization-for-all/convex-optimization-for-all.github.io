---
layout: post
title: 06-05 Stochastic gradient descent
chapter: "06"
order: 14
owner: "Kyeongmin Woo"
---

# Stochastic gradient descent

다음과 같이 함수의 합을 최소화하는 문제를 고려해보자.
>
$$ \begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation} $$

이 문제에 gradient descent를 적용한다면 각 함수 $$f_i$$에 대해 gradient를 구해서 합산을 해야 한다. (즉,  함수의 합에 대한 gradient는 각 함수의 gradient의 합과 같다.)
>
$$\nabla \sum_{i=1}^m f_i(x) = \sum_{i=1}^m \nabla f_i(x)$$

이 결과를 다음 식에 적용해서 다음 위치로 이동한다. 따라서, 한 step을 이동할 때마다 전체 함수에 대해 gradient를 구해야 한다는 것을 알 수 있다.
>
$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k-1)}), \,  k=1,2,3,\dots
\end{equation} $$

Gradient descent는 모든 함수들의 gradient를 구한 후에 한번에 업데이트를 수행하게 된다. 이런 이유로 gradient descent는 배치 업데이트(batch update) 방식이라고 부른다. 배치 업데이트의 경우 함수의 개수 많아질수록 계산 오버헤드가 크게 증가하는 단점이 있다.

## Stochastic gradient descent
이에 반해, **Stochastic gradient descent (SGD)** 방식은 다음 위치를 찾을 때 한 함수의 gradient만을 구해서 찾는다. 다음 식에서와 같이 SGD에서는 $$k$$번째 iteration에서 하나의 함수 인덱스 $$i_k$$를 선택해서 업데이트를 한다.
>
$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \nabla f_{i_k} (x^{(k-1)}), \, i_k \in \{1,2,\dots,m\}
\end{equation} $$

함수 인덱스 $$i_k$$는 다음 두 가지 방식으로 선택할 수 있다. 

* **순환 업데이트 (Cyclic rule)**: 모든 함수의 인덱스를 동일한 순서로 주기적으로 반복해서 선택하는 방법 $$i_k = 1,2,\dots,m, 1,2,\dots,m, ... $$
* **랜덤 업데이트 (Randomized rule)**: 함수의 인덱스를 균등하게 랜덤하게 선택하는 방법 $$i_k \in \{1,2,\dots,m\}$$

일반적으로 랜덤 업데이트 방식을 더 많이 사용한다.

## Convergence of stochastic gradient descent

**Gradient descent (GD)**와 **Stochastic gradient descent (SGD)** 방식은 어떤 차이가 있을까? 계산적으로 보면 GD는 배치 방식으로 한번에 업데이트를 하는 반면, SGD 방식에서 $$m$$번의 업데이트를 하게 된다. 즉, m stochastic steps $$\approx$$ one batch step이 된다.

그렇다면 업데이트 진행 과정에서는 어떤 차이가 있을까?

SGD의 경우 $$k$$ step에서 $$k+m$$ step으로 m번의 업데이트를 했을 경우 다음과 같이 진행이 된다.
>
$$ \begin{equation}
\text{SGD Cycle rule : } \quad x^{(k+1)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k+i-1)})
\end{equation} $$

GD의 경우 $$k$$ step에서 $$k+1$$ step으로 한번의 업데이트를 했을 경우 다음과 같이 진행이 된다.

>
$$ \begin{equation}
\text{GD Batch : }  \quad  x^{(k+m)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k)})
\end{equation} $$

따라서, 두 업데이트 방식으로 최적값을 탐색할 경우 방향은 아래와 같은 차이를 보이게 된다. 
>
$$ \begin{equation}
\sum_{i=1}^{m}[ \nabla f_i (x^{(k+i-1)}) - \nabla f_i (x^{(k)})]
\end{equation} $$

만일 각  $$\nabla f_i(x)$$가 $$x$$에 대해서 크게 변하지 않는다면 즉, Lipschitz continuous하다면 SGD는 수렴하게 되며 결과적으로 위의 두 방식은 동일한 최적해로 수렴하게 된다.

경험적으로 SGD 방식은 최적점에서 멀리 떨어져 있을 때는 효과적으로 동작하지만 최적점에 가깝게 왔을 때는 수렴에 어려움을 겪는 것으로 알려져 있다.