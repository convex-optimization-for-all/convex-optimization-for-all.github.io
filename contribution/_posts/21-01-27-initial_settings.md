---
layout: post
title: "Initial Settings"
chapter: home
order: 1
owner: kyeongminwoo
---

본 Repository의 컨텐츠들은 Jekyll을 사용하여 [Github Blog](<https://convex-optimization-for-all.github.io/>)로 호스팅됩니다.
따라서 기존 내용을 편집하거나 새로운 내용을 작성하기 위해서는 Jekyll의 디렉토리 구조 및 컨텐츠 작성 규약을 준수하여 작성해야 합니다.
또한 로컬 환경(현재 사용 중인 컴퓨터)에서 변경 사항이 반영되었는지 웹브라우저를 통해 확인하는 과정이 필요합니다. 

GitHub 또는 Jekyll에 익숙하지 않은 분들을 위해 환경 설정 방법을 정리해두었습니다.
가이드를 따라가는 것에 어려움이 있는 분들께서는 아래 메일로 문의주시면 도와드리겠습니다.

(우경민, wgm0601@gmail.com)

## 1. Git 설치

본 블로그의 모든 작업 관리는 Git과 GitHub을 통해 수행합니다. 아래 웹사이트에 접속하여 Git을 설치해주세요.

[https://git-scm.com/downloads](https://git-scm.com/downloads)


## 2. 저장소 내려받기

블로그의 수정을 위해 터미널에 다음 명령어를 입력하여 블로그의 소스코드를 내려받습니다.

```bash
git clone https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io.git
```

## 3. 로컬 호스팅

변경 또는 수정된 컨텐츠를 블로그에 반영하기에 앞서 로컬 호스팅을 통해 작업이 의도대로 잘 수행되었는지 확인해야 합니다.
Jekyll에서 요구하는 규약을 지키지 않은 작업 내용을 저장소에 병합한다면 실제 웹에서 호스팅되는 블로그가 정상적으로 동작하지 않을 수 있기 때문입니다. 
로컬 호스팅 설정에는 가상환경(Docker)을 이용하거나 (옵션1) Jekyll 환경을 로컬에 직접 설치하는 (옵션2) 두 가지 방법들 중 임의의 한 가지를 선택하시면 됩니다.
로컬 호스팅 설정을 완료한 뒤 local server를 실행시키면 웹브라우저에서 `127.0.0.1:4000` 주소를 통해 작업한 블로그 내용을 확인할 수 있습니다.

### 3-1. (옵션1) Docker 설치

#### A. Docker 설치

Docker를 이용하여 로컬에 직접적인 환경설치 없이도 로컬 호스팅을 가능하게 합니다.
아래 웹사이트에 접속하여 Docker를 설치해주세요.

[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

#### B. 로컬 호스팅

터미널에서 저장소의 최상단(`docker-compose.yml`파일이 있는 위치)으로 이동한 뒤 다음 명령어를 입력합니다.

```bash
$ docker-compose up
```

### 3-2. (옵션2) Jekyll 환경 설치

#### A. Jekyll 및 루비 패키지 설치

- [루비 설치하기](<https://jekyllrb-ko.github.io/docs/installation/>): Jekyll은 루비로 이루어져 있습니다. 따라서 Jekyll을 사용하기 위해서는 루비를 설치해야 합니다.
- [Jekyll 설치하기](<https://jekyllrb-ko.github.io/docs/>): 루비를 설치했다면 클론한 Repository에 들어가 Jekyll을 설치합니다.
- [Bundle Gem 설치하기](<https://jekyllrb-ko.github.io/docs/>): 호스팅에 필요한 루비 패키지들을 추가적으로 설치해야 해주어야 합니다. Repository의 프로젝트 디렉토리에서 다음 명령어를 실행합니다.

```bash
$ bundle install
```

#### B. 로컬 호스팅


터미널에서 다음 명령어를 입력합니다.

```
$ jekyll serve
```

호스팅이 되지 않는다면 다음 명령어로도 시도해 볼 수 있습니다.

```
$ bundle exec jekyll serve
```

두 명령어 모두 되지 않는다면 Jekyll 환경이 제대로 설치되지 않은 것입니다.
