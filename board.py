import random
import time
import copy
import LED_display as LMD
import print_dot as pd

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
            [9,0,2,0,2,0,2,0,2,0,2,5,9],
            [9,9,9,9,9,9,9,9,9,9,9,9,9]]
    return board

def board_print(board):
    #보드 출력 (일단 터미널에서)
    #벽은 네모, 플레이어는 '우선' 플레이어 1 2 구분하지 않고 X로 표기했다.
    
    #터미널 출력
    '''
    for y in board:
        for x in y:
            if x == 0: print(" ", end = (""))
            elif x == 1: print("X", end = (""))
            elif x == 2: print("□", end = (""))
            elif x == 3: print("■", end = (""))
            elif x == 4: print("M", end = (""))
            elif x == 5: print("Z", end = (""))
            elif x == 9: print("■", end = (""))
            else: print("▩", end = (""))
        print()
    '''
    
    #led 출력
    LMD.clear_pixel()
    for x in range(13):
         for y in range(13):
            color = board[y][x]
            if (color != 2 and color != 3):
                if color == 1:
                    LMD.set_pixel(x+1, y+1, 3)
                else:
                    LMD.set_pixel(x+1, y+1, color)

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
        time.sleep(.3)
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
        if board[i][j]==1 or board[i][j]==5: #캐릭터의 위치와 겹치면 안됨
            continue
        elif (i==1 and j==1) or (i==11 and j==11): # 플레이어 1,2 시작지점 배제 
            continue
        else:
            board[i][j]=4
            break 

def random_dice(player_n):
    while True:
        if player_n == 1:
            pd.P1_roll()
        else:
            pd.P2_roll()
         
        a= input("주사위를 굴리시오(enter를 입력하시오)\n")
        if a=="":
            dice_n = random.randrange(1,5)
            return dice_n
          
        else:
            print("다시 굴리시오.\n")
            
def character_move(board, player, dice_n, P1, P2, symbol):
    #symbol에 매직 심볼 개수 플레이어수만큼 리스트, 개수 세고 승리조건 만들기
    if player == 1:
        for x in range(13):
            for y in range(13):
                if board[x][y]==1:
                    a=x
                    b=y
                    
    else:
        for x in range(13):
            for y in range(13):
                if board[x][y]==5:
                    a=x
                    b=y
    
    crash = False
    for i in range(dice_n):
        if crash == True:
            print("cracked wall~\n")
            pd.printcrash()
            time.sleep(1)
            crash = False
            break
        while True:
            #적절한 break문으로 dice 소모 조건 계산
            board_print(board)
            if player == 1:
                pd.P1_turn(dice_n-i)
                pd.symbol(symbol[0])
                print("\nP1 %s, 남은 움직임 %d번, 보유한 매직 심볼 %d개" %(P1, dice_n-i, symbol[0]))
                player_number = 1
            else:
                pd.P2_turn(dice_n-i)
                pd.symbol(symbol[1])
                print("\nP2 %s, 남은 움직임 %d번, 보유한 매직 심볼 %d개" %(P2, dice_n-i, symbol[1]))
                player_number = 5

            key = input("Enter a key from [a (left), d (right), w (up) s (down)] : ")

            if key == 'a': #좌로 이동 
                board[a][b]= 0 
                b -=1
                if board[a][b]==2: #벽 유무 확인
                    b-=1
                    if board[a][b]==0:
                        board[a][b]=player_number
                        break
                    elif board[a][b]==1 or board[a][b]==5:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.\n")
                        b+=2
                        board[a][b]=player_number
                    elif board[a][b]==4:
                        pd.congrats()
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.\n")
                        board[a][b]=player_number
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    pd.show_wall(a, b)
                    if player == 1:
                        a=1
                        b=1
                        board[a][b]=1
                        crash = True
                        break
                    else:
                        a=11
                        b=11
                        board[a][b]=5
                        crash = True
                        break
                else:
                    print("갈 수 없습니다.\n")
                    b +=1
                    board[a][b]=player_number
                    

            elif key =='d': #우로 이동
                board[a][b]= 0 
                b +=1
                if board[a][b]==2: #벽 유무 확인
                    b+=1
                    if board[a][b]==0:
                        board[a][b]=player_number
                        break
                    elif board[a][b]==1 or board[a][b]==5:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.\n")
                        b-=2
                        board[a][b]=player_number
                    elif board[a][b]==4:
                        pd.congrats()
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.\n")
                        board[a][b]=player_number
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    pd.show_wall(a, b)
                    if player == 1:
                        a=1
                        b=1
                        board[a][b]=1
                        crash = True
                        break
                    else:
                        a=11
                        b=11
                        board[a][b]=5
                        crash = True
                        break
                else:
                    print("갈 수 없습니다.\n")
                    b -=1
                    board[a][b]=player_number

            elif key =='w': #위로 이동
                board[a][b]= 0 
                a -=1
                if board[a][b]==2: #벽 유무 확인
                    a-=1
                    if board[a][b]==0:
                        board[a][b]=player_number
                        break
                    elif board[a][b]==1 or board[a][b]==5:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.\n")
                        a+=2
                        board[a][b]=player_number
                    elif board[a][b]==4:
                        pd.congrats()
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.\n")
                        board[a][b]=player_number
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    pd.show_wall(a, b)
                    if player == 1:
                        a=1
                        b=1
                        board[a][b]=1
                        crash = True
                        break
                    else:
                        a=11
                        b=11
                        board[a][b]=5
                        crash = True
                        break
                else:
                    print("갈 수 없습니다.\n")
                    a +=1
                    board[a][b]=player_number

            elif key =='s': #아래로 이동
                board[a][b]= 0 
                a +=1
                if board[a][b]==2: #벽 유무 확인
                    a+=1
                    if board[a][b]==0:
                        board[a][b]=player_number
                        break
                    elif board[a][b]==1 or board[a][b]==5:
                        print("다른 플레이어와 같은 곳에 있을 수 없습니다.\n")
                        a-=2
                        board[a][b]=player_number
                    elif board[a][b]==4:
                        pd.congrats()
                        print("매직 심볼을 획득하셨습니다. 축하드립니다.\n")
                        board[a][b]=player_number
                        random_score_start(board)
                        if player == 1:
                            symbol[0] += 1
                        else:
                            symbol[1] += 1
                        break
                elif board[a][b]==3:
                    print( "갈 수 없습니다.")
                    pd.show_wall(a, b)
                    if player == 1:
                        a=1
                        b=1
                        board[a][b]=1
                        crash = True
                        break
                    else:
                        a=11
                        b=11
                        board[a][b]=5
                        crash = True
                        break
                else:
                    print("갈 수 없습니다.\n")
                    a -=1
                    board[a][b]=player_number
        if 5 in symbol:
            return symbol
    if crash == True:
        print("cracked wall~\n")
        pd.printcrash()
        time.sleep(1)
        crash = False
    return symbol
