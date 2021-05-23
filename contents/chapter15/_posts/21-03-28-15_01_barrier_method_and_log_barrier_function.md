---
layout: post
title: 15-01 Barrier method and log barrier function
chapter: "15"
order: 2
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

앞 장에서 **equality constrained smooth problem**을 newton's method를 이용해서 푸는 방법을 살펴보았다. 이 장에서는 **inequality and equality constrained smooth problem**를 풀기 위한 방법을 살펴볼 것이다. 

기본 아이디어는 문제를 equality constrained smooth problem으로 변환해서 newton's method로 푸는 것이다. 이와 같은 방법을 **interior method**라고 하는데 이 장에서는 interior method 중 하나인 **barrier method**에 대해 살펴보도록 하겠다.
