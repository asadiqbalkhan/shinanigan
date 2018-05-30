# Two import statements, in which we include random and time module

import random
import time
# first function for the introduction of the game
def displayIntro():
	print"""

		You are on a planet full of dragons. Infront of you,\n
		you see two caves. In one cave, the dragon is friendly\n
		and will share his treasure with you. The other dragon\n
		is greedy and hungry, and will eat you on sight

		"""
# defining another function 
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print 'Which cave will you go into?(1 or 2)'
		cave = input()

	return cave

def checkCave(chosenCave):
	print 'You approach the cave...'
	time.sleep(2)
	print 'It is dark and spooky...'
	time.sleep(2)
	print 'a large dragon jumpes out in front of you! he opens his jaws and...'
	time.sleep(2)

	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print 'Gives you his treasure!'
	else:
		print 'Gobbles you down in one bite!MF!'



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':

	displayIntro()

	caveNumber = chooseCave()

	checkCave(caveNumber)

	print 'Do you want to play again? (yes or no)'
	playAgain = input()