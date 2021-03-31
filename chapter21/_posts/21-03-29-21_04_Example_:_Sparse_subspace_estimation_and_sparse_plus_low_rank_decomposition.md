---
layout: post
title: 21-04 Example - Sparse subspace estimation and sparse plus low rank decomposition
chapter: "21"
order: 5
owner: "Hooncheol Shin"
---

## Sparse subspace estimation
$$S=X^{T}X, X\in \mathbb{R}^{n\times p}$$일때, 원래의 X와 projection된 X와의 Frobenius norm, 즉, 두 matrix의 거리를 최소화하는 projection를 찾는 문제를 생각해보자.

>$$
>\begin{align}
>\min_{P}||X-XP||^{2}_{F} \qquad \text{subject to rank(P)=k where P is a projection matrix}
>\end{align}
>$$

이 문제는 projection 행렬의 set이 convex set이 아니기 때문에 non-convex 문제이다. 하지만, 아래의 convex 문제와 동일함이 알려져 있다.[[VCLR13](https://wikidocs.net/22687)] 이는 subspace estimation problem이라고도 불린다.

>$$
>\begin{align}
>\max_{Y}tr(SY) \qquad \text{subject to }Y\in F_{k} = \left\{Y\in \mathbb{S}^{p} : 0 \preceq Y \preceq I, tr(Y) = k \right\}
>\end{align}
>$$

[VCLR13]에서는  sparse version(L1 norm이 추가된 형태)의 subspace estimation problem의 해결을 논한다. 
자세한 유도과정은 해당 논문을 참고한다.
>$$
>\begin{align}
>\max_{Y}tr(SY)-\lambda ||Y||_{1} \qquad \text{subject to }Y\in F_{k} 
>\end{align}
>$$

여기서 $$F_{k}$$는 위 식과 동일하게 Fantope of order k이다.

이다. $$\lambda = 0$$, 인 경우 위의 문제는 일반적인 PCA와 동일한 문제이다.

위의 문제는 SDP 형태를 가지고 있고, interior point method로 해결이 가능하다. 하지만, 이는 구현이 복잡하고, 문제 크기가 커지면 무척 느려지는 단점이 있다.

이 문제를 ADMM으로 해결하기 위하여, 문제를 아래와 같이 변형한다.
>$$
>\begin{align}
>\min_{Y,Z}-tr(SY)+I_{F_{k}}(Y) + \lambda||Z||_{1} \qquad \text{subject to }Y = Z.
>\end{align}
>$$

문제를 정리하면 ADMM step은 다음과 같다. 
 >$$
 >\begin{align}
 >Y^{+} &=  \underset{Y}{\operatorname{argmin}} -tr(SY) + I_{F_{k}}(Y)+\frac{\rho}{2}||Y-Z+W||^{2}_{F}\\\\
 >&=\underset{Y\in F_{k}}{\operatorname{argmin}} \frac{1}{2}||Y-Z+W-\frac{S}{\rho}||^{2}_{F}\\\\
 >&=P_{F_{k}}(Z-W+\frac{S}{\rho})\\\\
 >Z^{+} & = \underset{Z}{\operatorname{argmin}}\lambda||Z||_{1}+\frac{\rho}{2}||Y^{+}-Z+W||^{2}_{F}\\\\
 >&=S_{\frac{\lambda}{\rho}}(Y^{+}+W)\\\\
 >W^{+} &=W+Y^{+}-Z^{+}.
 >\end{align}
 >$$
 
여기서 $$P_{F_{k}}$$는 fantope projection operator이다. 이는 eigendecomposition $$A= U\sum U^{T}, \sum = diag(\sigma_{1},...\sigma_{p})$$의  clipping으로 정의된다.[[VCLR13](https://wikidocs.net/22687)]:
>$$
>\begin{align}
>P_{F_{k}}(A) = U\Sigma_{\theta}U^{T}, \Sigma_{\theta} = diag(\sigma_{1}(\theta),...\sigma_{p}(\theta))
>\end{align}
>$$

각각 $$\sigma_{i}(\theta) = \min\left\{\max\left\{\sigma_{i}-\theta,0\right\},1\right\}$$이고, $$\sum^{p}_{i=1}\sigma_{i}(\theta)=k$$ 이다.

## Sparse plus low rank decomposition
$$M\in \mathbb{R}^{n\times m}$$일때, sparse plue low rank decomposition problem은 다음과 같다.[[CLMW09](https://wikidocs.net/edit/page/22687)]
>$$
>\begin{align}
>\min_{L,S}||L||_{tr}+\lambda||S||_{1} \qquad \text{subject to }L+S=M
>\end{align}
>$$

이 문제의 목표는 관측된 행렬 M을 low rank 행렬 L과 sparse matrix S로 분해(decompose)하는 것이다. 목적함수의 첫번째 항은 L의 trace penalty로, L의 singular value의 합을 최소화한다. 두번째 항은 행렬 S에 대한 $$l_{1}$$ norm으로  S에 대한 sparsity를 유도한다. $$\lambda$$는 이 둘을 조절하는 tuning parameter이다. trace norm과 $$l_{1}$$ norm 모두 smooth하지 않고, 일반적으로 trace norm은 해를 찾기 어렵다고 알려져 있다. Sparse subspace estimation 문제와 동일하게 이 문제는 SDP의 형태를 가지고, interior point method로 해결 가능하지만, 이 또한 복잡하고 속도가 느리다. 이 문제에 대하여  ADMM은 조금 더 쉬운 update step을 보여준다.

>$$
>\begin{align}
>L^{+} = S^{tr}_{\frac{1}{\rho}}(M-S+W)\\\\
>S^{+} = S^{l_{1}}_{\frac{\lambda}{\rho}}(M-L^{+}+W)\\\\
>W^{+} = W+M-L^{+}-S^{+}
>\end{align}
>$$

각각 $$S^{tr}_{\frac{1}{\rho}}$$는 matrix soft-thresholding, $$S^{l_{1}}_{\frac{\lambda}{\rho}}$$는 elementwise soft-thresholding이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/24031/candes.png" alt="[Fig 1] Example of sparse plue low rank decomoposition on surveliance camera[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Example of sparse plue low rank decomoposition on surveliance camera[3]</figcaption>
</p>
</figure>

[Fig 1]은 sparse plue low rank decomoposition을 감시카메라 비디오 영상에 분석에 활용한 예시이다. 고정된 지역을 오랜 시간 촬영하는 감시카메라로부터, 대부분의 프레임을 공유하는 low rank 부분을 쉽게 분리해낼 수 있고, sparse한 부분은 특정한 프레임들에 대한 특징적인 부분을 뽑아낸다. 예를 들어서 [Fig 1]의 가운데 column은 low rank, 우측 column은 sparse 부분을 나타낸다. 확인할 수 있듯이, low rank 부분은 거의 모든 프레임에서 나타나는 배경 정보를 가지고 있고, sparse한 부분은 특정한 프레임들에서만 나타나는 특징적인 부분만을 담고 있음을 확인할 수 있다.
