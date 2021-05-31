---
layout: post
title: "07-03-05 Example: Distance to a Convex Set"
chapter: "07"
order: "11"
owner: "Kyeongmin Woo"
---

# Example: Distance to a Convex Set

닫힌 볼록집합 $$C $$까지의 거리함수를 아래와 같이 정의한다.  
>
\begin{alignat}{1}
dist(x,C) & = \min_{y \in C} \vert \vert y-x \vert \vert _2 \\
      & = \vert \vert x-P_C(x) \vert \vert _2 \\
      & \geq 0 
\end{alignat}

여기서 $$P_C(x) $$는 한 점 $$x $$에서 집합 $$C $$의 가장 가까운 곳으로의 사영(projection) 이다. 위 거리 함수의 subgradient는 아래와 같다. 
>
\begin{equation}
\partial dist(x,C) = \{\frac{x-P_C(x)}{ \vert \vert x-P_C(x) \vert \vert _2}\}
\end{equation}

#### Proof

만약 $$u=P_C(x) $$라면, first-order 최적 조건에 의해, 
>
\begin{equation}
(x-u)^T(y-u) \leq 0 \ \text{ for all $$y \in C $$}
\end{equation}

여기서, 
>
\begin{equation}
C \subseteq H = \\{y:(x-u)^T(y-u) \leq 0 \\}
\end{equation}

(i) $$y \in H $$에 대해, 
>
\begin{equation}
(x-u)^T(y-u) \leq 0
\end{equation}

한편, $$dist(y,C)\geq 0 $$ 이므로
>
\begin{equation}
dist(y,C) \geq \frac{(x-u)^T(y-u)}{ \vert \vert x-u \vert \vert _2} \text{ for all $$y \in H $$}
\end{equation}

(ii) $$y \notin H $$에 대해, 
>
\begin{equation}
(x-u)^T(y-u) = \vert \vert x-u \vert \vert _2 \vert \vert y-u \vert \vert _2 \cos\theta,
\end{equation}

여기서 $$\theta $$는 $$x-u $$ 와 $$y-u $$ 가 이루는 각을 의미한다. 그러면, 

>
$$
\eqalign{
dist(y,C) &\geq dist(y,H) \\
&= \vert \vert y-u \vert \vert _2 \cos \theta \\
&= \frac{(x-u)^T(y-u)}{ \vert \vert x-u \vert \vert _2} \text{ for all }y \notin H
}
$$

따라서 (i)과 (ii)로부터, 모든 $$y $$에 대해, 
>
$$
\eqalign{
dist(y,C) &\geq \frac{(x-u)^T(y-u)}{ \vert \vert x-u \vert \vert _2} \\
&= \frac{(x-u)^T(y-x+x-u)}{ \vert \vert x-u \vert \vert _2}\\
& = \vert \vert x-u \vert \vert _2 + \left(\frac{x-u}{ \vert \vert x-u \vert \vert _2}\right)^T(y-x)
}
$$

결론적으로, $$dist(x,C) $$는 $$x $$에서 다음의 subgradient를 갖는다. 
>
$$g=\frac{x-u}{ \vert \vert x-u \vert \vert _2}=\frac{x-P_C(x)}{ \vert \vert x-P_C(x) \vert \vert _2} $$

한편, 거리함수의 subdifferential 함수 $$\partial dist(x,C) $$는 하나의 원소만을 갖으므로 $$dist(x,C) $$는 미분가능하고 그 미분값이 곧 subgradient와 일치한다. 
