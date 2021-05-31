---
layout: post
title: 03-04-01 Definition and examples
chapter: "03"
order: "09"
owner: "Minjoo Lee"
---
## Definition

함수 $$f : R^n \rightarrow R$$가 도메인 **dom** $$f$$와 모든 sublevel set $$S_{\alpha}$$([03-01-03]({% post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %}) 참고)이 convex라면 이 함수를 **quasiconvex** (or **unimodal**)이라고 한다. 

>$$f : R^n \rightarrow R$$ is quasiconvex if dom $$f$$ and 
>$$S_{\alpha} =$$ {$$x \in dom$$ $$f \mid f(x) \leq \alpha$$} for $$\alpha \in R$$ are convex.


만약 함수 -$$f$$가 quasiconvex라면, $$f$$는 **quasiconcave** 라고 불린다.<br>
>$$f : R^n \rightarrow R$$ is quasiconcave if dom $$f$$ and 
>$$S_{\alpha} =$$ { $$x \in dom$$ $$f \mid f(x) \geq \alpha $$} for $$\alpha \in R$$<br>

$$f$$가 quasiconvex이고 qausiconcave일 때, 이를 **quasilinear**라고 하고, 함수의 도메인과 모든 level set에서 {$$x \mid f(x)=\alpha$$}는 convex가 된다. 다음 그림은 quasiconvex function의 예를 보여준다.<br><br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="https://wikidocs.net/images/page/17416/Fig3.9_quasiconvex_ftn_cAsoUpr.PNG" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] quasiconvex function on R [1]</figcaption>
</p>
</figure>


$$\alpha$$에 대하여, $$\alpha$$-sublevel set $$S_{\alpha}$$는 convex, 즉 interval [$$a,b$$]이다. $$\beta$$-sublevel set $$S_{\beta}$$는 interval ($$-\infty,c$$]을 갖는다. **Convex function은 convex sublevel set을 가지며, quasiconvex가 성립하지만, 그 역은 성립하지 않는다.**
> $$f$$ : convex $$\Longrightarrow$$ $$f$$ : quasiconvex


<br>
## Examples

Quasiconvex에서의 다양한 예제를 살펴보자.

#### Logarithm
$$R_{++}$$공간에서의 $$\log x$$는 quasiconvex이다. (또한 quasiconcave이므로, quasilinear의 성질을 갖는다.) 
> $$log x$$ on R
<br>


#### Celing function 
Celing function은 quasiconvex이다. (또한 quasiconcave 이다.)
>$$ceil(x) = inf$${$$z \in Z \mid z \geq x$$} 
<br>



#### Length of vector
$$x \in R^n$$의 길이를 nonzero component의 가장 큰 index 값으로 놓는다면,
>$$f(x) = max$${$$i \mid x_i \neq 0$$}.<br>

이 성립하며, <br>

>$$f(x) \leq \alpha \Longleftrightarrow x_i = 0$$ for $$i = \lfloor\alpha\rfloor + 1,...,n.$$ on $$R^n$$<br>

의 subspace를 만족하므로, quasiconvex이다.<br>
(※ subspace : subspace 내에 있는 모든 원소들은 덧셈, 곱셈에 대해 닫혀있다. $$R^n$$의 subspace도 convex set 이다.)<br>



#### Linear-fractional function
다음 조건에서, function $$f$$ 는 quasiconvex이자 quasiconcave, 즉 quasilinear이다.<br>
>$$f(x) = \frac{a^Tx+b}{c^Tx+d} $$ with $$dom$$ $$f =$$ {$$x \mid c^Tx + d > 0$$}<br>



#### Distance ratio function
$$a, b \in R^n$$이고, function $$f$$를 다음과 같이 정의할 때,즉, x와 a 간의 유클리디안 거리와 x와 b 간의 유클리디안 거리의 비율을 나타내는 function $$f$$에서,
$$f$$는 halfspace {$$x \mid \parallel x - a \parallel_2 \leq \parallel x - b \parallel_2 $$} 상에서 quasiconvex이다.

> $$f(x) = \frac{ \parallel x - a \parallel_2 }{ \parallel x - b \parallel_2 } $$<br>


$$\alpha \leq 1$$ 조건에서, 이는 유클리디안 ball 형태의 convex set이 되므로 $$f$$는 quasiconvex가 된다.