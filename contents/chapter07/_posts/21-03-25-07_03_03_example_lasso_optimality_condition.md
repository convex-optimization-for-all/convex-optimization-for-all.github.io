---
layout: post
title: "07-03-03 Example: Lasso Optimality Condition"
chapter: "07"
order: 9
owner: "Kyeongmin Woo"
---

아래와 같이 주어진 lasso 문제에 대해,
>
\begin{equation}
\min_{\beta} \frac{1}{2}  \vert  \vert y-X\beta \vert  \vert _2^2 + \lambda \vert  \vert \beta \vert  \vert _1
\end{equation}

여기서 $$y \in \mathbb{R}^n$$, $$X \in \mathbb{R}^{n \times p}$$, $$\lambda \geq 0$$. 

위 문제의 subgradient 최적 조건은 아래와 같이 표현될 수 있다.  
>
$$
\eqalign{
0 \in \partial\left(\frac{1}{2} \vert  \vert y-X\beta \vert  \vert _2^2 + \lambda \vert  \vert \beta \vert  \vert _1\right)
&\quad \Longleftrightarrow \quad 0 \in - X^T (y-X\beta) + \lambda \partial  \vert  \vert \beta \vert  \vert _1 \\
&\quad \Longleftrightarrow \quad X^T (y-X\beta)  = \lambda v \\
& \quad \text{for some } v \in \partial  \vert  \vert \beta \vert  \vert _1
}\\
$$

여기서, 한 점 $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$에 대한 subgradient를  $$v=(v_1,v_2,\dots,v_p)$$ 라고 할 때, 

$$
v_i, i \in \{1,2,\dots,p \} = 
\begin{cases}
\{ 1 \}  &\text{if } \beta_i > 0 \\
\{-1 \}  &\text{if } \beta_i < 0 \\
[-1,1]   &\text{if } \beta_i = 0
\end{cases}
$$

다음을 만족하는 $$\beta$$를 찾을 수 있으며, 해당 $$\beta$$는 최적해가 된다. 
>
\begin{equation}
X^T(y-X\beta) = \lambda v 
\end{equation}

즉, 위 문제에 대한 최적 $$\beta$$에 대해서 다음의 조건이 성립됨을 알 수 있다. 
>
$$
\begin{cases}
X_i^T(y-X\beta) = \lambda \cdot \text{sign}(\beta_i) &\text{if } \beta_i \neq 0 \\
 \vert X_i^T(y-X\beta) \vert  \leq \lambda &\text{if } \beta_i = 0 
\end{cases}$$

위 식에서 $$X_i, i \in \{1,2,\dots, p \}$$는 주어진 행렬 $$X$$의 $$i$$번째 열(column) 데이터를 의미한다. 
