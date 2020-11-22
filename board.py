import random

def board_reset():
    #벽 = 2(빈곳) 3(벽세운곳)
    #플레이어 = 0(빈곳) 1(있는곳)
    #점수 토큰 = 4(있는곳)
    #보드는 6*6 판이지만 실제로 보이지 않는 벽이 있기 때문에 세운다

    board = [[2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,1,2,0,2,0,2,0,2,0,2,0,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,0,2,0,2,0,2,0,2,0,2,0,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,0,2,0,2,0,2,0,2,0,2,0,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,0,2,0,2,0,2,0,2,0,2,0,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,0,2,0,2,0,2,0,2,0,2,0,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,0,2,0,2,0,2,0,2,0,2,0,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2]]
    return board

def board_print(board):
    #보드 출력 (일단 터미널에서)
    #벽은 네모, 플레이어는 '우선' 플레이어 1 2 구분하지 않고 X로 표기했다.
    for y in board:
        for x in y:
            if x == 0: print(" ", end = (""))
            elif x == 1: print("X", end = (""))
            elif x == 2: print("□", end = (""))
            elif x == 3: print("■", end = (""))
            elif x == 4: print("M", end = (""))
            else: print("▩", end = (""))
        print()

def random_wall(wall_num, board):
    #랜덤으로 벽세우기를 구현하자

    #벽은 3칸으로 이루어져 있다. 그러면 각 벽이 세워질 수 있는 구간을 계산하자.
    #30 세로벽
    #30 가로벽

    #왼쪽 위부터 1으로 차례대로 순서를 매긴다.
    #난이도에 따른 벽 개수만큼 중복되지 않는 숫자를 뽑아 리스트로 만든다.

    #겹치지 않도록 set를 이용해 뽑음
    while True:
        #뽑은 벽을 배치하고
        random_wall_set = set([])
        while (len(random_wall_set) < wall_num):
            random_wall_set.add(random.randint(0, 59))
        print(random_wall_set)

        #세로벽 좌표
        col_wall = []
        for y in range(1,12,2):
            for x in range(2,11,2):
                col_wall.append([y, x])

        #가로벽 좌표
        row_wall = []
        for y in range(2,11,2):
            for x in range(1,12,2):
                row_wall.append([y, x])



        for z in random_wall_set:
            if z<30:
                #세로벽
                y, x = col_wall[z]
                board[y][x] = 3

            else:
                #가로벽
                y, x = row_wall[z-30]
                board[y][x] = 3

        return board

    #뽑은 벽을 배치하고, 길이 막히는지 안막히는지 검사해야함. 길이 막히면 다시 뽑기
    #미완성

def random_score_start():
    while True:
        i = random.randrange(1,12,2)
        j = random.randrange(1,13,2)
        if board[i][j]==1: #캐릭터의 위치와 겹치면 안됨
            continue
        else:
            board[i][j]=4
            break 

def character_move():
    a=1
    b=1
    while True:
        board_print(board)
        key = input("Enter a key from [a (left), d (right), w (up) s (down)] : ")
        
        if key == 'a': #좌로 이동 
            board[a][b]= 0 
            b -=1
            if board[a][b]==2: #벽 유무 확인
                b-=1
                if board[a][b]==0:
                    board[a][b]=1
                elif board[a][b]==1:
                    print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                    b+=2
                    board[a][b]=1
                elif board[a][b]==4:
                    print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                    board[a][b]=1
                    random_score_start()
            elif board[a][b]==3:
                print( "갈 수 없습니다.")
                a=1
                b=1
                board[a][b]=1

        elif key =='d': #우로 이동
            board[a][b]= 0 
            b +=1
            if board[a][b]==2: #벽 유무 확인
                b+=1
                if board[a][b]==0:
                    board[a][b]=1
                elif board[a][b]==1:
                    print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                    b-=2
                    board[a][b]=1
                elif board[a][b]==4:
                    print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                    board[a][b]=1
                    random_score_start()
            elif board[a][b]==3:
                print( "갈 수 없습니다.")
                a=1
                b=1
                board[a][b]=1

        elif key =='w': #위로 이동
            board[a][b]= 0 
            a -=1
            if board[a][b]==2: #벽 유무 확인
                a-=1
                if board[a][b]==0:
                    board[a][b]=1
                elif board[a][b]==1:
                    print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                    a+=2
                    board[a][b]=1
                elif board[a][b]==4:
                    print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                    board[a][b]=1
                    random_score_start()
            elif board[a][b]==3:
                print( "갈 수 없습니다.")
                a=1
                b=1
                board[a][b]=1

        elif key =='s': #아래로 이동
            board[a][b]= 0 
            a +=1
            if board[a][b]==2: #벽 유무 확인
                a+=1
                if board[a][b]==0:
                    board[a][b]=1
                elif board[a][b]==1:
                    print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                    a-=2
                    board[a][b]=1
                elif board[a][b]==4:
                    print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                    board[a][b]=1
                    random_score_start()
            elif board[a][b]==3:
                print( "갈 수 없습니다.")
                a=1
                b=1
                board[a][b]=1

