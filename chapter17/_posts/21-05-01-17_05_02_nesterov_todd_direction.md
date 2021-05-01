---
layout: post
title: 17-05-02 Nesterov-Todd direction
chapter: "17"
order: 10
owner: "Minjoo Lee"
---
## Nesterov-Todd direction
앞에서의 symmetry 문제는 **Nesterov-Todd** direction으로 해결할 수 있다.
 
먼저 다음 식을 선형화(linearization)하고자 한다.
> $$XS −\tau I = 0. $$

Primal linearization: 
> $$S −\tau X^{−1} = 0 \rightsquigarrow τX^{−1}∆XX^{−1} + \Delta S = \tau X^{−1} −S.$$

Dual linearization: 
> $$X −\tau S^{−1} = 0 \rightsquigarrow \Delta X + \tau S^{−1}\Delta SS^{−1} = \tau S^{−1} −X.$$

이 두 식을 평균하면 primal-dual linearization을 구할 수 있다.
> $$W^{−1}\Delta XW^{−1} + \Delta S = \tau X^{−1} −S$$

이 식을 $$WSW = X$$라고 하고 다음과 같이 정리할 수 있다.
> $$\Delta X + W\Delta SW = \tau S^{−1} −X$$

$$X,S$$에 대한 기하평균(geometic mean)으로 $$W$$를 정의하면 위의 식을 얻을 수 있다.
> $$\begin{align}
> W & = S^{−1/2}(S^{1/2}XS^{1/2})^{1/2}S^{−1/2} \\\
> & = X^{1/2}(X^{1/2}SX^{1/2})^{−1/2}X^{1/2}
> \end{align}$$



### Semideﬁnite Programming 을 위한 Primal-Dual Algorithm<br>
Nesterov-Todd를 이용한 SDP를 위한 Primal-Dual 알고리즘을 정의해보자.

$$X,S \succeq 0$$일 때 $$\tau (X,S) := \frac{X \cdot S}{n}$$라고 하자.

Primal-Dual Algorithm :
> 1. 0에서 1사이의 $$\sigma$$ 를 선택 ($$\sigma  ∈ (0,1)$$)<br>
> 2. $$X^0,S^0 \succ 0$$를 만족하는 $$(X^0,y^0,S^0)$$ 를 선택<br>
> 3. For $$k = 0,1,... $$<br>
> $$\quad$$ * Nesterov-Todd 방향 계산<br>
> $$\qquad \quad (X,y,S) = (X^k,y^k,S^k), τ := \sigma \tau(X^k,S^k)$$<br>
> $$\quad$$  * Step length $$\theta_k$$ 선택 및 Primal-Dual 업데이트<br>
> $$\qquad \quad (X^{k+1},y^{k+1},S^{k+1}) := (X^k,y^k,S^k) + θ_k(\Delta X,\Delta y,\Delta S)$$<br>    


