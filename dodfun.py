# dodfun.py
# Functions for Dungeons of Doom
# that are helpful.
from os import system, name
from random import random
from time import sleep

debug = False

def delay(seconds):
	if debug == False:
		sleep(seconds)
	return

def cls():
	if debug == False:
		if name == 'nt':
			_ = system('cls')
		else:
			_ = system('clear')
	return
	
def rnd():
	return(random())

class playerObject:
	name	= 'name'
	hp		= 1
	x		= 0
	y		= 0
	oldx	= 0
	oldy	= 0
	gold	= 500
	turnstaken	= 0
	turnsleft	= 100
	monsterskilled	= 0
	haskey			= False
	hasmap			= False
	dead			= False
	movesdepleted	= False
	
	def decHP(x):
		playerObject.hp = playerObject.hp - x
		if playerObject.hp <= 0:
			playerObject.dead = True
		return
	
	def incHP(x):
		playerObject.hp = playerObject.hp + x
		return
	
	def turnEnd():
		playerObject.turnstaken = playerObject.turnstaken + 1
		playerObject.turnsleft	= playerObject.turnsleft - 1
		if playerObject.turnsleft == 0:
			playerObject.movesdepleted = True
		return
		
	def move(c,d):
#		playerObject.turnstaken = playerObject.turnstaken + 1
#		playerObject.turnsleft	= playerObject.turnsleft - 1
		playerObject.oldx		= playerObject.x
		playerObject.oldy		= playerObject.y
		playerObject.x			= c
		playerObject.y			= d
		return

class monsterObject:
	name	= 'monster'
	hp		= 1
	hm		= 1
	dead	= False
	
	def decHP(x):
		monsterObject.hp	= monsterObject.hp - x
		if monsterObject.hp <= 0:
			dead = True
		return
