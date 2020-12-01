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
    LMD.refresh()
    
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