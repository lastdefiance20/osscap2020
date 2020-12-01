# osscap2020
2020 오픈소스기초설계 수업 프로젝트

## 팀원
* [정재윤](http://www.github.com/lastdefiance20)
* [박정은](http://www.github.com/parkjungeun1013)

## 구성된 코드 및 파일들
- run.py - 메인으로 돌리는 코드로 옵션 선택과 리더보드 저장 등이 구현됨
- board.py - 보드 알고리즘 관련 코드
- dot.py - 라즈베리파이 출력에 필요한 도트 만들어주는 코드
- print_dot.py - 도트를 출력해주는 함수가 들어있는 코드
- LED_display.py - led 디스플레이 세팅 및 클리어가 가능한 코드
- score.txt - 각 대전기록이 기록된 txt 파일

## 프로젝트 개요
* [프로젝트 개요](./Project%20proposal_team%208%20-%20ver2.pdf)

## 준비물

준비물로는 라즈베리파이, 32 * 16 led matrix, 키보드, 모니터가 필요하다. 

## 설치방법

First, clone the code and move to the file:

```
$ git clone https://github.com/lastdefiance20/osscap2020.git
$ cd osscap2020
```

Second, run the code using python and enjoy the game!

```
$ python3 run.py
```

## 사용방법

* [마법의 미로 룰 설명영상]https://www.youtube.com/watch?v=IQlCOqgsUzA

기본적으로 마법의 미로 보드게임을 자동화한 게임이다.
