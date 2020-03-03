# The Dungeon of Danger (c) 1980
# Conversion in process

## Imports ##
from random import random
import tools
from os import system, name
from time import sleep
from dodfun import cls,rnd,delay
debug = False

## Classes ##
class playerObject:
	name = 'name'
	hp = 1
	gold = 500
	turnstaken = 1
	turnsleft = 10
	monsterskilled = 0
	haskey = False
	hasmap = False
	movesdepleted = False
	x = 0
	y = 0
	oldx = 0
	oldy = 0

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
			'Mummy','Nasty Orc','Skeleton','Troll','Goblin','Vampire Bat','Creeping Blob',
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
	return(retrate)

def gameWon():		# Line 890
	print("You found you way...")
	print("... Out of the Dungeon of Danger")
	print(" ")
	print(f'You have acquired {player.gold} gold pieces.')
	gg=player.gold + 100
	r = int ((gg*player.monsterskilled-7000+1)/player.turnstaken)
	rating = getRating(r)
	print(f'Game rating is {r} = {rating}')
	if (player.gold <= 0):
		print(f'You killed {player.monsterskilled} monsters ')
		print(f'..... in {player.turnstaken} turns.')
	else:
		print(f'You took {player.turnstaken} turns to find the way out')
		print(f'And killed {player.monsterskilled} monsters.')
	quit()
	return

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
	d=input("Enter (Y)es or (N)o:")
	dl=int(rnd()*6+1)
	if d.upper() == 'N':
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
		h=int(rnd()*6+1)*difficulty
		player.hp = player.hp - h
		print("You feel a little funny...")
		delay(4)
		if player.hp <= 0:
			return
		print("\nIt was a black magic potion...")
		print(f'Which decreased your hit-points by {h}.')
	return

def somethingJumps():	# Line 5290
	cls()
	print("Suddenly... something jumps...")
	print("in front of you......")
	delay(2)
	cls()
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

def showMap():		# Line 1570
	cls()
	if (player.hasmap == False):
		print("You don't have the map.")
		delay(1)
	else:
		print("The Dungeon of Danger Map: Level "+str(level))
		print(" ")
		for q in range(1,9):
			for n in range(1,9):
				if (player.x == n) and (player.y == q):
					print("Pl ",end=" ")
					continue
				else:
					idx = tools.getIndex(n,q,9)
					s1 = a[idx]
					if s1 == 1:
#						pass()		# Line 2910
						print("O  ",end=" ")
					elif s1 == 2:
#						pass()		# Line 2970
						print("C  ",end=" ")
					elif s1 == 3:
#						pass()		# Line 2930
						print("M  ",end=" ")
					elif s1 == 4:
#						pass()		# Line 2930
						print("M  ",end=" ")
					elif s1 == 5:
#						pass()		# Line 2950
						print("?  ",end=" ")
					elif s1 == 6:
#						pass()		# Line 2990
						print("NS ",end=" ")
					elif s1 == 7:
#						pass()		# Line 3010
						print("EW ",end=" ")
					elif s1 == 8:
#						pass()		# Line 3030
						print("?  ",end=" ")
					elif s1 == 9:
#						pass()		# Line 3040
						print("UP ",end=" ")
			print("\n")
	return

def nsCorridor():	# Line 1660
	print(" ")
	cls()
	print("You are in a North-South corridor")
	print("You can only go North or South.")
	return

def ewCorridor():	# Line 1620
	cls()
	print("You are in an East-West corridor")
	print("You can only go East or West")
	return
	
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
		ewCorridor()
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
		nsCorridor()
	return

def goSouth():	# Line 1400
	if inroom == 7:
		ewCorridor()
	else:
		if (player.y+1 == 9):
			cls()
			print("You are at the South Wall")
			print("You cannot pass through.")
			print(" ")
			print("Try another direction?")
			return
		else:
			player.y = player.y + 1
	return

def goWest():	# Line 1440
	if inroom == 6:
		nsCorridor()
	else:
		if (player.x - 1) == 0:
			cls()
			print("You are at the West wall.")
			print("You cannot pass through.")
			print("\nTry another direction?")
		else:
			player.x = player.x - 1
	return
	
def goUpstairs():	# Line 1480
	cls()
	if (a != 9):
		print("You are not at a stairway.")
		delay(1)
	else:
		if player.haskey:
			level = level -1
			print("You walk up the stairway...")
			delay(1)
			print("The Enchanted Key ... Opens the lock")
			delay(1)
			if level  == 0:
				gameWon()
			else:
				player.hasmap = False
				player.haskey = False
				k4 = int(rnd()*4+1)+1
				if player.hp < hi:
					player.hp = hi
					print("You feel stronger .....")
					delay(1)
					print(f'Your hit points are restored to {hi}')
					print(" ")
					bmonsterskilled = player.monsterskilled+k4
					print("You are at..... Level 1")
					delay(2)
					return
		else:
			print("\nYou cannot go up the stairway.")
			print("You don't have the key.")
			delay(1)
	return

def flourish():
	for aa in range(1,301):
		print("*        %",end="")
	delay(2)
	cls()
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

def teleportTrap():		# Line 5560
	tl = 0
	delay(2)
	print("You reactivated the teleportation trap")
	delay(2)
	flourish()
	print("You end up back in the area where")
	print(". . . You last teleported from")
	delay(2)
	return

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
		gg=player.gold + 100
		r = int ((gg*player.monsterskilled-7000+1)/player.turnstaken)
		rating = getRating(r)
		print(f'Game rating is {r} = {rating}')
#		playerRating()
		print(" ")
		print("Another game?")
		f=input("Enter (Y)es or (N)o >")
		if f.upper() == 'Y':
			newgame = True	# Goto 210
			cls()
		else:
			quit()
	return

def intoPit():
	global pitfall
	global player
	
	print("You fell into a deep . . . pit")
	pitfall = True
	delay(1)
	print("Luckily . . you didn't get hurt")
	print(" ")
	delay(1)
	print("But in climbing out . . . ")
	player.gold = 0
	print("\nYou . . . . . . lost")
	print("all of your gold pieces")
	print(" ")
	if pitfall:
		pitfall = False
		return
	print("But . . . you still have your key")

def trapDoor():		# Line 2610
	global level
	global player
	
	print("You activated a . . . trap door")
	delay(2)
	trap = int(rnd()*4+1)*difficulty
	if trap > 4:
		print("You fell thru . . . ")
		delay(2)
		pass		# GOTO 1720
		playerDead()
		return
	elif trap == 4:
		pass		# GOTO 2690
		if level == 2:
			pass	# GOTO 2800
			intoPit()
			return
		level = level + 1
		print(" ")
		player.haskey = 1
		print("You fell thru to level 2 . . . and")
#		player.gold = 0
		delay(1)
		intoPit()
		return
	else:
		print("But . . . you caught yourself")
		print("from falling")
		return
	return
	
def getKey():		# Line 3110
	global player
	player.haskey = True
	print("\nYou look to the ground......")
	print("and find the Enchanted Key!")
	if debug:
		print(f'Has key is {player.haskey}')
	delay(2)
	return

def checkKey():		# Line 3190
	if player.monsterskilled == cb:
		getKey()	# GOTO 3110
	return

def deadMonster():	# Line 4890
	delay(2)
	print("")
	print(f'You have killed the {monster.name}')
	print("\n")
	if (inroom < 6) and (inroom != 2):
		if level == 1:
			index = tools.getIndex(player.x,player.y,9)
			b[index] = 1
		else:
			index = tools.getIndex(player.x,player.y,9)
			a[index] = 1
	gold = 500
	if inroom >= 6:
		gold = 250
	givegold = int(rnd()*gold/level+1)+75
	if inroom == 2:
		givegold=givegold*2
	player.gold = player.gold+givegold
	delay(2)
	print("You search the area....")
	delay(2)
	print(f'and find ... {givegold} gold pieces')
	player.monsterskilled = player.monsterskilled + 1
	if player.haskey != True:
		if level == 1:
			checkKey()	# GOTO 3190
		else:
			getKey()	# GOTO 3110
	return	

def monsterAttacks():	# Line 4780
	print(" ")
	w = int(rnd()*7+1)
	print(". . . . . . . It attacks you")
	if (w <= 2):
		print("But . . . . . . . .  it misses")
		delay(2)
	else:
		w = int(rnd()*6+1)
		if (w >= 3):
			n = int(rnd()*player.hp*difficulty+1)
		else:
			n = int(rnd()*player.hp/level+1)+int(rnd()*player.hp/level+1)
		if monster.hm <= 2:
			n = 1
		player.hp = player.hp - n
		delay(1)
		if player.hp <= 0:
			return
#		else:
		print(f'And it does {n} hit points of damage')
		print(" ")
		print(f'You have . . . {player.hp} hit points left')
		print(" ")
#			return
	return

def attackMonster():	# Line 4600
	cls()
	delay(1)
	print(f'You attack the . . . {monster.name}')
	delay(1)
	print("With a swing of your sword")
	n = int(rnd()*5+1)+int(rnd()*player.monsterskilled/2+1)
	monster.hm = monster.hm - n
	if monster.hm <= 0:
		deadMonster()	# GOTO 4890
		return(monster.hm)
	print(f'You do {n} hit points of damage')
	delay(1)
	print(f'It has . . {monster.hm} hit points left')
	delay(1)
	return(monster.hm)
	
def flee():		# Line 4700
	w = int(rnd()*4+1)
	player.x = player.oldx
	player.y = player.oldy
	print("You quickly run out . . .")
	if tl == 1:
		teleportTrap()	# GOTO 5560
	n = int(rnd()*2+1)
	delay(2)
	if w >= 3:
		pass	# GOTO 5330
	player.hp = player.hp - n
	print(f'As you leave . . . ')
	print(f'the {monster.name} attacks')
	delay(1)
	if player.hp <= 0:
		return
	print(f'And it does {n} hit points of damage')
	delay(2)
	return
	
def fightOrFlee():
	print(" ")
	f = input("Will you (F)ight or (R)un? ")
	return(f)
		
def doBattle():
	battleloop = True
	delay(2)
	print(" ")
	w = int(rnd()*4+1)
	if (w > 2):
		delay(1)
		monsterAttacks()	# GOSUB 4780
		if player.hp <= 0:
			return
	while battleloop:
		f = fightOrFlee()
		if f.upper() == 'F':
			check = attackMonster()
			if check <= 0:
				battleloop = False
				continue
			else:	
				monsterAttacks()
		else:
			flee()
			battleloop = False
	return
	
def doBattle2():		# Line 4530
	battle = True
	delay(2)
	w = int(rnd()*4+1)
	while battle:
		if w>2:
			monsterAttack()	# GOSUB 4780
			if player.hp <= 0:
				battle = False
		print(" ")
		f=input("Will you (F)ight or (R)un? ")
		cls()
		if f.upper() == 'F':
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
#	pausePrint()	# GOSUB 4500
	delay(2)
	print("But wait... Before you proceed")
	delay(2)
	print(" ")
	print("You hear a noise off in the distance")
	delay(2)
	print("Cautiously, you walk towards the sound.")
	delay(2)
	w=int(rnd()*4+1)
	if player.hp < initialHP and w==1:
		somethingJumps()	# GOSUB 5290
		mrWizard()			# GOTO 5040
	elif w==2:
		somethingJumps()	# GOSUB 5290
		giantSpider()		# GOTO 5170
	return

def getMap():
	print("You search the chamber and")
	delay(1)
	print("You. . . . . find a map")
	return

def thief():
	cls()
	print("There is a thief in this chamber")
	idx=tools.getIndex(player.x,player.y,9)
	if level ==1:
		b[idx] = 1
	else:
		a[idx] = 1
	delay(1)
	g4 = int(rnd()*500/level+1)
	if (player.gold - g4 < 0):
		g4 = player.gold
	y = int(rnd()*8+1)
	if y <= 3:
		print(" ")
		print("You suprised the thief . . . . ")
		delay(1)
		print("As he runs out, he drops . . . . ")
		g4 = int(rnd()*400/level+1)
		print(f'. . . {g4} gold pieces.')
		print("You pick up the gold pieces")
		player.gold = player.gold + g4
		print(" ")
		if player.hasmap:
			return
		ma = int(rnd()*4+1)
		if ma <= 2:
			player.hasmap = True
		if player.hasmap:
			getMap()
			return
	else:
		print("\n. . . . . . . . He surprises you")
		delay(2)
		print("As he quickly passes by you, he")
		print(f'snatches . . . {g4} gold pieces.\n')
		player.gold = player.gold - g4
		if player.hasmap:
			return
		else:
			ma = int(rnd()*4+1)
			if ma <= 2:
				player.hasmap = True
		if player.hasmap:
			getMap()
	return
	
def occupiedCavern():
	if inroom == 4:
		w = int(rnd()*15+1)+15
	else:
		w = int(rnd()*15+1)
		
	print(" ")
	print("There is something lurking...")
	print(".... in this chamber ....")
	delay(1)
	print("........... Beware")
	delay(1)
	print(" ")
	monster.name = monsterInfo[0][w]
	monster.hp   = monsterInfo[1][w]
	monster.hm   = monsterInfo[2][w]
	print(f'It is a ..... {monster.name} .. ')
	delay(2)
	# continue at 4510
	doBattle()
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

def showInfo():	
	print(f'Currently at X: {player.x} Y: {player.y} Level: {level}')
	print(f'Turn #: {player.turnstaken} Inroom = {inroom}')
	print(f'Monsters killed: {player.monsterskilled}')
	print("Has Map: ",end=" ")
	if player.hasmap:
		print("Yes ",end=" ")
	else:
		print("No ",end=" ")
	print("Has Key: ",end=" ")
	if player.haskey:
		print("Yes ")
	else:
		print("No " + str(player.haskey))
	return
	
## Variables ##
player = playerObject
monster = monsterObject

difficulty=1
level=3
newgame = True
onload = True
gameloop = True
pitfall = False		# originally PT

# Variables that I don't know what they do yet
tl = 0	# Might be the teleport trap
cb = 0	# I have no idea, but it's related to monsters killed?

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
		player.hp = initialHP
		delay(2)
		introBottom()
		newgame = False
	while te == 1:
#		cls()
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
			trapDoor()		# GOTO 2610
		elif inroom == 9:
			print("You are at a stairway")
			print("...... going up")
			print(" ")
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
	index = tools.getIndex(player.x,player.y,9)
	inroom = a[index]
	print(f'{player.name}, what is your action or move?')
	print(" ")
	if debug:
		showInfo()
	print("(N)orth, (E)ast, (S)outh, (W)est")
	print("(U)p, (M)ap, (G)old, (H)it Points")
	pmove = input("> ")
	player.incturn()
	t1 = 0
#	c1 = player.x
#	d1 = player.y
	player.oldx = player.x
	player.oldy = player.y
	
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
		print(f'You have {player.gold} gold pieces on you.')
	elif pmove.upper() == 'H':
		print(f'You have {player.hp} hit points left')
	elif pmove.upper() == 'Q':
		quit()
	print(" ")
	te = 1
