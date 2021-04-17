---
layout: post
title: 20-02-01 Dual Decomposition with Equality Constraint
chapter: "20"
order: 5
owner: "Hooncheol Shin"
---

다음의 문제를 보자. 
>\begin{equation}
\min_x \sum_{i=1}^B f_i(x_i) \quad \text{ subject to } \quad Ax = b
\end{equation}

만약, 변수 $$x$$를 $$B$$개의 블록으로 분할하고, $$x = (x_1,\dots,x_B) \in \mathbb{R}^n, \text{ where } x_i \in \mathbb{R}^{n_i}$$, matrix $$A$$ 역시 $$B$$개의 sub-matrix 블록으로 다음과 같이 분할하면, $$A = [A_1, \dots, A_B], \text{ where } A_i \in \mathbb{R}^{m \times n_i}$$, 위 minimization 문제는 다음과 같이 $$B$$개의 분리된 문제로 분해될 수 있다.  
> $$
> \begin{alignat}{1}
> & \quad x^+ \in \arg\min_x \sum_{i=1}^B f_i(x_i) + u^T Ax  \\
> \Longleftrightarrow & \quad x_i^+ \in \arg\min_{x_i} f_i(x_i) + u^T A_ix_i, \quad i=1,\dots, B
> \end{alignat}
> $$

#### Dual decomposition 알고리즘: 

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right)
> \end{alignat}
> $$

위 두 단계는 아래와 같이 해석할 수 있다. 
>* 첫번째 수식은 broadcast 단계로서, $$B$$개의 프로세서의 각각에게 $$u$$를 보낸다. 그리고, 프로세서 각각은 병렬로 자신의 최적 $$x_i$$를 찾는다.   
* 두번째 수식은 gather 단계로서, 각 프로세서로부터 $$A_i x_i$$를 모은다. 그리고 global dual 변수 $$u$$를 업데이트 한다. 

위 두 단계는 $$k=1,2,3,\dots$$에 대해 계속 반복한다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/23703/decomposition.png" alt="[Fig 1] Broadcast and Gather" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Broadcast and Gather</figcaption>
</p>
</figure>
