---
layout: post
title: 18-05 The Broyden Class
chapter: "18"
order: 6
owner: "YoungJae Choung"
---


The Broyden class는 BFGS, DFP, SR1을 다음의 공식으로 일반화시킨다. <br>

* **Note:** $$B^+_{\text{BFGS}}$$와 $$B^+_{\text{DFP}}$$는 각각 BFGS와 DFP에 의해 유도되는 $$B^+$$다.

>$$
>B^+ = (1 - \phi)B^+\_{\text{BFGS}} + \phi B^+\_{\text{DFP}}, \text{ for } \phi \in \mathbb{R}.
>$$

$$v$$를 $$\frac{y}{y^Ts} - \frac{Bs}{s^TBs}$$로 정의하면 위 공식은 아래와 같이 정리된다.

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts} + \phi(s^TBs)vv^T.
>$$

Observe:

* $$\phi =0$$일때, 위 update는 BFGS와 동일해진다.
* $$\phi =1$$일때, 위 update는 DFP와 동일해진다.
* $$\phi = \frac{y^Ts}{y^Ts - s^TBs}$$일때, 위 update는 SR1과 동일해진다.

***참고**: $$\phi$$의 범위를 $$[0,1]$$로 제한한 특수한 경우를 restricted Broyden class라 부른다 [14]. 