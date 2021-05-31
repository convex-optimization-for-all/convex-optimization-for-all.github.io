---
layout: post
title: 07-02-02 Subgradient Calculus
chapter: "07"
order: "05"
owner: "Kyeongmin Woo"
---

# Subgradient Calculus

볼록함수의 subdifferential에 대한 다음의 몇가지 기본적인 규칙이 성립된다.

### Scaling

>
$$
\eqalign{
\text{if } & a>0, \\
\text{then } &\partial (af) = a\cdot \partial f
}
$$

### Addition

>
$$\partial(f_1 + f_2) = \partial f_1 + \partial f_2$$

위에서 두집합의 연산 $$A+B= \{a+b:a\in A, b \in B\}$$를 의미함. 

### Affine composition 

>
$$
\eqalign{
\text{if } & g(x)=f(Ax+b), \\
\text{then } & \partial g(x) = A^T \partial f(Ax+b)
}
$$

### Finite pointwise maximum

>
$$
\eqalign{
\text{if } & f(x)=\max_{i=1,\dots,m} f_i(x), \\
\text{then } & \partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
}
$$

즉, $$\partial f(x)$$는 $$x$$에서 $$f(x)$$값을 갖는 함수들의 subdifferential의 합집합에 대한 convex hull로 정의된다. 

### General pointwise maximum

>$$
\eqalign{
\text{if } & f(x) = \max_{s \in S} f_s(x),\\ 
\text{then } & \partial f(x) \supseteq cl \left \{ \text{conv} \left(\bigcup_{s:f_s(x)=f(x)} \partial f_s(x)\right) \right\}
}
$$


여기서 $$S$$는 무한집합으로서 무한한 갯수의 집합들의 합집합은 열린집합이 될 수 있으므로, subdifferential이 닫힌집합이 될 수 있도록, closure를 취해주어야 한다. 

한편 집합 $$S$$가 컴팩트하고 (closed and bounded), $$f_s$$ 함수들이 $$s$$에 대해서 연속적이면, 등호 관계가 성립된다. 

예를들어 다음의 p-norm 함수 $$f(x)$$에 대해서,  
>
\begin{equation}
f(x) =  \vert  \vert x \vert  \vert \_p = \max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx, \qquad 1/p + 1/q =1
\end{equation}

$$f_z(x)=z^Tx$$라고 하면, $$f(x)=f_{z^*}(x)$$가 되는 $$z^*$$가 $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$에 속하게 된다. 

한편 $$\partial f_{z^*}(x)=z^*$$ 이므로, $$\bigcup \partial f_{z^*}(x)$$는 모든 $$z^*$$의 합집합으로서, $$\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$ 가 된다.  

여기서 $$S={z: \vert  \vert z \vert  \vert _q \leq 1}$$는 컴팩트 집합이고, $$f_z(x)=z^Tx$$는 선형이므로,

general pointwise maximum 규칙에 의해,  $$\bigcup \partial f_{z^*}(x)$$에 대해서 convex hull을 취한 뒤 closure를 취해도 추가되는 집합의 원소가 존재하지 않는다. 

따라서 $$f(x)$$ 함수의 subgradient는 아래와 같다.

>
\begin{equation}
\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^T x
\end{equation}
