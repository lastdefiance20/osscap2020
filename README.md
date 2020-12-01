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

* [마법의 미로 룰 설명영상](https://www.youtube.com/watch?v=IQlCOqgsUzA)

기본적으로 마법의 미로 보드게임을 자동화한 게임이다.

## 게임 룰
<게임 방법>
1,2,3중 선택한 난이도에 따라서 벽이 15, 18, 21개 보이지 않게 생성될 것이다.
게임 시작은 P1부터 시작한다.
우선 자기차례에 엔터를 눌러 주사위를 굴린다. (주사위 눈금은 1~4까지 있다)

이제부터는 주머니에서 뽑아 놓은 마법 심볼이 있는 칸에 가장 먼저 도착해야 합니다.
자기 차례에는 주사위를 던져나온 숫자만큼, (혹은 그보다 조금) 자기 마법사를 움직입니다.
움직일 때는 가로나 세로, 어느 방향이든 움직일 수 있고 중간에 방향을 바꿔도 됩니다.
하지만 대각선으로 가로질러 움직일 수는 없습니다.
두명이서 게임을 할 때는 서로 가장 먼 반대쪽 귀퉁이에서 게임을 시작합니다.
보이지 않는 벽에 부딪치면 처음 시작할 때의 시작칸으로 돌아갑니다.
그리고 다음 사람이 차례를 진행합니다.
마법 심볼 칸에 도착하면 도착한 플레이어가 점수를 1 얻고 새 마법 심볼 칩을 꺼냅니다.
한 사람이 5개의 마법 심볼을 모으면 게임이 끝납니다.
