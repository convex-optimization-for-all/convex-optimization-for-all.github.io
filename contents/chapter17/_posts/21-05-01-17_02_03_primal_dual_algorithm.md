---
layout: post
title: 17-02-03 Primal-Dual Algorithm 
chapter: "17"
order: 6
owner: "Minjoo Lee"
---
Primal-Dual 알고리즘을 정의하기 위해 먼저 $$\tau(x,u)$$를 다음과 같이 정의하자
> $$\tau(x,u) := -\frac{h(x)^Tu}{m} \quad \text{with} \quad h (x) \le 0, u \ge 0$$

참고로 Barrier method에서의 $$t$$와 $$\mu$$를 Primal-Dual 알고리즘에서는 $$\tau$$와 $$\sigma$$로 재정의하여 표기한다.
> $$\tau = \frac{1}{t}, \quad \sigma = \frac{1}{\mu}$$

## Primal-Dual Algorithm 
Primal-Dual 알고리즘은 다음과 같다.
> 1. $$\sigma$$를 선택 ($$\sigma ∈ (0,1)$$)<br>
> 2. $$(x^0,u^0,v^0)$$를 선택 $$(h(x^0) < 0$$. $$u^0 > 0$$)<br>
> 3. 다음 단계를 반복 ($$k = 0,1,... $$)<br>
> $$\quad$$ * Newton step 계산 :<br>
> $$\qquad \quad (x,u,v) = (x^k,u^k,v^k)$$ <br>
> $$\qquad \quad \tau := \sigma \tau(x^k,u^k)$$ 계산<br>
> $$\qquad \quad \tau$$에 대해 $$(\Delta x,\Delta u,\Delta v)$$ 계산<br>
> $$\quad$$ * Backtracking으로 step length $$θ_k$$를 선택<br>
> $$\quad$$ * Primal-Dual 업데이트 :<br>
> $$\qquad \quad (x^{k+1},u^{k+1},v^{k+1}) := (x^k,u^k,v^k) + \theta_k(\Delta x,\Delta u,\Delta v)$$<br>
> 4. 종료 조건 : $$-h(x^{k+1})^Tu \le \epsilon$$ and $$(\parallel r_{prim} \parallel^2_2 + \parallel r_{dual} \parallel^2_2)^{1/2} \le \epsilon $$ 조건을 만족하면 중지 <br>

알고리즘은 각 단계 별로 Newton step을 실행하여 $$(\Delta x,\Delta u,\Delta v)$$를 계산하고  Primal-Dual 업데이트를 하여 $$(x^{k+1},u^{k+1},v^{k+1})$$를 구한다. 단, Backtracking line search를 통해 Primal-Dual 변수가 feasible해 지도록 $$θ_k$$를 선택한다. 알고리즘은 surrogate duality gap과 primal and dual residual이 $$\epsilon$$ 보다 작아지면 종료한다.


## Backtracking line search
Primer-Dual 알고리즘에서 Newton step을 한번만 실행하기 때문에 정확한 해을 찾기 보다는 해의 방향을 구한 것으로 볼 수 있다. 따라서, 그 방향으로 이동하면서 feasible set으로 들어올 수 있도록 적절한 step length를 구해야 한다.

즉, 알고리즘의 각 스텝에서 $$θ$$를 구해서 primal-dual 변수를 업데이트한다.

> $$x^+ = x + θ\Delta x, \quad  u^+ = u + θ\Delta u, \quad v^+ = v + θ\Delta v$$

이 과정에는 두 가지 주요 목표가 있다.

* $$h(x) < 0, u > 0$$의 조건을 유지하는 것
* $$\parallel r(x,u,v) \parallel$$을 감소시키는 것

이를 위해 다단계 백트랙킹 선형 검색(**multi-stage backtracking line search**)을 사용한다.

#### Stage 1: dual feasibility $$u \gt 0$$
처음에는 $$u + \theta \Delta u ≥ 0$$를 만족하는 가장 큰 스텝 $$\theta_{max} ≤ 1$$으로 시작한다. 

> $$\theta_{\max} = \min \Biggl\{1,\  \min \Bigl\{ −\frac{u_i}{\Delta u_i} : ∆u_i < 0 \Bigr\} \Biggr\}$$

위의 식은 다음과 같이 유도된다.

> $$\begin{align}
&u + \theta \Delta u && \ge 0  \\\\
\Leftrightarrow \quad &u && \ge -\theta \Delta u \\\\
\Leftrightarrow \quad &- u/\Delta u && \ge \theta \quad  \text{ such that }-\Delta u \gt 0  \\\\
\end{align}$$

이는 $$u$$를 feasible하게 만드는 과정이다.

#### Stage 2: primal feasibility $$h(x) \lt 0$$
그 다음엔 파라미터  $$\alpha, \beta \in (0,1)$$로 하고 $$\theta$$를 $$0.99\theta_{max}$$로 설정한 후 다음 업데이트를 수행 한다.

* $$h_i(x^+) < 0, i = 1,...m$$를 만족할 때까지, $$θ = βθ$$를 업데이트 <br>

이는 $$x$$를 feasible하게 만드는 과정이다.

#### Stage 3 : reduce $$\parallel r(x,u,v) \parallel$$
* $$\| r(x^+,u^+,v^+) \| ≤ (1−\alpha \theta) \| r(x,u,v) \|$$를 만족할 때까지, $$\theta = \beta \theta$$를 업데이트 

Stage 3의 update 식은 기존의 backtracking line search 알고리즘과 동일하다.

위의 식에서 우항은 다음과 같이 유도될 수 있다. 먼저 Newton's method에서 다음 결과를 얻는다.
> $$\begin{align}
\Delta w = (\Delta x, \Delta u, \Delta v) &\approx -r^{'}(w)^{-1} r(w) \\\\
\Leftrightarrow r(w)  &\approx  -r^{'}(w) \Delta w \\\\
\end{align}$$

위의 식에서 $$r^{'}(w) \Delta w \approx -r(w)$$이므로 이를 아래 Taylor 1차 근사식에 대입한다.
> $$\begin{align}
r(w + \theta \Delta w) & \approx r(w) +  r^{'}(w) (\theta \Delta w) \\\\
&\approx (1-\theta) r(w) \\\\
\end{align}$$

결과적으로 $$r(w + \alpha \theta \Delta w) \approx (1-\alpha  \theta) r(w)$$가 된다.
