---
layout: post
title: 08-01-06 Polyak step sizes
chapter: "08"
order: 8
owner: "Kyeongmin Woo"
---

**Polyak step sizes**는 optimal value가 알려져 있을때 step size를 설정하는 방법이다. 만약 $$f^*$$가 알려져 있을 때 다음과 같이 Polyak step sizes를 정의 할 수 있다. 

## Convergence theorem for Polyak step-sizes
>
$$ \begin{align}
t_k = \{\frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}\}, \quad k = 1,2,3...
\end{align} $$


## Proof of convergence theorem for Polyak step-sizes
증명은 [basic inequality]({%post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %})의 유도과정에 이용된 부등식으로부터 증명할 수 있다. 

>
$$ \begin{align}
 \Vert x^{(k)}-x^* \Vert_2^{2}  \quad \le \quad  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} \\
\end{align} $$

위 부등식의 오른쪽 항을 $$t_k$$에 대해서 미분하여 0과 같게 하면 오른쪽 항을 최소화시키는 Polyak step size를 도출할 수 있다. 
>
$$ \begin{align}
& \frac{\partial}{\partial t_k}  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} \quad = \quad 0 \\
 \Longleftrightarrow \quad & -2(f(x^{(k-1)})-f^*)+2t_k \Vert g^{(k-1)} \Vert_2^{2}  \quad = \quad 0 \\
 \Longleftrightarrow \quad & 2(f(x^{(k-1)})-f^*)  \quad = \quad 2t_k \Vert g^{(k-1)} \Vert_2^{2} \\
 \Longleftrightarrow \quad & f(x^{(k-1)})-f^* \quad = \quad t_k \Vert g^{(k-1)} \Vert_2^{2} \\
 \Longleftrightarrow \quad & t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \quad \text{(Polyak step size at k)}
\end{align} $$

Polyak step size의 convergence rate도 [basic inequality]({%post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %})에서 유도된 부등식으로부터 유도할 수 있다. 

## Congervence rate for Polyak step-sizes 

[basic inequality]({%post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %})에서 유도된 부등식에 Polyak step size $$t_i$$를 대입해보자. 
>
$$ \begin{align}
& 2\sum_{i=1}^{k}t_i(f(x^{(i)})-f^*) \le R^2 + \sum_{i=1}^kt_i^2 \Vert g^{(i)} \Vert_2^2 \\
 \Longleftrightarrow \quad & 2\sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 + \sum_{i=1}^k\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \\
 \Longleftrightarrow \quad & \sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 \\
\end{align} $$

Lipschitz condition $$ \Vert g^{(i)} \Vert_2 \le G$$를 항상 만족한다고 가정하면, 위의 부등식은 아래와 같이 정리된다.
>
$$ \begin{align}
& \sum_{i=1}^{k}(f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & k ⋅ (f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & \sqrt{k} ⋅ (f(x^{(i)})-f^*) \le RG \\
 \Longleftrightarrow \quad & (f(x^{(i)})-f^*) \le \frac{RG}{\sqrt{k}} \\
\end{align} $$

$$\frac{RG}{\sqrt{k}}=\epsilon$$이라 하면, $$k=\big(\frac{RG}{\epsilon}\big)^2$$이므로 $$\epsilon$$에 대한 suboptimal point에 도달하는 것이 보장되기 위해서는 $$\big(\frac{RG}{\epsilon}\big)^2$$만큼의 시행 횟수가 필요하다. 즉, convergence rate는 $$O(1/\epsilon^{2})$$으로 다른 subgradient method와 동일하다. 