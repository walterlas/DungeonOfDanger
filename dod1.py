# The Dungeon of Danger (c) 1980
# Conversion in process
import random
import tools
from os import system

a=tools.createGrid(9,9)
b=tools.createGrid(9,9)

playerName=""
playerGold=500
playerHP=0

monster=['Large Dragon','Hideous Ghoul','Lizard Man']
monsterhp=[6,5,4]
monsterhm=[12,10,8]
difficulty=0

def rnd():
	return random.random()

def cls():
	_ = system('clear')
	return
	
def showIntro():
	global difficulty
	global playerName
	global playerHP

	cls()
	print("The Dungeon of Danger")
	print("Python 3")
	print("(c)1980 by Howard Berenbon")
	print("Converted to Python by me.")
	print(" ")
	print("A Fantasy Game")
	print("=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=")
	print("You will be teleported to... The Dungeon of Danger!")
	difficulty = getDifficulty()		#gosub 5530
	playerName = getName()
	hi=20+int(rnd()*15+1)
	hi=int(hi/difficulty)
	playerHP=hi
	print("\nYou carry a magic sword and "+str(playerGold)+" pieces with you.")
	print("Your 'hit point' value is "+str(playerHP)+".")
	print("If it reaches zero, you will die... So be careful!")
#	fillArray()							#gosub 500
	print("You have arrived at...")
	print("The Dungeon of Danger... Level 2")
	print(" ")
	print("You will encounter monsters and thieves and... gold.")
	print("Good luck!")
	return

def getDifficulty():					#subroutine at 5530
	print("Difficulty Levels: 1 = Moderate, 2 = Hard")
	n=input("Enter difficulty level > ")
	return(int(n))
# End of getDifficulty

def getName():
	n=input("Enter your character's name > ")
	return(n)
# End of getName

def fillArray(col,row):						#subroutine at 500
#	global a
#	global b
	grid=tools.createGrid(col,row)
	n=0
	for y in range(1,col):
#	for y in range(len(a[0])):
		for x in range(1,row):
#		for x in range(len(a[1])):
#			print(a)
#			print(str(x)+":"+str(y))
#			a[y][x] = int(rnd()*7+1)
#			b[y][x] = int(rnd()*7+1)
			i=tools.getIndex(x,y,col)
			grid[i]=int(rnd()*7+1)
#			grid[x][y] = int(rnd()*7+1)
		# next x
	# next y
	h=int(rnd()*3+1)
	for n in range(1,h+1):
		x=int(rnd()*col)
		y=int(rnd()*row)
#		p=int(rnd()*8+1)
#		w=int(rnd()*8+1)
#		print("x= "+str(x)+" y= "+str(y)+" p= "+str(p)+" w= "+str(w))
#		a[y][x]=8
#		b[w][p]=8
		i=tools.getIndex(x,y,col)
		grid[i]=8
	# next n
	s=int(rnd()*4+1)+2
	for n in range(1,s+1):
		x=int(rnd()*8+1)
		y=int(rnd()*8+1)
#		p=int(rnd()*8+1)
#		w=int(rnd()*8+1)
#		a[y][x]=9
#		b[w][p]=9
		i=tools.getIndex(x,y,col)
		grid[i]=9
	# next n
	return(grid)
# End of fillArray()

def emptyChamber():		# 2100-2200
	w=int(rnd()*2+1)
	if w==2:
		print("\nYou are in a damp and misty, but empty, chamber.")
	else:
		print("\nYou are in a cold and dark, but empty, chamber.")
	return

def hiddenCavern():		#4060-
	print("You stumbled onto...")
	print("A hidden cavern!")
	hiddenVial()		# Gosub 4210
	if playerHP <=0:
		return
	w=int(rnd()*9+1)
	if w>3:
		print("The cavern seems empty.")
		return
	print("But wait... before you proceed,")
	print("you hear a noise off in the distance.")
	print("Cautiously, you walk towards the sound."
	w=int(rnd()*4+1)
	if hi<playerHP:
		# GOTO 4180
	if w==1:
		# GOTO 5040
	if w==2:
		# GOTO 5170
	if (w==4) and (lvl==2):
		# GOTO 5720
	# GOTO 5230
	return
	
############ Main Loop ###########
showIntro()
a=fillArray(9,9)
b=fillArray(9,9)
c=int(rnd()*8+1)
d=int(rnd()*8+1)
location=tools.getIndex(c,d,9)
a[location]=1
lvl=2
k=int(rnd()*4+1)+1
f=" "
if lvl==1:
	location=tools.getIndex(c,d,9)
	inta=b[location]
else:
	location=tools.getIndex(c,d,9)
	inta=a[location]
if inta==1:
	emptyChamber()	# Gosub 2100
if inta==2:
	hiddenCavern()	# Gosub 4060
quit()
