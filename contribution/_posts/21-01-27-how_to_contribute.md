---
layout: post
title: "How to Contribute"
chapter: home
order: 1
owner: kyeongminwoo
---

## 컨텐츠를 직접 수정하는 방법

1. 우선 Local의 Repository Directory로 들어갑니다. Local Repository가 없다면 Initial Settings를 참고하시기 바랍니다.

2. 수정하고자 하는 chapter의 branch로 이동합니다.

```bash
$ git checkout feature/chapter01
$ git pull origin feature/chapter01
```

2-1. 만약 Loacl에 수정하고자 하는 branch가 없다면 다음 예시와 같이 새로운 branch를 생성하고 Remote로 부터 Pull 합니다.

```bash
$ git checkout -b feature/chapter01
$ git pull origin feature/chapter01
```

3. 수정 내용을 담는 새로운 브랜치를 생성합니다. 브랜치 명은 `feature/chapter01/[수정하는_이유]`로 하시면 됩니다.

```bash
$ git checkout -b feature/chapter01/fix_bug
```

4. 파일을 편집합니다. 생성 또는 수정하고자 하는 컨텐츠는 Convention을 지켜 작성해야 합니다.

5. Remote로 Push합니다.

```
$ git push origin feature/chapter01/fix_bug
```

6. [Github](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/pulls>)에서 Pull Request를 생성한다.

---

## 컨텐츠 수정을 요청하는 방법

- Github Repository에 [Issue](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/issues>)를 생성하실 수 있습니다.

---
