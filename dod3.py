# The Dungeon of Danger (c) 1980
# Conversion in process

## Imports ##
from random import random
import tools
from os import system, name
from time import sleep
from dodfun import cls,rnd,delay
debug = True

## Classes ##
class playerObject:
	name = 'name'
	hp = 1
	gold = 500
	turnstaken = 1
	turnsleft = 10
	monsterskilled = 0
	havekey = 0
	x = 0
	y = 0

	def dechp(x):
		hp = self.hp - x
		return
	def inchp(x):
		hp = self.hp + x
		return
	def incturn():
		playerObject.turnstaken = playerObject.turnstaken + 1
		return
	def decturnleft():
		turnsleft = turnsleft -1
		return
		
class monsterObject:
	name = 'name'
	hp = 1
	hm = 1

## Functions ##

def getDifficulty():					#subroutine at 5530
	print("Difficulty Levels: 1 = Moderate, 2 = Hard")
	n=input("Enter difficulty level > ")
	return(int(n))
	
def getName():
	n=input("Enter your character's name > ")
	return(n)
	
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
		info[0].append(monster[loop])
		info[1].append(monsterhp[loop])
		info[2].append(monsterhm[loop])
	return(info)

def goNorth():		# Line 1320
	global player
	if inroom != 7:
		if (player.y - 1) == 0:
			cls()
			print("You are at the North wall")
			print("You cannot pass through")
			print(" ")
			print("Try another direction?")
			return
#		d = d - 1
		player.y = player.y - 1
		return
	else:
		print(" ")
		cls()
		print("You are in an East-West Corridor")
		print("You can only go East or West")
	return

def goEast():		# Line 1360
	global player
	if inroom != 6:
		if (player.x + 1) == 9:
			cls()
			print("You are at the East wall")
			print("You cannot pass through")
			print(" ")
			print("Try another direction?")
			return
		player.x = player.x + 1
		return
	else:
		print(" ")
		cls()
		print("You are in an North-South Corridor")
		print("You can only go North or South")
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

def introTop():
	cls()
	print("The Dungeon of Danger")
	print("For Python 3")
	print("(c) 1980 by Howard Berenbon")
	print("Converted to Python by Me")
	print(" ")
	print("A Fantasy Game")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	print("You will be teleported to...")
	print(" ")
	return

def introMiddle():
	print("The Dungeon of Danger")
	print(" ")
	return

def introBottom():
	print(f'You carry a magic sword and {player.gold} gold pieces with you.')
	print(f'Your hit-point value is {player.hp}.')
	print("If it reaches zero, you will die... So be careful!")
	delay(1)
	print(f'{player.name}... You are on your way.')
	delay(3)
	cls()
	print("You have arrived at...")
	print("The Dungeon of Danger... Level 2")
	print(" ")
	print("You will encounter monsters and thieves and... gold.")
	print("Good luck!")
	return
	
## Variables ##
player = playerObject
monster = monsterObject

difficulty=1
level=3
newgame = True
onload = True
gameloop = True
#	dy = 0
#	md = 0
#	ma = 0
#	hi = 0	# HP given at game start
#	te = 1
#	dy = 1
#	md = 1


##### Main Game Loop #####
while gameloop:

	if (onload == True):
		introTop()
		monsterInfo = monsterSetup()
		a = fillArray(9,9)
		b = fillArray(9,9)
		
		onload = False
		
	if (newgame == True):
#		c = int(rnd()*8+1)
#		d = int(rnd()*8+1)
		player.x = int(rnd()*8+1)
		player.y = int(rnd()*8+1)
#		index = tools.getIndex(c,d,9)
		index = tools.getIndex(player.x,player.y,9)
		a[index] = 1
		level=2
		movesdepleted = 0	# dy
		md = 0
		ma = 0
		te = 1
		dy = 1
		md = 1
		f = ' '
		introMiddle()
		difficulty = getDifficulty()
		player.monsterskilled = 0
		player.gold = 500
		player.turnstaken = 1
		player.havekey = 0
		initialHP = 20*int(rnd()*15+1)
		initialHP = (initialHP/difficulty)
		player.name = getName()
		delay(2)
		introBottom()
		newgame = False
	while te == 1:
		cls()
		if level == 1:
			inroom = b[index]
		else:
			inroom = a[index]
		delay(1)
		if inroom == 1:
			emptyChamber()
		elif inroom == 2:
			hiddenCavern()
		elif (inroom == 3) or (inroom == 4):
			occupiedCavern()
		elif inroom == 5:
			thief()
		elif inroom == 6:
			nsCorridor()
		elif inroom == 7:
			ewCorridor()
		elif inroom == 8:
			trapDoor()
		elif inroom == 9:
			upStairway()
		if te == 1:
			te = 0
	print(" ")
	if player.hp <= 0:
		playerDead()
	if movesdepleted == 1:
		md = md - 1
		if (movesdepleted == 1) and (md == 0):
			playerDead()
	if f.upper() == 'R':
		continue
	print(f'{player.name}, what is your action or move?')
	print(" ")
	print("(N)orth, (E)ast, (S)outh, (W)est")
	print("(U)p, (M)ap, (G)old, (H)it Points")
	pmove = input("> ")
	player.incturn()
	t1 = 0
	c1 = player.x
	d1 = player.y
	if pmove.upper() == 'N':
		goNorth()
	elif pmove.upper() == 'E':
		goEast()
	elif pmove.upper() == 'S':
		goSouth()
	elif pmove.upper() == 'W':
		goWest()
	elif pmove.upper() == 'U':
		goUpstairs()
	elif pmove.upper() == 'M':
		showMap()
	elif pmove.upper() == 'G':
		showGold()
	elif pmove.upper() == 'H':
		showHP()
	print(" ")
	te = 1
