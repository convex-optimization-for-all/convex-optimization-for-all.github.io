---
layout: post
title: contents
chapter: home
order: 2
owner: kyeongminwoo
---

## Open Source 참여 가이드

{% assign posts = site.categories.contribution | sort: "order" %}
{% for post in posts %}
  <li><a href="{{ post.url }}"> {{ post.order }}. {{ post.title }}</a></li>
{% endfor %}
