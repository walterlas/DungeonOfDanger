# The Dungeon of Danger (c) 1980
# Conversion in process
from random import random
import tools
from os import system, name
from time import sleep

player=["name"],[1],[500],[0]
difficulty=1
pname=0
php=1
pgold=2
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
#	difficulty = getDifficulty()		#gosub 5530
#	player[0] = getName()
	delay(2)
	hi=20+int(rnd()*15+1)
	hi=int(hi/difficulty)
	player[1]=int(hi)
	print("\nYou carry a magic sword and "+str(player[2])+" pieces with you.")
	print("Your 'hit point' value is...",end='')
	delay(2)
	print("..."+str(player[1]),end='\n')
	print("If it reaches zero, you will die... So be careful!")
	delay(1)
	print(f'{player[0]}... You are on your way.')
	delay(5)
	clr()
	print("You have arrived at...")
	print("The Dungeon of Danger... Level 2")
	print(" ")
	print("You will encounter monsters and thieves and... gold.")
	print("Good luck!")
	return
	
monsterInfo=monsterSetup()
#print(monsterInfo)
showIntro()

