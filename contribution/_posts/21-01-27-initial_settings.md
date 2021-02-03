---
layout: post
title: "Initial Settings"
chapter: home
order: 3
---

본 Repository의 컨텐츠들은 Jekyll을 사용하여 [Github Blog](<https://convex-optimization-for-all.github.io/>)로 호스팅됩니다. 따라서 기존 내용을 편집하거나 새로운 내용을 작성하기 위해서는 Jekyll의 디렉토리 구조 및 컨텐츠 작성 규약을 준수하여 작성해야 합니다. 또한 local 환경에서 변경 사항이 반영되었는지 확인하는 과정이 필요합니다. 

Github와 Jekyll과 관련하여 익숙하지 않으신 분들을 위해 간단한 환경 설정 방법을 정리해두었습니다. 작성에 어려움이 있으신 분들께서는 아래 메일로 문의주시면 도와드리겠습니다.

(우경민, wgm0601@gmail.com)

## Git Clone

컨텐츠를 수정하기 위해서는 우선 local 환경(현재 사용 중인 컴퓨터)에서 먼저 수정하고, 원하는 대로 수정이 완료되었는지 확인해야 합니다. 따라서 local에 Blog의 Source Code를 다운로드 받아야 합니다. Github에서는 이를 `Clone`이라고 합니다. Clone을 수행하는 명령어는 다음과 같습니다.

```bash
git clone https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io.git
```

Clone이 완료되면 local 환경에서 Blog의 변경 사항을 확인할 수 있도록 몇 가지 추가적인 환경 셋팅이 필요합니다.

## Install Jekyll

- [루비 설치하기](<https://jekyllrb-ko.github.io/docs/installation/>): Jekyll은 루비로 이루어져 있습니다. 따라서 Jekyll을 사용하기 위해서는 루비를 설치해야 합니다.
- [Jekyll 설치하기](<https://jekyllrb-ko.github.io/docs/>): 루비를 설치했다면 클론한 Repository에 들어가 Jekyll을 설치합니다.
- [Bundle Gem 설치하기](<https://jekyllrb-ko.github.io/docs/>): 호스팅에 필요한 루비 패키지들을 추가적으로 설치해야 해주어야 합니다. Repository의 프로젝트 디렉토리에서 다음 명령어를 실행합니다.

```bash
$ bundle install
```

## Local Hosting

- 컨텐츠를 수정했다면 Push하기 전 로컬에서 수정 내용이 잘 반영되었는지 먼저 확인해야 합니다. Jekyll에서 요구하는 규약을 지키지 않은 경우 Blog가 정상적으로 동작하지 않을 수 있고, 이러한 내용을 Push한다면 실제 웹에서 호스팅되는 Blog가 동작하지 않을 수 있습니다.
- 설치가 완료되었다면 프로젝트 디렉토리에서 다음 명령어를 실행하여 Local Server에 띄울 수 있습니다.

```
$ jekyll serve
```

- 호스팅이 되지 않는다면 다음 명령어로도 시도해 볼 수 있습니다.

```
$ bundle exec jekyll serve
```

- 두 명령어 모두 되지 않는다면 Jekyll 환경이 제대로 설치되지 않은 것입니다.