---
layout: post
title: 08-01-02 Basic Inequality
chapter: "08"
order: "04"
owner: "Kyeongmin Woo"
---

Subgradient method의 convergence theorem과 convergence rate는 다음과 같은 basic inequality를 활용해 증명할 수 있다.

## Basic Inequality

>$$
\begin{align}
f_{best}^{k} - f^* \quad \le \quad \frac{R^{2}+G^{2}\sum_{i=1}^{k}\alpha_{i}^{2}}{2\sum_{i=1}^{k}\alpha_{i}} 
\end{align}
$$

## Proof
$$x^*$$가 함수 $$f$$의 optimal point라고 하면 다음과 같은 등식이 유도된다. 

>$$
\begin{alignat}{1}
 \Vert x^{(k+1)}-x^* \Vert _2^{2} & \quad = \quad  \Vert x^{(k)}-\alpha_k g^{(k)}-x^* \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert (x^{(k)}-x^*)-\alpha_k g^{(k)} \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert x^{(k)}-x^* \Vert _2^2 - 2 \alpha_k g^{(k)T}(x^{(k)}-x^*)+\alpha_k^2 \Vert g^{(k)} \Vert _2^2 \\
\end{alignat} $$

Subgradient의 정의에서 다음과 같은 부등식이 유도된다. 

>$$
\begin{alignat}{1}
f(x^*) \ge f(x^{(k)}) + g^{(k)T}(x^*-x^{(k)}) & \quad \Longleftrightarrow \quad f(x^*)-f(x^{(k)}) \ge  g^{(k)T}(x^*-x^{(k)}) \\
                     & \quad  \Longleftrightarrow \quad f(x^{(k)} - f(x^*)) \le  g^{(k)T}(x^{(k)}-x^*) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(f(x^{(k)}) - f(x^*)) \ge  -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \le -2\alpha_{k}(f(x^{(k)})-f(x^*)) \\
\end{alignat} $$

위의 등식과 부등식을 이용하여 아래의 부등식을 유도된다. 

>$$
\begin{alignat}{1}
 \Vert x^{(k+1)}-x^* \Vert _2^{2}  & \quad = \quad  \Vert x^{(k)}-x^* \Vert _2^{2}-2\alpha_k g^{(k)T}(x^{(k)}-x^*)+\alpha_k^{2} \Vert g^{(k)} \Vert _2^{2} \\
                    & \quad \le \quad  \Vert x^{(k)}-x^* \Vert _2^{2}-2\alpha_k (f(x^{(k)})-f^*)+\alpha_k^{2} \Vert g^{(k)} \Vert _2^{2} \\
\end{alignat} $$

$$k=1,2,3...,n$$일때, 위 부등식에 의해 다음과 같은 관계가 성립한다. 

>$$
\begin{alignat}{1}
 \Vert x^{(2)}-x^* \Vert _2^{2} & \quad \le \quad  \Vert x^{(1)}-x^* \Vert _2^{2}-2\alpha_1(f(x^{(1)})-f^*)+\alpha_1^{2} \Vert g^{(1)} \Vert _2^{2} \\
 \Vert x^{(3)}-x^* \Vert _2^{2} & \quad \le \quad  \Vert x^{(2)}-x^* \Vert _2^{2}-2\alpha_2(f(x^{(2)})-f^*)+\alpha_2^{2} \Vert g^{(2)} \Vert _2^{2} \\
 \Vert x^{(4)}-x^* \Vert _2^{2} & \quad \le \quad  \Vert x^{(3)}-x^* \Vert _2^{2}-2\alpha_2(f(x^{(3)})-f^*)+\alpha_2^{2} \Vert g^{(3)} \Vert _2^{2} \\
& \quad ... \quad \\
 \Vert x^{(n+1)}-x^* \Vert _2^{2} & \quad \le \quad  \Vert x^{(n)}-x^* \Vert _2^{2}-2\alpha_2(f(x^{(n)})-f^*)+\alpha_2^{2} \Vert g^{(n)} \Vert _2^{2} \\
\end{alignat} $$

위의 관계를 이용하면 아래와 같은 재귀적인 전개가 가능하다. 

>$$
\begin{alignat}{1}
 \Vert x^{(2)}-x^* \Vert_2^{2} & \quad \le \quad  \Vert x^{(1)}-x^* \Vert_2^{2}-2\alpha_1(f^{(1)}-f^*)+\alpha_1^{2} \Vert g^{(1)} \Vert_2^{2} \\
 \Vert x^{(3)}-x^* \Vert_2^{2} & \quad \le \quad  \Vert x^{(2)}-x^* \Vert_2^{2}-2\alpha_2(f^{(2)}-f^*)+\alpha_2^{2} \Vert g^{(2)} \Vert_2^{2} \\
& \quad \le \quad ( \Vert x^{(1)}-x^* \Vert_2^{2}-2\alpha_1(f^{(1)}-f^*)+\alpha_1^{2} \Vert g^{(1)} \Vert_2^{2})-2\alpha_2(f^{(2)}-f^*)+\alpha_2^{2} \Vert g^{(2)} \Vert_2^{2} \\
& \quad = \quad  \Vert x^{(1)}-x^* \Vert_2^{2}-2\alpha_1(f^{(1)}-f^*)-2\alpha_2(f^{(2)}-f^*)+\alpha_1^{2} \Vert g^{(1)} \Vert_2^{2}+\alpha_2^{2} \Vert g^{(2)} \Vert_2^{2} \\
& \quad = \quad  \Vert x^{(1)}-x^* \Vert_2^{2} -2\sum_{i=1}^{2}\alpha_i(f(x^{(i)})-f^*) + \sum_{i=1}^{2}\alpha_i^{2} \Vert g^{(i)} \Vert_2^{2} \\
& \quad ... \quad & \\
 \Vert x^{(k)}-x^* \Vert_2^{2}, & \quad k=4,...,n+1 \text{도 위와 같이 전개된다.}
\end{alignat} 
$$

위를 일반화 해보자.

>$$
\begin{alignat}{1}
 \Vert x^{(k+1)}-x^* \Vert_2^{2} \quad = \quad  \Vert x^{(1)}-x^* \Vert_2^{2} -2\sum_{i=1}^{k}\alpha_{i}(f(x^{(i)})-f^*)+\sum_{i=1}^{k}\alpha_{i}^{2} \Vert g^{(i)} \Vert_2^{2}
\end{alignat} $$

$$ \Vert x^{(k+1)}-x^* \Vert _2^{2} \ge 0$$과 $$R \ge  \Vert x^{(1)}-x^* \Vert _2$$라 하면, 다음과 같이 부등식이 정리된다. 

>$$
\begin{alignat}{2}
&  \Vert x^{(k+1)}-x^* \Vert_2^{2} \quad \le \quad R^{2}-2\sum_{i=1}^{k}\alpha_i(f(x^{(i)})- f^{*})+\sum_{i=1}^{k}\alpha_i^{2} \Vert g^{(i)} \Vert_2^{2}\\
\Longleftrightarrow & \quad 0 \quad \le \quad  \Vert x^{(k+1)}-x^* \Vert_2^{2} \quad \le \quad  R^{2}-2\sum_{i=1}^{k}\alpha_i(f(x^{(i)})-f^*)+\sum_{i=1}^{k}\alpha_i^{2} \Vert g^{(i)} \Vert_2^{2} \\
\Longleftrightarrow & \quad 0 \quad \le \quad R^{2}-2\sum_{i=1}^{k}\alpha_i(f(x^{(i)})-f^*)+\sum_{i=1}^{k}\alpha_i^{2} \Vert g^{(i)} \Vert_2^{2} \\
 \Longleftrightarrow & 2\sum_{i=1}^{k}\alpha_i(f(x^{(i)})-f^*) \quad \le \quad R^{2}+\sum_{i=1}^{k}\alpha_i^{2} \Vert g^{(i)} \Vert_2^{2}
\end{alignat} $$

이때 아래의 관계를 이용하여 부등식을 다시 한번 정리한다. 

>$$
\begin{align}
\sum_{i=1}^{k}\alpha_{i}(f(x^{(i)})-f^*)  \quad \ge \quad (\sum_{i=1}^{k}\alpha_i)\min_{i=1,...,k}(f(x^{(i)})-f^*) = (\sum_{i=1}^{k}\alpha_i)(f(x_{best}^{(k)})-f^*)
\end{align}
$$

정리된 부등식은 다음과 같다. 

>$$
\begin{align}
\min_{i=1,..,k} f(x^{(i)})-f^* \quad = \quad f_{best}^{(k)} - f^* \le \frac{R^{2}+\sum_{i=1}^{(k)}\alpha_i^{2} \Vert g^{(i)} \Vert _2^2}{2\sum_{i=1}^{k}\alpha_i} 
\end{align}
$$

$$f$$는 Lipschitz condition에 의해 $$ \Vert g^{(k)} \Vert_2 \le G$$를 만족하므로 최종적으로 basic inequality가 유도된다. 

>$$
\begin{align}
f_{best}^{k} - f^* \quad \le \quad \frac{R^{2}+G^{2}\sum_{i=1}^{k}\alpha_i^{2}}{2\sum_{i=1}^{k}\alpha_i} \\
\end{align}
$$
