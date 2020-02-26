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

def showIntro():
	global difficulty
	global player
#	global playerName
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

