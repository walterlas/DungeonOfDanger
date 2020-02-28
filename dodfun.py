# dodfun.py
# Functions for Dungeons of Doom
# that are helpful.
from os import system, name
from random import random
from time import sleep

debug = True

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
