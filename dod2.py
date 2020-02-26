# The Dungeon of Danger (c) 1980
# Conversion in process
from random import random
import tools
from os import system, name
from time import sleep

#player=["name",1,500,0]
class playerObject:
	name = 'name'
	hp = 1
	gold = 500
player = playerObject

class monsterObject:
	name = 'name'
	hp = 1
	hm = 1
monster = monsterObject

difficulty=1
#pname=0
#php=1
#pgold=2
plevel=3

def delay(seconds):
	sleep(seconds)
	return

def cls():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	return
	
def rnd():
	return(random())

def monsterSetup():
	info=[[],[],[]]
	monster=['Large Dragon','Hideous Ghoul','Lizard Man','Manticore','Purple Worm','Deadly Cobra',
			'Mad Elf','Clay Man','Hairy Beast','Mad Dwarf','Zombie','Berserker','Giant Scorpion',
			'Giant Cockroach','Doppleganger','Giant Fire Beetle','Giant Ant','Giant Tick',
			'Mummy','Nasty Orc','Skeleton','Troll','Gobline','Vampire Bat','Creeping Blob',
			'Mad Dog','Large Spider','Black Cat','Man Eating Plant','Hydra','Gelatinous Cube',
			'Giant Centipede','Giant Rat','Shadow']
	monsterhp=[6,5,4,6,6,5,5,4,5,4,4,5,6,4,5,1,1,2,3,2,1,3,3,3,3,2,3,2,1,3,2,1,2,2]
	monsterhm=[12,10,8,12,12,10,10,8,10,8,8,10,12,8,10,2,2,4,6,4,2,6,6,6,6,4,6,4,2,6,4,2,4,4]
	monsterName=" "
	monsterHitPower=0
	monsterStrength=0
	for loop in range(0,34):
#		print(monster[loop])
		info[0].append(monster[loop])
		info[1].append(monsterhp[loop])
		info[2].append(monsterhm[loop])
#		print(f'{info[0][loop]} -- {info[1][loop]} -- {info[2][loop]}\n')
	return(info)

def fillArray(col,row):						#subroutine at 500
	grid=tools.createGrid(col,row)
	n=0
	for y in range(1,col):
		for x in range(1,row):
			i=tools.getIndex(x,y,col)
			grid[i]=int(rnd()*7+1)
		# next x
	# next y
	h=int(rnd()*3+1)
	for n in range(1,h+1):
		x=int(rnd()*col)
		y=int(rnd()*row)
		i=tools.getIndex(x,y,col)
		grid[i]=8
	# next n
	s=int(rnd()*4+1)+2
	for n in range(1,s+1):
		x=int(rnd()*8+1)
		y=int(rnd()*8+1)
		i=tools.getIndex(x,y,col)
		grid[i]=9
	# next n
	return(grid)
# End of fillArray()

def getDifficulty():					#subroutine at 5530
	print("Difficulty Levels: 1 = Moderate, 2 = Hard")
	n=input("Enter difficulty level > ")
	return(int(n))
	
# End of getDifficulty
def getName():
	n=input("Enter your character's name > ")
	return(n)
# End of getName

def pausePrint():	# Line 4500 most useless subroutine yet
	delay(3)
	print("\n")
	return
	
def emptyChamber():	# Line 2100
	w=int(rnd()*2+1)
	if w == 2:	# THEN 2160
		print("You are in a damp and misty")
		print("...... Empty chamber.")
		print("")
	else:
		print("You are in a cold and dark")
		print("...... Empty chamber.")
		print("")
	return
# End of emptyChamber

def somethingJumps():	# Line 5290
	cls()
	print("Suddenly... something jumps...")
	print("in front of you......")
	delay(2)
	cls()
	return
# End of somethingJumps

def mrWizard():	# Line 5040
		print("Halt... I am the Ancient Wizard")
		print("I will not harm you......")
		delay(4)
		print(" ")
		gold=int(rnd()*300+1)+100
		player.gold = player.gold + gold
		print(" ")
		print(f'I give you... {gold} gold pieces")
		print("Out of good will and friendship.")
		print(" ")
		hp = int(rnd()*10/difficulty+1)+(6/difficulty)
		player.hp=player.hp+hp
		print("Also, I will increase...")
		print(f'your hit-points by {hp}.')
		delay(2)
	return
# End of mrWizard()

def findVial():	# Line 4210
	print("\nYou look around...")
	delay(2)
	v=int(rnd()*7+1)
	if v < 5:
		return
	print("On the ground, at your feet, is a vial.")
	delay(2)
	print("You pick up the vial.. and see that")
	print("It contains ... a milky liquid.")
	print("Would you like a drink?")
	d=upper(input("Enter (Y)es or (N)o:"))
	dl=int(rnd()*6+1)
	if d == 'N':
		return
	print("\nYou take a drink...")
	delay(3)
	cls()
	if dl >= 3:
		h=int(rnd()*10/difficulty+1)+(6/difficulty)
		player.hp = player.hp+h
		print("It was a white magic potion...")
		print(f'Which increased your hit-points by {h}
	elif dl == 2:
		print("The liquid had no effect on you.")
	else:
		h=int(rnd(0)*6+1)*difficulty
		player.hp = player.hp - h
		print("You feel a little funny..."
		delay(4)
		if player.hp <= 0:
			return
		print("\nIt was a black magic potion...")
		print(f'Which decreased your hit-points by {h}."
	return
# End of findVial
	
def hiddenCavern():	# Line 4060
	print("You stumbled onto .....")
	print("A hidden cavern")
	delay(2)
	print(" ")
	findVial()		# GOSUB 4210
	if player.hp <= 0:
		return
	w=int(rnd()*9+1)
	delay(3)
	if w > 3:
		print("The cavern seems empty...")
		return
	delay(2)
	pausePrint():	# GOSUB 4500
	delay(2)
	print("But wait... Before you proceed")
	delay(2)
	print(" ")
	print("You hear a noise off in the distance")
	delay(2)
	print("Cautiously, you walk towards the sound.")
	delay(2)
	w=int(rnd()*4+1)
	if player.hp > hi and w==1:
		somethingJumps():	# GOSUB 5290
		mrWizard():			# GOTO 5040
		
def showIntro():
	global difficulty
	global player
#	global playerNameß
#	global playerHP

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
	player.name = getName()
	delay(2)
	hi=20+int(rnd()*15+1)
	hi=int(hi/difficulty)
	player.hp=int(hi)
	print("\nYou carry a magic sword and "+str(player.gold)+" pieces with you.")
	print("Your 'hit point' value is...",end='')
	delay(2)
	print("..."+str(player.hp),end='\n')
	print("If it reaches zero, you will die... So be careful!")
	delay(1)
	print(f'{player.name}... You are on your way.')
	delay(5)
	cls()
	print("You have arrived at...")
	print("The Dungeon of Danger... Level 2")
	print(" ")
	print("You will encounter monsters and thieves and... gold.")
	print("Good luck!")
	return	# GOTO 1030

###### Main Part ######
## Consider it 1030  ##
monsterInfo=monsterSetup()
#print(monsterInfo)
showIntro()
a=fillArray(9,9)	# Guessing it's a map?
b=fillArray(9,9)	# or a grid? 
c=int(rnd()*8+1)
d=int(rnd()*8+1)
location=tools.getIndex(c,d,9)
a[location]=1
level=2
k4=int(rnd()*4+1)+1
f=" "
cls()
if level==1:
	aint=b[location]
else:
	aint=a[location]
delay(2)

#	Line 1100 - ON GOSUB
if aint == 1:
	emptyChamber():	# to 2100
elif aint == 2:	
	hiddenCavern():	# to 4060
	
