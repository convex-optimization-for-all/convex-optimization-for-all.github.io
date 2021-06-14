---
layout: post
title: 07-02-01 Connection to a Convexity Geometry
chapter: "07"
order: "04"
owner: "Kyeongmin Woo"
---


한 볼록집합 (convex set) $$C \subseteq \mathbb{R}^n$$에 대해서, 아래와 같은 indicator 함수 $$I_C: \mathbb{R}^n \to \mathbb{R}$$를 정의했을 때,   

>
$$
I_C(x) = I\{x \in C \} =
\begin{cases}
0               &\text{if } x \in C \\\\
\infty         &\text{if } x \notin C 
\end{cases}
$$

해당 함수의 subdifferential은 다음의 기하학적 의미가 있다.  

#### Lemma
$$x \in C$$에 대해서, $$I_C(x)$$ 함수의 $$\partial I_C(x)$$는 $$x$$에서의 집합 $$C$$에 대한 normal cone $$\mathcal{N}_C(x)$$과 일치한다. 

>
\begin{equation}
\mathcal{N}_C(x) = \{g \in \mathbb{R}^n | g^Tx \geq g^Ty \text{  for all  } y \in C \}
\end{equation}


#### Proof 

Subgradient는 정의에 의해, 다음의 식이 만족된다. 
>
\begin{equation}
I_C(y) \geq I_C(x) + g^T(y-x) \text{ for all $$y$$}
\end{equation}

여기서, $$x \in C$$이고 $$I_C(x)=0$$ 이므로, 아래와 같이 된다. 

>
\begin{equation}
I_C(y) \geq g^T(y-x) \text{ for all $$y$$}
\end{equation}

첫째, 모든 $$y \in C$$에 대해서 아래의 식이 성립되어야 하므로,
>
\begin{equation}
I_C(y) = 0 \geq g^T(y-x)
\end{equation}

subgradient $$g$$는 $$g^Tx \geq g^Ty$$를 만족해야 한다.  

둘째, 모든 $$y \notin C$$에 대해서, $$I_C(y) = \infty$$ 이므로, $$g$$가 어떤 값이든 관계없이 
>
$$I_C(y)=\infty \geq g^T(y-x)$$

가 항상 성립된다. 

위 두 조건에 대해, subgradient는 모두 만족시켜야 하므로, 위 함수에 대한 subgradient는 
>
$$\{g \in \mathbb{R}^n | g^Tx \geq g^Ty\}$$

가 된다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_02_subgrad-5.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 1] Normal cone [1]</figcaption>
</figure>