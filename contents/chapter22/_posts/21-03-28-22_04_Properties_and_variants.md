---
layout: post
title: "22-04 Properties and variants"
chapter: "22"
order: "05"
owner: "YoungJae Choung"
---

## Some variants
일부 변종 conditional gradient 방법들을 살펴보자:<br>
• **Line search**: $$γk=2/(k+1),k=1,2,3,...$$를 고정하는 대신 각 $$k = 1, 2, 3, . . .$$ 스텝 사이즈에 대한 exact line search를 사용한다.
> $$γ_k = \arg\min_{γ∈[0,1]} f\Bigl( x^{(k−1)} + γ\bigl(s^{(k−1)} − x^{(k−1)} \bigr) \Bigr)$$

그리고 백트레킹을 사용 할 수도 있다.

• **Fully corrective**: 아래 식에 따라 직접 업데이트 한다.
> $$x^{(k)} = \arg\min_y f(y) \text{ subject to } y ∈ conv\{ x^{(0)}, s^{(0)}, . . . s^{(k−1)} \}$$

이 방식은 훨씬 더 나은 진전을 이룰 수 있지만, Cost가 높다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/22690/away_steps.png" alt="[Fig 3] Away step motivation [3]">
  <figcaption style="text-align: center;">[Fig 3] Away step motivation [3]</figcaption>
</p>
</figure>
<br>


## Another variant: away steps
좀 더 빠른 이해를 위해,  [Fig 3]의 최소화 문제를 살펴 보자. 여기서 최적 해는 (0,0)이다. 그리고 conditional descent 방법은 초기 점 (0,1) 때문에 움직이기 어렵게 된다. 그러나 away step 이동으로 인해 Conditional gradient descent는 가능성 있는 지점으로 이동 할 뿐만 아니라 가능성이 없는 지점에서 벗어나게 된다.



atoms $$A$$ 집합에 대한 Convex hull $$C = conv(A)$$를 가정해 보자

$$A$$에 속한 element의 convex combination으로 $$x∈C$$를 명시적으로 나타낼 수 있다.
> $$x = \sum_{a∈A} λ_a(x)a$$

Away steps에서의 Conditional gradient: \\
$$\text{1. choose } x^{(0)} = a^{(0)} ∈ A$$ \\
$$\text{2. for } k = 1, 2, 3, . . .$$ \\
$$\qquad s^{(k−1)} ∈ \arg\min_{a∈A} ∇f(x^{(k−1)})^Ta,$$
$$\qquad a^{(k−1)} ∈ \arg\max_{a∈A, λa(x(k−1))>0} ∇f(x^{(k−1)})^Ta$$
$$\qquad \text{choose } v = s^{(k−1)} − x^{(k−1)} or \quad v = x^{(k−1)} − a^{(k−1)}$$
$$\qquad x^{(k)} = x^{(k−1)} + γ_kv$$ \\
$$\text{3. end for}$$


## Linear convergence
다음의 제약 조건이 없는 문제를 고려해 보자.
> $$\min_x f(x) \text{ subject to } x ∈ \mathbb{R}^n$$

여기서 $$f$$ is µ-strongly convex이고 $$∇f$$ 는 L-Lipschitz이다.

$$t_k = 1/L$$ 에 대해서 gradient descent $$x^{(k+1)} = x^{(k)} − t_k∇f(x^{(k)})$$를 반복하면서, 다음을 만족시킨다.
> $$f(x^{(k)}) − f^{\star} ≤ \Bigl( 1 −\frac{µ}{L} \Bigr)^k \bigl( f(x^{(0)}) − f^{\star} \bigr)$$

이제 아래의 제약 조건이 있는 문제도 고려해 보자.
> $$\min_x f(x) \text{ subject to } x ∈ conv(A) ⊆ \mathbb{R}^n$$

### [Theorem (Lacoste-Julien & Jaggi 2013)]
$$f$$가 µ-strongly convexd이고, $$∇f$$는 L-Lipschitz 하며 $$A ⊆ \mathbb{R}^n$$는 유한 이라고 가정할 때

적절한 $$γ_k$$에 대해, conditional gradient 알고리즘에 의해 생성 된 반복 스텝은 다음을 항상 만족한다. 
> $$f(x^{(k)}) − f^{\star} ≤ (1 − r)^{k/2}(f(x^{(0)}) − f^{\star}) \text { for } r = \frac{µ}{L}·\frac{Φ(A)^2}{4\text{diam}(A)^2}$$
> $$\text{where }Φ(A) = \min_{F ∈faces(conv(A))} dist(F, conv(A \ F))$$
 
만약 polytope가 평면이면, $$Φ$$는 작고 알고리즘은 천천히 수렴한다.


## Path following
다음 주어진 norm constrained 문제를 살펴보자 
> $$\min_x f(x) \text{ subject to } \| x \| ≤ t$$

Frank-Wolfe 알고리즘은  **path following**에 사용할 수 있다. 다시말해, (대략적인) 솔루션 경로 $$\hat{x}(t), t ≥ 0$$를 생성할 수 있다는 의미 이다.

$$t_0 = 0$$와 $$x^{\star}(0) = 0$$에서 시작하여 매개변수 $$\epsilon, m > 0$$을 수정한 다음 $$k=1,2,3,...$$에 대해 반복한다.

* $$t_k = t_{k−1} + \frac{(1 − 1/m)\epsilon}{\| ∇f(\hat{x}(t_k−1))\|\_{∗}}$$를 계산하고, 모든 $$t ∈ (t_{k−1}, t_k)$$에 대해 $$\hat{x}(t) = \hat{x}(t_{k−1})$$를 설정한다.

* $$t = t_k$$ 에서 Frank-Wolfe를 실행하여 $$\hat{x}(t_k)$$를 계산하고 duality gap이 $$≤ \frac{\epsilon}{m}$$ 인 경우 종료 한다.

이것은 기존의 전략을 단순화 시킨 방법이다. [Giesen et al. (2012)]

이 **path following** 전략을 통해, 방문하는 모든 $t$에 대해 다음을 보장할 수 있다.
> $$f(\hat{x}(t)) − f(x^{\star}(t)) ≤ \epsilon$$

즉, 모든 $$t$$에 대해서 $$\epsilon$$에 의해 균일하게 경계가 정해진 suboptimality gap의 경로를 생성한다.

아래의 수식에서 보듯 Frank-Wolfe duality gap을 다음과 같이 재정의 할 수 있다.
> $$g_t(x) = \max_{\|s\|≤1} ∇f(x)^T(x − s) = ∇f(x)^Tx + t\|∇f(x)\|_{∗}$$

이것은$t$에 대한 선형 함수이다. 따라서 $$g_t(x) ≤ = \frac{\epsilon}{m}$$이면, 다음 수식에 의해서 $$t^+ = t + (1 − 1/m)\epsilon/\|∇f(x)\|_{∗}$$까지 $$t$$를 증가 시킬 수 있다.

> $$g_t+ (x) = ∇f(x)^Tx + t\|∇f(x)\|_{∗} + \epsilon − \epsilon/m ≤ \epsilon$$

즉, duality gap은 동일한 $$x$$에 대해 $$t$$와 $$t^+$$ 사이에서 $$≤ \epsilon$$로 유지된다.

