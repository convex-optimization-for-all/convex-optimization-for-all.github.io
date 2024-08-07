---
layout: post
title: 20 Dual Methods
chapter: "20"
order: 1
owner: "Hooncheol Shin"
---

본 장에서는 dual 을 이용하여 문제를 해결하는 방법으로서,  dual subgradient method, dual decomposition method, augmented Lagrangian method에 대해 알아보고, Alternating Direction Method of Multipliers (ADMM)의 개념을 간단히 알아본다. 

우선 앞에서 배운 내용 중 Proximal Newton method 와 Conjugate function 내용을 간단히 복습한다. 

## Review: proximal Newton method  
다음의 문제가 있다. 
>\begin{equation}
\min_x g(x) + h(x)
\end{equation}

여기서, 함수 $$g$$와 $$h$$는 convex 함수이며, $$g$$는 두번 미분 가능하고, $$h$$는 simple 하다고 가정한다.  

Proximal Newton method는 최초 $$x^{(0)} \in \mathbb{R}^n$$에서 시작되며, 먼저 함수 $$g$$와 $$h$$에게 모두 좋은 최적의 벡터 방향을 아래와 같이 찾는다
>\begin{alignat}{1}
v^{(k)} & = \arg \min_v g({x^{(k-1)}})^T v +  \frac{1}{2} v^T \nabla^2 g(x^{(k-1)}) v + h(x^{(k-1)} + v) 
\end{alignat}

위에서 찾아진 방향으로 아래와 같이 다음 $$x^{(k)}$$를 업데이트한다.  
>\begin{equation}
x^{(k)} = x^{(k-1)} + t_k v^{(k)}, k=1,2,3,\dots 
\end{equation}

여기서, $$t_k$$는 step size로서 backtracking으로 결정된다. 

위 두 과정을 반복적으로 실행한다. 

> * 위 반복(iteration)은 매우 비용이 많이 든다 ($$v^{(k)}$$를 계산하는 것이 일반적으로 매우 어렵다)
* 그러나, 적당한 조건하에서는 converge하기까지 매우 적은 iteration이 요구되고, local quadratic convergence의 수렴 속도를 갖는다 


## Review: conjugate function ###
$$f: \mathbb{R}^n \to \mathbb{R}$$에 대해, conjugate 함수는 아래와 같이 정의된다.   
>\begin{equation}
f^*(y) = \max_x y^Tx - f(x)
\end{equation}

(1) Conjugate 함수는 아래와 같이 쓸 수 있으며, 이는 dual 문제에서 자주 나타나는 형태이다.  
>\begin{equation}
-f^{\ast}(y) = \min_x f(x) - y^Tx
\end{equation}

(2) 만약 $$f$$가 closed하고 convex이면, $$f^{**} = f$$ 이다. 또한, 
>\begin{equation}
x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz
\end{equation}
#### Proof ####
먼저, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$을 증명한다. 

#### 1단계 : $$x \in \partial f^{\ast}(y) \Longleftarrow y \in \partial f(x)$$
>
$$y \in \partial f(x)$$를 가정하자. 그러면, $$x$$는 $$y^Tz - f(z)$$를 최대로 하게 하는 $$z$$들의 집합 $$M_y$$ 에 속하게 된다, 즉 $$x \in M_y$$. <br> 그러나, $$f^{\ast}(y)=   \max_z y^Tz - f(z)$$ 이고, $$\partial f^{\ast}(y)=\text{cl} \left( \text{conv} \left( \bigcup_{z \in M_y} \left\{ z \right\} \right) \right)$$. 따라서, $$x \in \partial f^{\ast}(y)$$

####  2단계 : $$x \in \partial f^{\ast}(y) \Longrightarrow y \in \partial f(x)$$
>
위에서 보인것과 같이, 만약, $$x \in  \partial f^{\ast}(y)$$ 이면, $$y \in \partial f^{\ast\ast}(x)$$. 여기서, $$f^{\ast\ast}(x)=f$$ 이므로 $$y \in \partial f(x)$$.  

위 1, 2 단계를 통해, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$이 증명되었다. 
#### 3단계 : $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$
>
한편, $$y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$은 subgradient의 정의로부터 자명한 사실이다.  <br>
따라서, 위 두 증명을 통해, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$임이 증명되었다.  


(3) 만약 $$f$$가 strictly convex이면,
> $$
> \begin{equation}
> \nabla f^{\ast}(y) = \arg\min_z f(z) - y^T z
> \end{equation}
> $$

#### Proof

>$$f$$가 strictly convex이면, $$f(z)-y^Tz$$는 최소값을 갖는 유일한 $$z$$가 존재하며, 
>이것은 위 (2)에 대한 증명으로부터 $$\nabla f^{\ast}(y)$$이어야 한다. 

다시 말하면 $$f$$가 strictly convex이면  $$f^{\ast}$$의 subgradient는 1개이며 gradient가 된다. 따라서,  $$f^{\ast}$$는 differentiable한 함수이다.
