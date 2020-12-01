import board as bd
import LED_display as LMD
import threading
import print_dot as pd
import time

#화면세팅?
def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

def print_menu():
     print("<마법의 미로>\n\n")

     print("1. Play")
     print("2. Rule")
     print("3. Ranking")
     print("4. Exit")
     print("5. swap\n")
     
     LMD.refresh()
     menu = int(input("Choose the menu: "))
     print("\n")
     return menu

def game_level():
     while 1:
          level = int(input("Choose the game level: "))
          if level == 1:
               return 15
          elif level == 2:
               return 18
          elif level == 3:
               return 21
          else:
               print("Choose the right game level!\n")
    
def run():
     LED_init()
     menu_num = 1
     while 1:
          pd.menu_display(menu_num)
          menu = print_menu()
          if menu ==1:
               pd.name()
               print("<Enter your name>\n")
               pd.P1()
               Player1= input("Player1: ")
               pd.P2()
               Player2= input("Player2: ")
               
               pd.level()
               print("\n<Game Level>\n")
               print("1. Easy")
               print("2. Normal")
               print("3. Hard\n")
               wall_num = game_level()
               print("Start\n")
               symbol = [0, 0]
               game_board = bd.board_reset()
               game_board = bd.random_wall(wall_num, game_board)
               bd.random_score_start(game_board)
               
               while True:
                    dice_n = bd.random_dice()
                    symbol = bd.character_move(game_board, 1, dice_n, Player1, Player2, symbol)
                    bd.board_print(game_board)
                    
                    if 5 in symbol:
                         break
                    dice_n = bd.random_dice()
                    symbol = bd.character_move(game_board, 2, dice_n, Player1, Player2, symbol)
                    bd.board_print(game_board)
                    
                    if 5 in symbol:
                         break
                         
               f=open("score.txt",encoding="utf-8")
               words =f.read().splitlines()
               f.close

               score= {}
               for i in range(int(len(words)/3)):
                    score[words[i*3]] = [words[i*3+1], words[i*3+2]]
                   
               if symbol[0] == 5:
                    pd.P1_win()
                    print("P1 %s win" %Player1)
                    if Player1 in score:
                         score[Player1][0]= str(int(score[Player1][0])+1)
                    else:
                         score.update( {Player1: ['1','0']})
                    if Player2 in score:
                         score[Player2][1]= str(int(score[Player2][1])+1)
                    else:
                         score.update({Player2: ['0','1']})	
                         
               elif symbol[1] == 5:
                    pd.P2_win()
                    print("P2 %s win" %Player2)
                    if Player2 in score:
                         score[Player2][0]= str(int(score[Player2][0])+1)
                    else:
                         score.update({Player2: ['1','0']})
                    if Player1 in score:
                         score[Player1][1]= str(int(score[Player1][1])+1)
                    else:
                         score.update({Player1: ['0','1']})
		 
               #score.txt갱신하기
               score_list_update= []
               fg = open("score.txt",mode="w+t",encoding="utf-8")
               for i in score.items():
                    score_list_update.append(i[0])
                    score_list_update.append(i[1][0])
                    score_list_update.append(i[1][1])
                
               fg.write("\n".join(score_list_update))
               fg.close()
               time.sleep(5)
               
          elif menu ==2:
               pd.see_screen()
               print("<게임 방법>\n")
               print("가장 최근에 길을 잃어버린 적이 있는 사람이 먼저 시작합니다.")
               print("이제부터는 주머니에서 뽑아 놓은 마법 심볼이 있는 칸에 가장 먼저 도착해야 합니다.")
               print("\n")
               print("자기 차례에는 주사위를 던져나온 숫자만큼, (혹은 그보다 조금) 자기 마법사를 움직입니다.")
               print("움직일 때는 가로나 세로, 어느 방향이든 움직일 수 있고 중간에 방향을 바꿔도 됩니다.")
               print("하지만 대각선으로 가로질러 움직일 수는 없습니다.")
               print("\n")
               print("두명이서 게임을 할 때는 서로 가장 먼 반대쪽 귀퉁이에서 게임을 시작합니다.")
               print("보이지 않는 벽에 부딪치면 처음 시작할 때의 시작칸으로 돌아갑니다.")
               print("그리고 다음 사람이 차례를 진행합니다.")
               print("마법 심볼 칸에 도착하면 주머니에서 새 마법 심볼 칩을 꺼냅니다.")
               print("\n")
               print("한 사람이 5개의 마법 심볼을 모으면 게임이 끝납니다.\n")
               time.sleep(2)

          elif menu ==3:
               pd.see_screen()
                
               f=open("score.txt",encoding="utf-8")
               words =f.read().splitlines()
               f.close

               score= {}
               for i in range(int(len(words)/3)):
                    score[words[i*3]] = [words[i*3+1], words[i*3+2]]
                
               score_list=[]
               for i in score.items():
                    rate = int(i[1][0])/(int(i[1][0])+int(i[1][1]))
                    score_list.append([i[0],rate,i[1][0],i[1][1]])
              
               for j in range(1, len(score_list)):
                    for k in range(0, len(score_list)-1):
                         if score_list[k+1][1] > score_list[k][1]:
                              score_list[k],score_list[k+1] = score_list[k+1],score_list[k]
               n=1
               print("<Ranking>\n")
               for i in score_list:
                    print("%d. %s | 승률: %.2f | Win: %s | Lose: %s" %(n, i[0],i[1],i[2],i[3]))
                    n+=1
               print("\n")
               time.sleep(2)

          elif menu ==4:
               break
                
          elif menu ==5:
               if menu_num == 1:
                    menu_num = 2
               else:
                    menu_num = 1
          else:
               print("Choose the right menu!\n")

run()
