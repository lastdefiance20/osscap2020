import time
import dot as dt
import LED_display as LMD

def menu_display(num):
    if num == 1:
        LMD.clear_pixel()
        
        for x in range(25):
             for y in range(5):
                start = dt.start()
                color = start[y][x]
                if color == 1:
                    LMD.set_pixel(x, y+2, 4)
                    
        for x in range(21):
             for y in range(5):
                start = dt.rule()
                color = start[y][x]
                if color == 1:
                    LMD.set_pixel(x, y+9, 4)
                    
        for x in range(7):
             for y in range(5):
                start = dt.right()
                color = start[y][x]
                if color == 1:
                    LMD.set_pixel(x+25, y+5, 4)
        
    else:
        LMD.clear_pixel()
        
        for x in range(25):
             for y in range(5):
                start = dt.rank()
                color = start[y][x]
                if color == 1:
                    LMD.set_pixel(x+7, y+2, 4)
                        
        for x in range(23):
             for y in range(5):
                start = dt.quit()
                color = start[y][x]
                if color == 1:
                    LMD.set_pixel(x+7, y+9, 4)
                    
        for x in range(7):
             for y in range(5):
                start = dt.left()
                color = start[y][x]
                if color == 1:
                    LMD.set_pixel(x, y+5, 4)
                    
def see_screen():
    LMD.clear_pixel()
    
    a, b = dt.see_screen()
    
    for x in range(11):
        for y in range(5):
            color = a[y][x]
            if color == 1:
                    LMD.set_pixel(x+3, y+2, 4)
    
    for x in range(25):
        for y in range(5):
            color = b[y][x]
            if color == 1:
                    LMD.set_pixel(x+3, y+9, 4)
    
def name():
	LMD.clear_pixel()
	
	for x in range (19):
		for y in range(7):
			name = dt.name()
			color = name[y][x]
			if color == 1:
				LMD.set_pixel(x+1, y+1,4)

def P1():
	for x in range(3):
		for y in range(5):
			P = dt.P()
			color = P[y][x]
			if color ==1:
				LMD.set_pixel(x+1, y+10, 4)
	
	for x in range(3):
		for y in range(5):
			one = dt.one()
			color = one[y][x]
			if color ==1:
				LMD.set_pixel(x+5, y+10,4)

	for x in range(1):
		for y in range(5):
			colon = dt.colon()
			color = colon[y][x]
			if color ==1:
				LMD.set_pixel(x+9,y+10,4)

def P2():
	for x in range(3):
		for y in range(5):
			P = dt.P()
			color = P[y][x]
			if color ==1:
				LMD.set_pixel(x+17, y+10, 4)
	
	for x in range(3):
		for y in range(5):
			two = dt.two()
			color = two[y][x]
			if color ==1:
				LMD.set_pixel(x+21, y+10,4)

	for x in range(1):
		for y in range(5):
			colon = dt.colon()
			color = colon[y][x]
			if color ==1:
				LMD.set_pixel(x+25,y+10,4)

def level():
	LMD. clear_pixel()

	for x in range(21):
		for y in range(7):
			level = dt.level()
			color = level[y][x]
			if color ==1:
				LMD.set_pixel(x+1,y+1,4)
	
	for x in range(3):
		for y in range(5):
			one = dt.one()
			color = one[y][x]
			if color ==1:
				LMD.set_pixel(x+3, y+10,4)

	for x in range(3):
		for y in range(5):
			two = dt.two()
			color = two[y][x]
			if color ==1:
				LMD.set_pixel(x+14, y+10,4)
	
	for x in range(3):
		for y in range(5):
			three= dt.three()
			color = three[y][x]
			if color ==1:
				LMD.set_pixel(x+25, y+10,4) 

def P1_win():
	LMD. clear_pixel()

	for x in range(29):
		for y in range(7):
			P1_win = dt.P1_win()
			color = P1_win[y][x]
			if color ==1:
				LMD.set_pixel(x+1,y+4,4)

def P2_win():
	LMD. clear_pixel()

	for x in range(29):
		for y in range(7):
			P2_win = dt.P2_win()
			color = P2_win[y][x]
			if color ==1:
				LMD.set_pixel(x+1,y+4,4)
				
def printcrash():
    LMD.clear_pixel()
        
    for x in range(29):
         for y in range(7):
            crash = dt.crash()
            color = crash[y][x]
            if color == 1:
                LMD.set_pixel(x+1, y+4, 4)
		
def P1_turn(n):
	for x in range(3):
		for y in range(5):
			P = dt.P()
			color = P[y][x]
			if color ==1:
				LMD.set_pixel(x+17, y+1, 3)
	
	for x in range(3):
		for y in range(5):
			one = dt.one()
			color = one[y][x]
			if color ==1:
				LMD.set_pixel(x+21, y+1,3)
	LMD.set_pixel(25,3,3) 

	if n==1:
		for x in range(6):
			for y in range(7):
				dice_1= dt.dice_1()
				color = dice_1[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7)
	if n==2:
		for x in range(6):
			for y in range(7):
				dice_2= dt.dice_2()
				color = dice_2[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7) 

	if n==3:
		for x in range(6):
			for y in range(7):
				dice_3= dt.dice_3()
				color = dice_3[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7)

	if n==4:
		for x in range(6):
			for y in range(7):
				dice_4= dt.dice_4()
				color = dice_4[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7)

def P2_turn(n):
	for x in range(3):
		for y in range(5):
			P = dt.P()
			color = P[y][x]
			if color ==1:
				LMD.set_pixel(x+17, y+1, 5)
	
	for x in range(3):
		for y in range(5):
			two = dt.two()
			color = two[y][x]
			if color ==1:
				LMD.set_pixel(x+21, y+1,5)
	LMD.set_pixel(25, 3,5)
	
	if n==1:
		for x in range(6):
			for y in range(7):
				dice_1= dt.dice_1()
				color = dice_1[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7) 
					
	if n==2:
		for x in range(6):
			for y in range(7):
				dice_2= dt.dice_2()
				color = dice_2[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7) 

	if n==3:
		for x in range(6):
			for y in range(7):
				dice_3= dt.dice_3()
				color = dice_3[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7)

	if n==4:
		for x in range(6):
			for y in range(7):
				dice_4= dt.dice_4()
				color = dice_4[y][x]
				if color ==1:
					LMD.set_pixel(x+17,y+7,6)   
				elif color ==2:
					LMD.set_pixel(x+17,y+7,7)
def symbol(n):
	if n ==0:
		for x in range(5):
			for y in range(7):
				m_0 = dt.m_0()
				color = m_0[y][x]
				if color ==1:
					LMD.set_pixel(x+25,y+7,4)
				elif color ==2:
					LMD.set_pixel(x+25,y+7,7)
	if n ==1:
		for x in range(5):
			for y in range(7):
				m_1 = dt.m_1()
				color = m_1[y][x]
				if color ==1:
					LMD.set_pixel(x+25,y+7,4)
				if color ==2:
					LMD.set_pixel(x+25,y+7,7)
	if n ==2:
		for x in range(5):
			for y in range(7):
				m_2 = dt.m_2()
				color = m_2[y][x]
				if color ==1:
					LMD.set_pixel(x+25,y+7,4)
				if color ==2:
					LMD.set_pixel(x+25,y+7,7)

	if n ==3:
		for x in range(5):
			for y in range(7):
				m_3= dt.m_3()
				color = m_3[y][x]
				if color ==1:
					LMD.set_pixel(x+25,y+7,4)
				if color ==2:
					LMD.set_pixel(x+25,y+7,7)

	if n ==4:
		for x in range(5):
			for y in range(7):
				m_4 = dt.m_4()
				color = m_4[y][x]
				if color ==1:
					LMD.set_pixel(x+25,y+7,4)
				if color ==2:
					LMD.set_pixel(x+25,y+7,7)

	if n ==5:
		for x in range(5):
			for y in range(7):
				m_5= dt.m_5()
				color = m_5[y][x]
				if color ==1:
					LMD.set_pixel(x+25,y+7,4)
				if color ==2:
					LMD.set_pixel(x+25,y+7,7)
					
def roll():
	for x in range(17):
		for y in range(5):
			roll_dice = dt.roll_dice()
			color = roll_dice[y][x]
			if color ==1:
				LMD.set_pixel(x+15,y+8,4)
def P1_roll():
	for x in range(3):
		for y in range(5):
			P = dt.P()
			color = P[y][x]
			if color ==1:
				LMD.set_pixel(x+17, y+1,3)
	
	for x in range(3):
		for y in range(5):
			one = dt.one()
			color = one[y][x]
			if color ==1:
				LMD.set_pixel(x+21, y+1,3)
	LMD.set_pixel(25,3,3)
	roll()
	
def P2_roll():
	for x in range(3):
		for y in range(5):
			P = dt.P()
			color = P[y][x]
			if color ==1:
				LMD.set_pixel(x+17, y+1, 5)
	
	for x in range(3):
		for y in range(5):
			two = dt.two()
			color = two[y][x]
			if color ==1:
				LMD.set_pixel(x+21, y+1,5)
	LMD.set_pixel(25, 3,5)
	roll()
	
def show_wall(y, x):
	LMD.set_pixel(x+1, y+1, 7)
	time.sleep(3)
	
def congrats():
    for x in range(32):
        for y in range(16):
            congrats = dt.congrats()
            color = congrats[y][x]
            if color == 1:
                LMD.set_pixel(x,y,6)
            elif color ==2:
                LMD.set_pixel(x,y,7)
            elif color ==0:
                LMD.set_pixel(x,y,8)
