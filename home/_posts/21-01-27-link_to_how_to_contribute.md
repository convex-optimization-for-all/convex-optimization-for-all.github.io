---
layout: post
title: contents
chapter: home
order: "02"
owner: kyeongminwoo
---

## 오픈소스 참여가이드

{% assign posts = site.categories.contribution | sort: "order" %}
{% for post in posts %}
  <li><a href="{{ post.url }}"> {{ post.order }}. {{ post.title }}</a></li>
{% endfor %}
