# The Dungeon of Danger (c) 1980
# Conversion in process

## Imports ##
from random import random
import tools
from os import system, name
from time import sleep
from dodfun import cls,rnd,delay

## Classes ##
class playerObject:
	name = 'name'
	hp = 1
	gold = 500
	turnstaken = 1
	turnsleft = 10
	monsterskilled = 0
	havekey = 0

	def dechp(x):
		hp = hp - x
		return
	def inchp(x):
		hp = hp + x
		return
	def incturn():
		turnstaken = turnstaken + 1
		return
	def decturnleft():
		turnsleft = turnsleft -1
		return
		
class monsterObject:
	name = 'name'
	hp = 1
	hm = 1

## Functions ##

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
newgame = False
gameloop = True


##### Main Game Loop #####
while gameloop:
	dy = 0
	md = 0
	ma = 0
	hi = 0	# HP given at game start
	te = 1
	dy = 1
	md = 1
	if (newgame == False):
		introTop()
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
	
