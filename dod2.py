# The Dungeon of Danger (c) 1980
# Conversion in process

## Imports ##
from random import random
import tools
from os import system, name
from time import sleep

## Classes ##
class playerObject:
	name = 'name'
	hp = 1
	gold = 500
	turnstaken = 1
	turnsleft = 10
	monsterskilled = 0

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

## Variables ##
player = playerObject
monster = monsterObject

difficulty=1
level=3
haveKey = 0
newgame = False
dy = 0
md = 0
ma = 0
ca = 0
m1 = 0
hi = 0

## Function Declarations ##
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
# End of pausePrint():

def monsterAttack():# Line 4780
	print("\n")
	w = int(rnd()*7+1)
	print("...... It Attacks you")
	if w <= 2:		# GOTO 5350
		delay(2)
		print("But....... it misses.")
		delay(2)
	else:
		w = int(rnd()*6+1)
		if w >= 3:
			n=int(rnd()*player.hp*difficulty+1)
		else:
			n=int(rnd()*player.hp/level+1)+int(rnd()*player.hp/level+1)
		if monster.hm <= 2:
			n=1
		player.hp = player.hp -n
		delay(2)
		if player.hp <= 0:
			return
		print(f'And it does {n} hit-points of damage')
		print(" ")
		print(f'You have... {player.hp} hit-points left.')
		print(" ")
	return
# End of monsterAttack

def getKey():		# Line 3110
	haveKey == 1
	print("\nYou look to the ground......")
	print("and find the Enchanted Key!")
	delay(2)
	return
# End of getKey

def checkKey():		# Line 3190
	if ca == cb:
		getKey()	# GOTO 3110
	returnn
# End of checkKey

def deadMonster():	# Line 4890
	printDelay()
	print(f'You have killed the {monster.name}')
	print("\n")
	if (aint < 6) and (aint != 2):
		if level == 1:
			index = getIndex(c,d,9)
			b[index] = 1
		else:
			index = getIndex(c,d,9)
			a[index] = 1
	gold = 500
	if aint >= 6:
		gold = 250
	givegold = int(rnd()*gold/level+1)+75
	if aint == 2:
		givegold=givegold*2
	player.gold = player.gold+givegold
	delay(2)
	print("You search the area....")
	delay(2)
	print(f'and find ... {givegold} gold pieces')
	ca=ca+1
	if haveKey != 1:
		if level == 1:
			checkKey()	# GOTO 3190
		else:
			getKey()	# GOTO 3110
	return
#End of deadMonster

def doBattle():		# Line 4530
	battle = True
	delay(2)
	while battle:
		monsterAttack()	# GOSUB 4780
		if player.hp <= 0:
			battle = False
		print(" ")
		f=upper(input("Will you (F)ight or (R)un? "))
		cls()
		if f == 'F':
			delay(2)
			print(f'You attack the... {monster.name}')
			delay(2)
			print("With a swing of your sword")
			n=int(rnd()*5+1)+int(rnd()*ca/2+1)
			monter.hm = monster.hm - n
			if monster.hm <= 0:
				deadMonster()	# GOTO 4890
				return
			print(f'You do {n} hit-points of damage')
			print(" ")
			delay(2)
			print(f'It has.. {monster.hm} hit-points left.')
			print(" ")
			delay(2)
	return
	
def giantSpider():	# Line 5170
	monster.name = "Giant Spider"
	monster.hp = 6
	monster.hm = 12
	print("It's a huge man-sized crawling")
	print("....... SPIDER .......")
	delay(2)
	print("...... and ......")
	doBattle()		# GOTO 4530
	return
# End of giantSpider

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
	print(f'I give you... {gold} gold pieces')
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
		print(f'Which increased your hit-points by {h}')
	elif dl == 2:
		print("The liquid had no effect on you.")
	else:
		h=int(rnd(0)*6+1)*difficulty
		player.hp = player.hp - h
		print("You feel a little funny...")
		delay(4)
		if player.hp <= 0:
			return
		print("\nIt was a black magic potion...")
		print(f'Which decreased your hit-points by {h}.')
	return
# End of findVial

def flourish():
	for aa in range(1,301):
		print("*        %",end="")
	delay(2)
	cls()
	return
# End of flourish

def getRating(r):
	if r <= -400:
		retrate = "Incompetent serf"
	elif r <= -100:
		retrate = "Weakling"
	elif r < 0:
		retrate = "Apprentice"
	elif r < 100:
		retrate = "Halfling"
	elif r < 200:
		retrate = "Foot soldier"
	elif r < 600:
		retrate = "Warrior"
	elif r < 900:
		retrate = "Great warrior"
	elif r < 1500:
		retrate = "Swordsman"
	elif r < 2500:
		retrate = "Magic Swordsman"
	elif r >= 2500:
		retrate = "Dungeon Master!"
	return
#End of getRating

def playerRating():
	gg = player.gold+100
	r = int((gg*ca-7000+1)/m1)
	rating = getRating(r)	# GOSUB 5620
	print(" ")
	print(f'Game Rating Is {r} = {rating}')
	print(" ")
	if player.gold <=0:
		print(f'You killed {ca} monsters')	# GOTO 3210
		print(f'..... in {m1} turns.')
	print(f'You took {m1} turns to find the way out')
	print(f'And you killed {ca} monsters.')
	return
# End of playerRating
	
def playerDead():
	global dy
	delay(2)
	cls()
	if dy == 1:
		print(f'{player.name}, you have depleted your moves.')
	else:
		print("Your hit-points have been depleted,")
	player.gold = 0
	print("And unfortunately... You just died.")
	delay(3)
	w = int(rnd()*6+1)
	if (dy == 0) and (w >= 3):	# Line 5370
		delay(1)
		dy = 1
		player.hp = hi
		flourish()
		print("You have entered .. a zone")
		print("between .. Life and Death")
		print(" ")
		delay(1)
		print("I.... The Ancient Wizard")
		print("will restore your hit-pointes to "+str(hi))
		print("and .... You have one more")
		print("chance in the Dungeon.")
		print(" ")
		md = int(rnd()*15+1)*ca+10
		player.hp = hi
		print(f'You shall have {md} moves.')
		print("left to find your way out")
		print("of the Dungeon of Danger.")
		delay(2)
		flourish()
		return
	else:		# Kube 1710
		cls()
		print("You lost all your gold and you were")
		print("... unable to meet the demands of")
		print(".....The Dungeon of Danger")
		print("\n\n")
		print(" ")
		print("Better luck next time")
		playerRating()
		print(" ")
		print("Another game?")
		f=input("Enter (Y)es or (N)o >")
		if f.upper() == 'Y':
			newgame = True	# Goto 210
			cls()
		else:
			quit()
	return
# End of playerDead	

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
	pausePrint()	# GOSUB 4500
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
		somethingJumps()	# GOSUB 5290
		mrWizard()			# GOTO 5040
	elif w==2:
		somethingJumps()	# GOSUB 5290
		giantSpider()		# GOTO 5170
	return
	
def showIntro():
	global difficulty
	global player
	global newgame
	global dy
	global md
	global ma
	global ca
	global m1
	global haveKey
	global hi
	
	if newgame == False:
		cls()
		print("The Dungeon of Danger")
		print("Python 3")
		print("(c)1980 by Howard Berenbon")
		print("Converted to Python by me.")
		print(" ")
		print("A Fantasy Game")
		print("=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=")
		print("You will be teleported to...")
		print(" ")
	print("The Dungeon of Danger")
	print(" ")
	dy = 0
	md = 1
	difficulty = getDifficulty()		#gosub 5530
	ma = 0
	ca = 0	# monsters killed
	player.gold = 500
	m1 = 1	# turns taken
	haveKey = 0
	hi=20+int(rnd()*15+1)
	hi=int(hi/difficulty)
	player.hp=int(hi)
	player.name = getName()
	delay(2)
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

def playerAction(): # Lines 1030-1310
	c = int(rnd()*8+1)
	d = int(rnd()*8+1)
	index = tools.getIndex(c,d,9)
	a[index] = 1
	level = 2
	k4 = int(rnd()*4+1)+1
	f=" "
	cls()
	if level == 1:
		a=b[index]
	else:
		inta = a[index]
	delay(1)
	if inta == 1:
		emptyChamber()
	if inta == 2:
		hiddenCavern()
	if (inta == 3) or (inta == 4):
		occupiedCavern()
	if inta == 5:
		thief()
	if inta == 6:
		nsCorridor()
	if inta == 7:
		ewCorridor()
	if inta == 8:
		trapDoor()
	if inta == 9:
		print("You are at a stairway")
		print("...... going up")
		print(" ")
	if te == 1:
		te = 0 
		# GOTO 1070 (f$=" " above)
	print(" ")
	if player.hp <= 0:
		playerDead()	# goto 1700
	if dy == 1:
		md = md - 1
	if dy ==1 and md == 0:
		playerDead()	# goto 1700
	if f == 'R':
		pass	# goto 1070 
	print('{player.name}, what is your action or move?')
	print(" ")
	print("(N)orth, (E)ast, (S)outh, (W)est")
	print("(U)p, (M)ap, (G)old, (H)it Points")
	m1s = upper(input("> "))
	m1 = m1 + 1
	tl = 0
	c1 = c
	d1 = d
	if m1s == 'N':
		goNorth()
	if m1s == 'E':
		goEast()
	if m1s == 'S':
		goSouth()
	if m1s == 'W':
		goWest()
	if m1s == 'U':
		goUpstairs()
	if m1s == 'M':
		showMap()
	if m1s == 'G':
		checkGold()
	if m1s == 'H':
		checkHP()
	print(" ")
	# End loop and go back to Koder 399
	return

###### Main Part ######
## Consider it 1030  ##
monsterInfo=monsterSetup()
showIntro()
a=fillArray(9,9)	# Guessing it's a map?
b=fillArray(9,9)	# or a grid? 
c = int(rnd()*8+1)
d = int(rnd()*8+1)
index = tools.getIndex(c,d,9)
a[index] = 1
level = 2
k4 = int(rnd()*4+1)+1
inloop = True
te = 1
dy = 1
md = 1

while inloop:
	f=" "
	cls()
	if level == 1:
		a=b[index]
	else:
		inta = a[index]
	delay(1)
	if inta == 1:
		emptyChamber()	# Done
	if inta == 2:
		hiddenCavern()	# Done?
	if (inta == 3) or (inta == 4):
		occupiedCavern()
	if inta == 5:
		thief()
	if inta == 6:
		nsCorridor()
	if inta == 7:
		ewCorridor()
	if inta == 8:
		trapDoor()
	if inta == 9:
		upStairway()
#	if te == 1:
#		te = 0 
#		continue	# GOTO 1070 (f$=" " above)
	print(" ")
	if player.hp <= 0:
		playerDead()	# goto 1700
	if dy == 1:
		md = md - 1
		if dy ==1 and md == 0:
			playerDead()	# goto 1700
	if f == 'R':
		continue	# goto 1070 
	print('{player.name}, what is your action or move?')
	print(" ")
	print("(N)orth, (E)ast, (S)outh, (W)est")
	print("(U)p, (M)ap, (G)old, (H)it Points")
	m1s = input("> ")
	m1 = m1 + 1
	tl = 0
	c1 = c
	d1 = d
	if m1s.upper() == 'N':
		goNorth()
	if m1s.upper() == 'E':
		goEast()
	if m1s.upper() == 'S':
		goSouth()
	if m1s.upper() == 'W':
		goWest()
	if m1s.upper() == 'U':
		goUpstairs()
	if m1s.upper() == 'M':
		showMap()
	if m1s.upper == 'G':
		checkGold()
	if m1s.upper() == 'H':
		checkHP()
	print(" ")
	# End loop and go back to Koder 399
	
