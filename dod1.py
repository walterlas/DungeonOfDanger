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

monster=['Large Dragon','Hideous Ghoul','Lizard Man','Manticore','Purple Worm','Deadly Cobra',
			'Mad Elf','Clay Man','Hairy Beast','Mad Dwarf','Zombie','Berserker','Giant Scorpion',
			'Giant Cockroach','Doppleganger','Giant Fire Beetle','Giant Ant','Giant Tick',
			'Mummy','Nasty Orc','Skeleton','Troll','Gobline','Vampire Bat','Creeping Blob',
			'Mad Dog','Large Spider','Black Cat','Man Eating Plant','Hydra','Gelatinous Cube',
			'Giant Centipede','Giant Rat','Shadow']
monsterhp=[6,5,4,6,6,5,5,4,5,4,4,5,6,4,5,1,1,2,3,2,1,3,3,3,3,2,3,2,1,3,2,1,2,2]
monsterhm=[12,10,8,12,12,10,10,8,10,8,8,10,12,8,10,2,2,4,6,4,2,6,6,6,4,6,4,2,6,4,2,4,4]
monsterName=" "
monsterHitPower=0
monsterStrength=0

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
	print("Cautiously, you walk towards the sound.")
	w=int(rnd()*4+1)
	if hi<playerHP:
		doSomething()	# GOTO 4180
	if w==1:
		mrWizard()		# GOTO 5040
	if w==2:
		giantSpider()	# GOTO 5170
	if (w==4) and (lvl==2):
		deepDarkPool()	# GOTO 5720
	# GOTO 5230
	return

def doAttack():		# Line 4600
	print(" ")
	print(f'You attack the {monsterName} with a swing of your sword!')
	n=int(rnd()*5+1)+int(rnd()*ca/2+1) # WTF is ca?
	monsterStrength = monsterStrength - n
	if monsterStrength <=0:		# killed the monster
		monsterDead()			# GOTO 4890
	print(f'You do {n} hit points of damage!')
	print(" ")
	print(f'It has {monsterStrength} hit points left.')
	
def monsterAttack():	# Line 4780
	return

def askFight():		# Line 4510
	print(" ")
	w=int(rnd()*4+1)
	if w<=2:
		return		# Goto 4540
	else:
		monsterAttacks()	# GOSUb 4780
	if h1<=0:
		return
	print("\nWill you (F)ight or (R)un? ")
	pc=str(input(">"))
	if upper(pc)=="F":
		doAttack()		# GOTO 4600
		monsterAttack()	# GOSUB 4780
		return			# Should go back to 4540
	if upper(pc)=="R":
		doFlee()		# GOTO 4700
	# go back to h1<=0 (line 4540)
	
	
def chamberLurking():	# Line 3600
	global monsterName
	global monsterHitPower
	global monsterStrength
	
	w=int(rnd()*15+1)+15
	monsterName=monster[w]
	monsterHitPower=monsterhp[w]
	monsterStrength=monsterhm[w]
	
	print(" ")
	print("There is something lurking...")
	print("... In this chamber...")
	print(".... Beware!")
	print(f'It is a {monsterName}!')
	askFight()	# Goto 4510
	
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
if lvl==1:			# Line 1100
	location=tools.getIndex(c,d,9)
	inta=b[location]
else:
	location=tools.getIndex(c,d,9)
	inta=a[location]
if inta==1:
	emptyChamber()	# Gosub 2100
if inta==2:
	hiddenCavern()	# Gosub 4060
if inta==3:			# Gosub 3580
	if aSomething==4:	
		chamberLurking()	# Goto 3600
quit()
