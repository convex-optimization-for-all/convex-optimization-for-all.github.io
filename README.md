# 모두를 위한 컨벡스 최적화

- [블로그](<https://convex-optimization-for-all.github.io/>)
- [모두를 위한 컨벡스 최적화](<https://wikidocs.net/book/1896>)

## 시작하는 글

최근 머신러닝 분야의 지속적인 발전 속에서 다양한 연구들이 진행되고 있으며, 이를 현실 문제에 빠르게 적용하려는 움직임 또한 점차 커지고 있습니다. 하지만 머신러닝의 근간을 이루는 수학에 대한 심도 높은 이해가 없다면 선행 연구와 적용 또한 피상적으로 이뤄질 수 밖에 없습니다. Convex Optimization은 그 자체만으로도 머신러닝과 직접적으로 연관이 많을 뿐더러 선형대수, 미적분학, 수치해석과 같이 수학의 다양한 하위 분야들을 포함하고 있다는 점에서 머신러닝을 공부하는 사람들에게 매력적인 학문입니다. 다만 홀로 다루기에는 내용이 적지 않을 뿐더러 학문 자체의 난이도도 높은 편이기에 함께 공부할 사람들을 모아 Convex Optimization Study를 시작하게 되었습니다. 본 Repository는 함께 진행한 Study의 흔적이자, 후에 혼자 공부하고자 하시는 분들께 도움을 드리고자 만들었습니다.

본 Repository의 주요 컨텐츠는 [모두를 위한 컨벡스 최적화](<https://wikidocs.net/book/1896>)의 저자 분들의 동의를 구해 Migration한 내용들입니다. 원 컨텐츠는 Convex Optimization에 관한 한국어 컨텐츠 중 가장 잘 알려져 있으면서 내용적으로도 부족함이 없습니다. 다만 Wiki Books로 되어 있어 이슈 관리가 어렵다는 기존 저자 분들의 의견이 있었고, 본 Repository는 기존 컨텐츠를 Open Source화 하여 이러한 아쉬움을 해소하기 위한 목적으로 제작되었습니다. 따라서 누구나 컨텐츠에 이슈를 제기하고 원한다면 PR로 수정할 수 있습니다. 이를 통해 [모두를 위한 컨벡스 최적화](<https://wikidocs.net/book/1896>) 저자분들의 뜻이기도 한 '전국민의 지적 성장과 컨벡스 최적화의 국내 대중화'에 작은 보탬이 될 수 있기를 바랍니다.

## 다루는 내용들

1. Introduction
2. Convex Sets
3. Convex Functions
4. Convex Optimization Basis
5. Canonical Problems
6. Gradient Descent
7. Subgradient
8. Subgradient Method
9. Proximal Gradient Descent and Acceleration
10. Duality in Linear Programs
11. Duality in General Programs
12. KKT Conditions
13. Duality uses and correspondences
14. Newton's Method
15. Barrier Method
16. Duality Revisited
17. Primal-Dual Interior-Point Methods
18. Quasi-Newton Methods
19. Proximal Netwon Method
20. Dual Methods
21. Alternating Direction Method of Mulipliers
22. Conditional Gradient Method
23. Coordinate Descent
24. Mixed Integer Programming 1
25. Mixed Integer Programming 2

## 만든 사람들

### Open Source Contributor

- 우경민(wgm0601@gmail.com)

### 모두를 위한 컨벡스 최적화 저자 분들

- 김기범(astroblasterr@gmail.com)
- 김정훈(placidus36@gmail.com)
- 노원종(wnoh27@naver.com)
- 박진우(www.jwpark.co.kr@gmail.com)
- 윤성진(sjyoon@gmail.com)
- 이규복(gyubokl@gmail.com)
- 한영일(thinkingtoyihan@gmail.com)
- 황혜진(brillianthhj@gmail.com)
- [저자 소개](<https://wikidocs.net/17197>)

### 모두를 위한 컨벡스 최적화 리뷰어 분들

- 이주희 (juhee1108@gmail.com)
- 장승환 (schang.math@gmail.com)
- 정태수 (tcheong@korea.ac.kr)
- [리뷰어 소개](<https://wikidocs.net/17197>)

## 작성하기 전 읽어보면 좋은 글

### Jekyll

본 Repository의 컨텐츠들은 Jekyll을 사용하여 [Github Blog](<https://convex-optimization-for-all.github.io/>)로 호스팅됩니다. 따라서 기존 내용을 편집하거나 새로운 내용을 작성하기 위해서는 Jekyll의 디렉토리 구조 및 컨텐츠 작성 규약을 준수하여 작성해야 합니다. 아래 기본적인 작성 규칙 또는 [Jekyll 공식 문서](<https://jekyllrb-ko.github.io/>)를 참고하여 작성하시면 됩니다. 이와 관련하여 작성에 어려움이 있으신 분들께서는 아래 메일로 문의주시면 도와드리겠습니다.

(우경민, wgm0601@gmail.com)

#### 시작하기

- [Repository Clone](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io>): 먼저 본 Repository를 로컬 환경에 클론합니다.
- [루비 설치하기](<https://jekyllrb-ko.github.io/docs/installation/>): Jekyll은 루비로 제작되어있습니다. 따라서 Jekyll을 사용하기 위해서는 루비를 설치해야 합니다.
- [Jekyll 설치하기](<https://jekyllrb-ko.github.io/docs/>): 루비를 설치했다면 클론한 Repository에 들어가 Jekyll을 설치합니다.
- [Bundle Gem 설치하기](<https://jekyllrb-ko.github.io/docs/>): 호스팅에 필요한 루비 패키지들을 추가적으로 설치해야 해주어야 합니다. Repository의 프로젝트 디렉토리에서 다음 명령어를 실행합니다.

`$ bundle install`

#### 로컬 호스팅

- 컨텐츠를 수정했다면 Push하기 전 로컬에서 수정 내용이 잘 반영되었는지 먼저 확인해야 합니다. Jekyll에서 요구하는 규약을 지키지 않은 경우 Blog가 정상적으로 동작하지 않을 수 있고, 이러한 내용을 Push한다면 실제 웹에서 호스팅되는 Blog가 동작하지 않을 수 있습니다.
- 설치가 완료되었다면 Repository의 프로젝트 디렉토리에서 다음 명령어를 실행하여 Local Server에 띄울 수 있다.

`$ jekyll serve`

- 호스팅이 되지 않는다면 다음 명령어로도 시도해본다.

`$ bundle exec jekyll serve`

- 두 명령어 모두 되지 않는다면 설치가 완료되지 못한 것이다.

#### Directory Convention

- 주요 컨텐츠는 `chapter`로 시작하는 디렉토리에 포함되어 있습니다. 또한 컨텐츠에 필요한 이미지는 `image` 디렉토리에 들어 있습니다.
- `chapter`의 내부 디렉토리는 다음과 같습니다.

```
chapter01
| - _posts
  | - 20-01-08-text.md
| - index.html
```

- Jekyll에서는 `_posts` 디렉토리 내에 있는 Markdown 또는 html 파일을 블로그의 Posting으로 인식합니다. 따라서 새로운 포스팅을 작성하고자 한다면 `_posts`에 새로 파일을 추가하시면 됩니다.
- Jekyll의 Posting 파일들은 모두 일정한 Naming Convention을 따릅니다. 본 Repository에서는 다음과 같이 파일 이름을 작성해주시면 됩니다.
    - `yy-mm-dd-new_posting_name.md`
- `chapter`와 `image` 디렉토리 외의 내용들은 모두 Blog 설정과 관련된 것들입니다. 안정적인 운영을 위해 이외의 부분들에 대해서는 직접 편집보다는 이슈로 작성해주시면 처리하겠습니다.

#### Posting Convention

- 모든 Posting 파일들은 다음 예시와 같은 Header를 가지고 있어야 합니다.

```
---
layout: post
title: Quasi-Newton Methods
chapter: 18
---
```

- layout은 `post`여야 합니다.
- title은 내용에 맞게 임의로 정하시면 됩니다.
- chapter는 상위 카테고리의 마지막 두 숫자로 해주시면 됩니다. 다만 한 자리 수 인 경우 "01"과 같이 표기해주어야 합니다.
- 이외의 내용들은 모두 Markdown 작성 방법에 맞춰 작성해주시면 됩니다.

### Github Convnention

작성 내용에 질문이 있거나 수정 사항을 발견하신 경우 다음 두 방법 중 하나로 남겨주시면 됩니다.

- 댓글 작성하기
- Repogitory에 이슈 생성하기

새로운 내용을 추가하거나 직접 편집하시고 싶으신 경우 먼저 수정하신 후 `Pull Request`를 생성해주시면 됩니다. 신규 작성 및 기존 내용 수정은 누구나 가능합니다.

#### Branch Naming Convention

브랜치 이름은 다음 컨벤션에 맞춰 작성해주시면 됩니다.

- `chapter01/[내용]` : Posting 관련 수정 사항
- `setting/[내용]` : Blog 설정 관련 수정 사항

## 참고한 자료들

- [Convex Optimization - Boyd and Vandenberghe](<https://web.stanford.edu/~boyd/cvxbook/>)
- [Stanford Convex Optimization Lecture 2014](<https://www.youtube.com/playlist?list=PL3940DD956CDF0622>)
- [CMU Convex Optimization Lecture 2016](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/>)
- [CMU Convex Optimization Lecture 2019](<http://www.stat.cmu.edu/~ryantibs/convexopt/>)
