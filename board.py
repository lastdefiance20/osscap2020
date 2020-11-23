import random
import time
import copy

def board_reset():
    #벽 = 2(빈곳) 3(벽세운곳)
    #플레이어 = 0(빈곳) 1(P1있는곳) 5(P2있는곳?)
    #점수 토큰 = 4(있는곳)
    #보드는 6*6 판이지만 실제로 보이지 않는 벽이 있기 때문에 세운다
    #외벽 = 9

    board = [[9,9,9,9,9,9,9,9,9,9,9,9,9],
            [9,1,2,0,2,0,2,0,2,0,2,0,9],
            [9,2,2,2,2,2,2,2,2,2,2,2,9],
            [9,0,2,0,2,0,2,0,2,0,2,0,9],
            [9,2,2,2,2,2,2,2,2,2,2,2,9],
            [9,0,2,0,2,0,2,0,2,0,2,0,9],
            [9,2,2,2,2,2,2,2,2,2,2,2,9],
            [9,0,2,0,2,0,2,0,2,0,2,0,9],
            [9,2,2,2,2,2,2,2,2,2,2,2,9],
            [9,0,2,0,2,0,2,0,2,0,2,0,9],
            [9,2,2,2,2,2,2,2,2,2,2,2,9],
            [9,0,2,0,2,0,2,0,2,0,2,0,9],
            [9,9,9,9,9,9,9,9,9,9,9,9,9]]
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
            elif x == 9: print("■", end = (""))
            else: print("▩", end = (""))
        print()

def check_wall(board):
    #정말 까다로웠음,,, 탐색을 해나가는 오픈소스 참고 작성함
    #접근 가능한 바닥을 마지막에 list_A로 리턴함

    start = [(1,1)]
    list_A = [(1,1)]

    while True:
        if start == []:
            return list_A

        for i in start:
            y, x = start.pop(0)

            #위
            if board[y-1][x] != 3 and board[y-1][x] != 9:
                if not (y-2,x) in list_A:
                    list_A.append((y-2,x))
                    start.append((y-2,x))

            #아래
            if board[y+1][x] != 3 and board[y+1][x] != 9:
                if not (y+2,x) in list_A:
                    list_A.append((y+2,x))
                    start.append((y+2,x))

            #왼쪽
            if board[y][x-1] != 3 and board[y][x-1] != 9:
                if not (y,x-2) in list_A:
                    list_A.append((y,x-2))
                    start.append((y,x-2))

            #오른쪽
            if board[y][x+1] != 3 and board[y][x+1] != 9:
                if not (y,x+2) in list_A:
                    list_A.append((y,x+2))
                    start.append((y,x+2))
        
def random_wall(wall_num, board):
    #랜덤으로 벽세우기를 구현하자(목표 중 하나)

    #벽은 3칸으로 이루어져 있다. 그러면 각 벽이 세워질 수 있는 구간을 계산하자.
    #30 세로벽
    #30 가로벽

    #왼쪽 위부터 1부터 시작해서 로 차례대로 순서를 매긴다.
    
    #리스트 딥카피
    clear_board = copy.deepcopy(board)
    while True:
        #난이도에 따른 벽 개수만큼 중복되지 않는 숫자를 뽑아 리스트로 만든다.
        #겹치지 않도록 set를 이용해 뽑음
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

        #뽑은 벽을 배치하고, 길이 막히는지 안막히는지 검사해야함. 길이 막히면 다시 뽑기
        for z in random_wall_set:
            if z<30:
                #세로벽
                y, x = col_wall[z]
                board[y][x] = 3

            else:
                #가로벽
                y, x = row_wall[z-30]
                board[y][x] = 3

        #check_wall의 개수가 36이면 36칸 다 접근가능하다는 뜻이라 return
        #아니면 어딘가 접근 불가능한, 막힌 구간이 있기 때문에 다시 보드를 짠다
        time.sleep(.5)
        print("접근가능한 바닥 개수 = %d" %len(check_wall(board)))

        if len(check_wall(board)) == 36:
            #보드를 리턴해 시작한다
            return board
        else:
            #보드 벽 다 지우기
            board = copy.deepcopy(clear_board)

def random_score_start(board):
    while True:
        i = random.randrange(1,12,2)
        j = random.randrange(1,13,2)
        if board[i][j]==1: #캐릭터의 위치와 겹치면 안됨
            continue
        else:
            board[i][j]=4
            break 
            
def random_dice():
    #다이스 1~6 및 출력 구현?
            
def character_move(board, player, dice_n, P1, P2, symbol):
    #symbol에 매직 심볼 개수 플레이어수만큼 리스트, 개수 세고 승리조건 만들기
    a=1
    b=1
    for i in range(dice_n):
        while True:
            #적절한 break문으로 dice 소모 조건 계산
            board_print(board)
            
            #일단 1인부터 구현
            if player == 1:
                print("P1 %s, has symbol %d" %(P1,symbol[0]))
            #else:
                #print("P2 %s, has symbol %d" %(P2,symbol[0]))
            key = input("Enter a key from [a (left), d (right), w (up) s (down)] : ")
            
            if key == 'a': #좌로 이동 
                board[a][b]= 0 
                b -=1
                if board[a][b]==2: #벽 유무 확인
                    b-=1
                    if board[a][b]==0:
                        board[a][b]=1
                        break
                    elif board[a][b]==1:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                        b+=2
                        board[a][b]=1
                    elif board[a][b]==4:
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                        board[a][b]=1
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    a=1
                    b=1
                    board[a][b]=1
                    break
                else:
                    print("갈 수 없습니다.")
                    b +=1
                    board[a][b]=1
                    

            elif key =='d': #우로 이동
                board[a][b]= 0 
                b +=1
                if board[a][b]==2: #벽 유무 확인
                    b+=1
                    if board[a][b]==0:
                        board[a][b]=1
                        break
                    elif board[a][b]==1:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                        b-=2
                        board[a][b]=1
                    elif board[a][b]==4:
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                        board[a][b]=1
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    a=1
                    b=1
                    board[a][b]=1
                    break
                else:
                    print("갈 수 없습니다.")
                    b -=1
                    board[a][b]=1

            elif key =='w': #위로 이동
                board[a][b]= 0 
                a -=1
                if board[a][b]==2: #벽 유무 확인
                    a-=1
                    if board[a][b]==0:
                        board[a][b]=1
                        break
                    elif board[a][b]==1:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                        a+=2
                        board[a][b]=1
                    elif board[a][b]==4:
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                        board[a][b]=1
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    a=1
                    b=1
                    board[a][b]=1
                    break
                else:
                    print("갈 수 없습니다.")
                    a +=1
                    board[a][b]=1

            elif key =='s': #아래로 이동
                board[a][b]= 0 
                a +=1
                if board[a][b]==2: #벽 유무 확인
                    a+=1
                    if board[a][b]==0:
                        board[a][b]=1
                        break
                    elif board[a][b]==1:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.")
                        a-=2
                        board[a][b]=1
                    elif board[a][b]==4:
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.")
                        board[a][b]=1
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    a=1
                    b=1
                    board[a][b]=1
                    break
                else:
                    print("갈 수 없습니다.")
                    a -=1
                    board[a][b]=1
        if 5 in symbol:
            return symbol
    return symbol
