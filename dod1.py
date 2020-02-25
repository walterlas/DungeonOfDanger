# The Dungeon of Danger (c) 1980
# Conversion in process
import random
import tools
from os import system, name

a=tools.createGrid(9,9)
b=tools.createGrid(9,9)

playerName=""
playerGold=500
playerHP=0
playerLevel=0

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
	if name == 'nt':
		_ = system('cls')
	else:
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

def emptyChamber():		# 2100-2200
	w=int(rnd()*2+1)
	if w==2:
		print("\nYou are in a damp and misty, but empty, chamber.")
	else:
		print("\nYou are in a cold and dark, but empty, chamber.")
	return

def drinkBlackPotion():
	h3=int(rnd()*6+1)*difficulty	
#	playerHP=h1-h3
	print("You feel a little funny...")
#	if playerHP <= 0:
#		return
	print("\n\nIt was a black magic potion...")
	print(f'Which decreased your hit points by {h3} points.')
	return(h3)

def drinkWhitePotion():
	h3=int(rnd()*10/difficulty+1)+(6/difficulty)
	print(f'It was a white magic potion, which increased your hit points by {h3}!')
	return(h3)
	
def hiddenVial():		# 4210
	global playerHP
	print("You look around...")
	v=int(rnd()*7+1)
	if v<=5:
		return
	print("On the ground, at your feet, is a vial.")
	print("You pick up the vial and see that it contains a milky liquid.")
	print(" ")
	print("Would you like a drink?")
	drink=str(input("Enter (Y)es or (N)o >"))
	dl=int(rnd()*6+1)
	if upper(drink) != "Y":
		return
	print("\n\n")
	print("You take a drink...")
	if dl >= 3:			# 4440
		points=drinkWhitePotion()
		playerHP=playerHP+points
		return
	if dl == 2:			# 4480
		print("The liquid has no effect on you.")
		return
	points=drinkBlackPotion()
	playerHP=playerHP-points
	return			# 4490

def somethingJumps():	# 5290
	print("Suddenly, something jumps in front of you!")
	return
	
def giantSpider():		# 5170
	somethingJumps()	# Surely this could have been done better
	hp=6
	hm=12
	print("It's a huge man-sized crawling spider!")
	print("... and ...")
	askFight()			# GOTO 4540 | Ugh. askFight needs to change
	return
	
def mrWizard():			# 5040
	global playerGold
	global playerHP
	
	somethingJumps()	# GOSUB 5290
	print("Halt! I am the Ancient Wizard!")
	print("I will not harm you.")
	print(" ")
	giveGold=int(rnd()*300+1)+100
	playerGold=playerGold+giveGold
	print(f'I give you... {giveGold} gold pieces out of goodwill and friendship.')
	print(" ")
	giveHP=int(rnd()*10/difficulty+1)+(6/difficulty)
	playerHP = playerHP + giveHP
	print(f'Also, I will increase your hit points by {giveHP}.')
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
#	if hi<playerHP:
#		doSomething()	# GOTO 4180
	if (w==1) and (hi>=playerHP):	# This should satisfy above IF
		mrWizard()		# GOTO 5040
	if w==2:			# This is 4180
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

def askFight(mname,mhp,mstr):		# Line 4510
	print(" ")
	w=int(rnd()*4+1)
	if w<=2:
		return				# Goto 4540
	else:
		monsterAttacks()	# GOSUB 4780
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
	askFight(monsterName,monsterHitPower,MonsterStrength)	# Goto 4510
	
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
