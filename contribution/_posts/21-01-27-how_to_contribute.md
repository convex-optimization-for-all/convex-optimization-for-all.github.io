---
layout: post
title: "How to Contribute"
chapter: home
order: 3
owner: kyeongminwoo
---

---

## 1. 컨텐츠를 직접 수정하는 방법

#### (1) 우선 Local의 Repository Directory로 들어갑니다. Local Repository가 없다면 [Initial Settings](<https://convex-optimization-for-all.github.io/contribution/2021/01/27/initial_settings/>)를 참고하시기 바랍니다.

#### (2) Remote와 동기화하기 위해 main branch를 pull 합니다.

```
$ git pull origin main
```

#### (3) 수정 내용을 담는 새로운 브랜치를 생성합니다. 브랜치 명은 `feature/[챕터명]/[수정하는_이유]`로 하시면 됩니다.

```bash
$ git checkout -b feature/chapter01/fix_bug
```

#### (4) 파일을 편집합니다. 생성 또는 수정하고자 하는 컨텐츠는 Convention을 지켜 작성해야 합니다.

#### (5) Remote로 Push합니다.

```
$ git push origin feature/chapter01/fix_bug
```

#### (6) [Github](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/pulls>)에서 main branch로의 Pull Request를 생성합니다.

---

## 2. 컨텐츠 수정을 요청하는 방법

- Github Repository에 [Issue](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/issues>)를 생성하실 수 있습니다.

---
