---
layout: post
title: 09-05-04 Is acceleration always useful?
chapter: "09"
order: 10
owner: "Kyeongmin Woo"
---

# Is acceleration always useful?

Acceleration은 매우 효과적인 속도 향상의 도구일 수 있다. 하지만 항상 사용하는 것이 좋을까?

## 성능 향상에 도움이 되지 않는 경우
실제로 **Warm start**를 적용할 때 acceleration을 사용하면 속도가 향상되지 않을 수 있다.
예를 들어, 파라미터를 튜닝하면서 lasso problem을 푼다고 가정해 보자.

> $$\lambda_1 > \lambda_2 > ... > \lambda_r $$

- $$\lambda_1$$에 대해 문제를 풀 때, $$x^{(0)} = 0$$로 초기화를 하고 해 $$\hat{x}(\lambda_1)$$를 저장해둔다.
- $$\lambda_j$$에 대해 문제를 풀 때, $$\lambda_{j−1}$$에 대해 저장된 해로 $$x^{(0)} = \hat{x} (\lambda_{j−1})$$와 같이 초기화를 한다.

$$\lambda$$값이 충분히 튜닝된 경우 proximal gradient descent는 가속 없이도 좋은 성능으로 실행된다. 이 경우 가속을 하게 되면 성능을 저하시키지는 않지만 성능 향상에 크게 도움이 되지는 않는다.

## 성능이 저하되는 경우
어떤 경우에는 acceleration을 사용하면 성능을 저하될 수도 있다. 예를 들어 backtracking에 acceleration을 사용할 경우가 그런 경우이다. Matrix completion problem의 proximal gradient 업데이트에 backtracking을 할 경우를 고려해보자.

> $$B^+ = S_\lambda ( B + t (P_\Omega(Y ) − P^\bot (B) ) )$$

여기서 $$S_\lambda$$는 matrix soft-thresholding operator로 SVD를 실행한다.

* $$t$$를 감소시키면서 backtracking을 할 때마다 generalized gradient $$G_t (x)$$를 계산해야 하는데 이는 내부적으로 행렬 SVD 계산을 포함하는 $$\text{prox}\_t (x)$$의 계산을 의미한다. 이는 성능을 약화시키는 원인이 된다.

* 또한, acceleration은 prox로 전달하는 argument를 변경한다. Matrix completion을 위해 $$x-t \nabla g (x)$$ 대신 $$ v-t \nabla g (v)$$를 사용하게 되는데, $$v$$를 계산하면서 행렬이 더 이상 low rank가 아니게 바뀔 수 있어서 SVD 연산이 더 느려질 수 있다.

> $$B−\nabla g(B) = \underbrace{P_\Omega(Y)}_{\text{sparse}} + \underbrace{P_\Omega^\bot (B)}_{\text{low rank}}$$ ⇒ **fast SVD**

> $$V−\nabla g(V) = \underbrace{P_\Omega(Y)}_{\text{sparse}} + \underbrace{P_\Omega^\bot (V)}_{\text{not necessarily low rank}}$$ ⇒ **slow SVD**

따라서, matrix completion에서는 acceleration과 backtracking line search 방식을 사용하게 되면 오히려 좋지 않다.