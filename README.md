# 오픈소스기초설계(나) 8팀

2020 오픈소스기초설계 수업 프로젝트 - osscap2020

## 팀 구성원

- **팀장 [정재윤](http://www.github.com/lastdefiance20)**
> 전체적인 게임 환경 구성을 맡음, LED_display.py, board.py, print_dot.py를 주로 다룸   
>> 보드게임 보드를 코드로 구성하고 터미널 및 led matrix로 보드 출력을 구현   
플레이어 움직임에 의해서 발생하는 이벤트에 따른 반응을 구현   
플레이어의 움직임을 2인용으로 개조하여 두명이 움직일 수 있도록 구현   
랜덤으로 벽을 세우고 벽이 막히지 않았는지 조사하고 판을 구성하는 알고리즘을 구현   
led matrix에 메인 메뉴 출력을 구현   

- **팀원 [박정은](http://www.github.com/parkjungeun1013)**
> 전체적인 인터페이스 및 유저 친화 UI / UX를 맡음, run.py, dot.py, print_dot.py를 주로 다룸   
>> 메인 메뉴와 score.txt를 이용한 리더보드 저장 구현   
키보드 입력에 따른 플레이어의 움직임과 랜덤 주사위를 구현   
랜덤으로 매직 심볼 배치 및 먹었을때 이펙트를 구현   
승리 조건 충족에 따른 승리자 출력 및 리더보드 저장 구현   
led matrix에 주사위 개수, 매직심볼 개수, 현재 플레이어 출력을 구현   


## 참고한 오픈 소스
교수님의 pytet_v0.2_led 및 [adafruit 공식 홈페이지](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/experimental-python-code) 코드를 이용하여 led matrix 출력을 참고함

[quoridor 보드게임](https://github.com/alainrinder/quoridor.py) 에서 보드게임을 구현하는 방법 및 이동 등 많은 점을 참고함

[led matrix 레트로 게임](https://github.com/zcqsntr/retro_matrix) 에서 프로그램 구성을 참고함

## 프로젝트 개요
* 마법의 미로라는 보드게임의 세팅을 자동화한 보드게임이다.
* 파이썬으로 구현되었으며, 기본적으로 라즈베리 파이 led matrix에 출력된다.

* [최종 프로젝트 제안서](./Project%20proposal_team%208%20-%20ver2.pdf)

## 프로젝트 마무리
* [결과 리포트 PPT](./최종%20레포트%20PPT.pdf)
10매분량 (2020-12-03 완성)
* [유튜브 동작 영상] https://youtu.be/iZeQtXdPZCw
3분이내 (2020-12-02 완성)
* 코드들 (전부 완성)

**2020-12-03 오후 12시 40분 프로젝트 마감**

## 구성된 코드 및 파일들

- run.py - 메인으로 돌리는 코드로 옵션 선택과 리더보드 저장 등이 구현됨
- board.py - 보드 알고리즘 관련 코드
- dot.py - 라즈베리파이 출력에 필요한 도트 만들어주는 코드
- print_dot.py - 도트를 출력해주는 함수가 들어있는 코드
- LED_display.py - led 디스플레이 세팅 및 클리어가 가능한 코드
- score.txt - 각 대전기록이 기록된 txt 파일

## 준비물

준비물로는 라즈베리파이, 32 * 16 led matrix, 키보드, 모니터가 필요하다.

또한 python3가 설치되어 있어야 한다.

**f you did not install python3, try this or search how to install python3**

```
$ sudo apt-get install python3
```

## 설치 및 실행방법

First, clone the code and move to the file:

```
$ git clone https://github.com/lastdefiance20/osscap2020.git
$ cd osscap2020
```

Second, run the code using python and enjoy the game!

```
$ python3 run.py
```

## 게임을 즐기는 방법

### <선택창>

#### 1번: 게임시작, 2번: 게임룰 간단설명, 3번: 리더보드, 4번: 종료, 5번 페이지 이동

> 게임을 하려면 1번을 누르고 P1 이름, P2이름을 차례대로 터미널에 입력한다. 이후 난이도 선택창이 나오는데 1,2,3 중에서 선택하여 입력하면 된다. 입력한 난이도에 따라서 벽이 15, 18, 21개 보이지 않게 생성되고 게임이 시작된다.

> 룰을 보고싶으면 2번을 눌러 터미널에서 확인을 하면 된다.

> 리더보드 및 전적을 보고싶으면 3번을 눌러 터미널에서 확인한다.

> 종료하고 싶다면 4번을 눌러 프로그램을 종료한다.

> 5번을 입력하여 페이지 이동이 가능하다.


### <게임 룰>
게임 시작은 P1부터 시작한다. 두명이서 게임을 하기 때문에 서로 가장 먼 반대쪽 귀퉁이에서 게임을 시작합니다.

+ 우선 자기차례인 플레이어가 **엔터**를 눌러 주사위를 굴린다. (주사위 눈금은 1~4까지 있다)
+ 움직일 때는 **W, A, S, D**를 입력하여 주사위 수를 하나씩 소모하며 **위, 왼쪽, 아래, 오른쪽** 으로 움직인다.
  + 보이지 않는 벽에 부딪치면 3초간 벽을 보여준  **CRASH**가 뜨며 턴이 종료되고 처음 시작할 때의 시작칸으로 돌아간다.
  + 파란색 마법 심볼 칸에 도착하면 화면이 반짝이며 도착한 플레이어가 점수를 **1** 얻고 새 마법 심볼 칩이 세팅된다.
  + 외벽 혹은 다른 플레이어가 있는 칸으로 이동을 하려고 하면 아무일도 일어나지 않는다.
+ 주사위 눈금을 모두 소모하면 다음 사람이 차례를 진행합니다.

이해가 힘들다면 [마법의 미로 룰 설명영상](https://www.youtube.com/watch?v=IQlCOqgsUzA)을 보고 다시 게임 룰을 보자.

```
보이지 않는 벽을 최대한 외워 부딪히지 않고 가는 것이 중요하다
```
#### 승리조건
+ 한 사람이 **5개**의 마법 심볼을 모으면 승리 페이지가 출력되고 게임이 끝나며, 리더보드에 기록된다.
