---
layout: post
title: "09-03 Example: matrix completion"
chapter: "09"
order: 4
owner: "Kyeongmin Woo"
---

# Example: matrix completion


여러 응용에서 측정된 데이터를 행렬로 표현하게 되는데, 이때 행렬의 대부분의 항목들에는 값이 없고 소수의 항목에만 관측 데이터가 있는 희소 행렬인 경우가 있다. 이와 같은 행렬에서 값이 없는 항목(missing entry)들의 값을 채우는 문제를 **Matrix completion** 문제라고 한다. 

예를 들어, 추천 시스템에서 아직 구매를 하지 않은 상품이나 서비스를 고객에게 추천할 때 이런 문제가 발생할 수 있다.

## Maxtrix Completion Problem
**Matrix completion** 문제는 다음과 같이 정의할 수 있다. 

행렬 $$Y ∈ \mathbb{R}^{m×n}$$는 관측 데이터를 갖고 있는 행렬이며, 관측 데이터가 있는 항목을 $$Y_{ij}, (i,j) ∈ \Omega$$라고 하자. 행렬 $$B$$는 관측 값이 없는 항목들을 추정하기 위한 추정 행렬이다.

> $$\min_B \frac{1}{2} \sum_{(i,j)∈\Omega} (Y_{ij} −B_{ij})^2 + λ\lVert B \rVert_{tr}$$

Objective 함수의 첫번째 항은 행렬 $$B$$와 관측 데이터와의 오차를 최소화하며, 두번쨰 항은 행렬 $$B$$를 저차원(low rank) 행렬로 만들어 준다. (여기에는 행렬 B는 저차원의 manifold에 있다고 가정한다.) 따라서, 행렬 $$B$$는 관측 데이터는 그대로 유지하면서 관측 데이터가 형성하고 있는 가장 낮은 차원의 값으로 나머지 부분을 채우는 행렬이 된다.

#### [참고] Trace Norm
행렬의 trace norm은 행렬의 sigular value들의 합이다.

> $$\lVert B \rVert_{tr} = \text{trace}(\sqrt{B^* B}) = \sum_{i=1}^r \sigma_i(B), \quad r = rank(B)$$

$$B^* B$$는 positive semi-definite이고 $$\sigma_1(X) ≥ ... ≥ \sigma_r(X) ≥ 0$$는 singular value이다.

#### [참고] **L1** Norm Regularizer vs. Trace Norm Regularizer
이 문제는 matrix soft-thresholding로 원래 soft-thresholding에서의 벡터가 행렬로 대체되었다고 보면 된다. Regularizer 항을 보면 벡터에 대한 **L1** norm regularizer ( $$\lVert \cdot \rVert_{1}$$)가 행렬에 대한 trace norm regularizer ($$\lVert \cdot \rVert_{tr}$$)로 대체되었는데 실제 두 regularizer의 역할은 같다고 볼 수 있다.

**L1** norm regularizer가 벡터를 sparse하게 만들어 주는데,  trace norm regularizer도 행렬의 sigular value vector를 sprase하게 만들어 주기 때문이다. 즉, 행렬이 diagonal일 때 diagonal을 singular value vector로 볼 수 있으며 trace norm regularizer는 singular value의 합을 최소화 하기 때문에 singular value vector를 sparse하게 해준다.

이 문제에서 trace norm $$\lVert B \rVert_{tr}$$는 $$\text{Rank}(B)$$의 approximation으로 사용되었다고 볼 수 있다.

## Proximal gradient descent
이 문제를 projection operator를 이용해서 정의하면 proximal gradient descent를 Nice하게 적용할 수 있다.
#### Projection Operator
관측값에 대해 projection operator $$P_\Omega$$를 다음과 같이 정의해보자.

> $$[ P_\Omega(B) ] _{ij} =
> \begin{cases}
B_{ij}, & (i,j) ∈ \Omega \\\
0, & (i,j) \notin \Omega
\end{cases}$$

#### Objective Function
Projection operator를 이용해서 objective 함수를 정의하면 다음과 같다.

>$$f(B) = \underbrace{ \frac{1}{2} \lVert P_\Omega(Y) − P_\Omega(B) \rVert_F^2 }_{g(B)} + \underbrace{ \lambda \lVert B \rVert_{tr} }_{h(B)}$$

이제 함수 $$f(B)$$는 differentiable 파트인 $$g(B)$$와 non-differentiable 파트로 $$h(B)$$로 구성되었다. 

#### Proximal Mapping
이제 proximal gradient descent를 적용하기 위해 함수 $$g(B)$$의 gradient를 구하고 proximal mapping를  정의해보자.

* 함수 $$g(B)$$의 gradient : $$\nabla g(B) = −(P_\Omega(Y )−P_\Omega(B))$$
* Proximal mapping : 

> $$ \begin{align}
\text{prox}_t (B) = \underset{Z}{\text{argmin}} \frac{1}{2t} \Vert B−Z \Vert_F^2 + \lambda \Vert Z \Vert_{tr}
\end{align} $$

#### Matrix SVD & Soft-thresholding
Proximal mapping은 $$\lambda$$ 레벨에서의 matrix soft-thresholding로 $$\text{prox}_t(B) = S_{\lambda t}(B)$$이다.

일반적으로 행렬 $$B$$는 매우 크기 때문에 Singular Vector Decompoisition(SVD)를 해서 연산량을 최소화 해야만 한다. 따라서, $$B = U \Sigma V^T$$와 같이 SVD를 했다면 $$S_\lambda(B)$$는 다음과 같이 정의할 수 있다.

> $$ S_\lambda(B) = U \Sigma_\lambda V^T$$

이때, $$\Sigma_\lambda$$는 다음과 같은 대각 행렬이다.

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$
 

#### [참고] $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$  inducement
이 식이 어떻게 도출되었을까? $$\text{prox}_t(B) = Z$$라고 하면 $$Z$$는 다음과 같다.
($$\text{prox}_t(B)$$의 우변을 Z에 대해 미분하면 다음 결과를 얻을 수 있다.)

> $$0 ∈ Z − B + \lambda t \cdot \partial \lVert Z \rVert_{tr}$$

이 식을 정리해 보면 다음과 같다.
>$$\begin{align}
Z & = B - \lambda t \cdot \partial \lVert Z \rVert_{tr} \\
 & = U \Sigma V^T - \lambda t \cdot (UV^T + W) \\
 & = U (\Sigma - \lambda t) V^T - \lambda t  W \\
 & = U (\Sigma - \lambda ) V^T  \\
\end{align}$$

최종 수식은 Lipschitz constant $$L=1$$일 경우 $$t=1$$이고 $$W$$가 0일 경우에 도출될 수 있다.

따라서, $$\text{prox}_t(B) = S_\lambda(B) = Z$$이므로 다음 식이 도출된다..

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$

#### [참고] Derivative of Trace Norm
만약 $$Z = U \Sigma V^T$$라면 trace norm이 미분은 다음과 같다. 
> $$\partial \lVert Z \rVert_{tr} = \{UV^T + W : \lVert W \rVert_{op} ≤ 1, U^TW = 0, WV = 0 \}$$

$$\lVert W \rVert_{op}$$는 operator norm으로 biggest singular value가 1보다 작다. 그리고, $$W$$는 $$U^T$$와 $$V$$와 orthogonal하다.

* 증명은 [Derivative of the nuclear norm with respect to its argument](https://math.stackexchange.com/questions/701062/derivative-of-the-nuclear-norm-with-respect-to-its-argument) 참조

#### Proximal gradient update
이제 proximal gradient 업데이트 식을 정의해 보자.

> $$B^+ = S_{\lambda t} ( B + t( P_\Omega(Y) − P_\Omega(B) ) )$$

$$L = 1$$일 때 $$\nabla g(B)$$는 Lipschitz continuous이므로 ﬁxed step size $$t = 1$$로 선택할 수 있다.

따라서, 업데이트 식이 다음과 같이 간단해졌다.
> $$B^+ = S_\lambda (P_\Omega(Y) + P_\Omega^\bot (B) )$$

$$P_\Omega^\bot$$는 미관측 값에 대한 사영(projection)이며 $$P_\Omega(B) + P_\Omega^\bot (B) = B$$를 만족한다.

이 식에서 $$P_\Omega(Y)$$는 observed 파트이고 $$P_\Omega^\bot (B)$$는 missing 파트이다. $$S_\lambda$$ 함수는 입력 행렬을 SVD를 해서 $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$만 계산하면 되므로 매우 간단하다.

## Soft-Impute Algorithm
이 알고리즘을 **Soft-Impute**이라고 하며 matrix completion에 간단하고 효과적으로 할 수 있다. 일반적으로 행렬이 큰 경우 SVD 계산 비용은 매우 높은데, 이 알고리즘에서는 $$P_\Omega(Y)$$가 sparse하고 $$P_\Omega^\bot (B)$$가 low rank이기 때문에 SVD를 효율적으로 할 수 있게 된다.

* 자세한 내용은 논문 참조 : Mazumder et al. (2011), "Spectral regularization algorithms for learning
large incomplete matrices"

