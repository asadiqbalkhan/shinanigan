# This is a guess the random number game
# import random function 
# Author: Asad Iqbal
# Language: python 3
# Date: 18 - June - 2017

import random
# variable to store the total guesses done by the player
guesses_taken = 0
# Display welcome message to the player
# Input required by the player at this stage to proceed
print('Hello! , What is your name player?')
pName = input('> ')
#  random.randint(x, y) function from import random
number = random.randint(1, 20)
# print message using string concatination
print('Well, ' + pName + ', I am thinking of a number between 1 and 20.')
# run while loop 6 times to give player 6 chances to guess the number
while guesses_taken < 6:
	print('Take a guess.')
	guess = input()
	guess = int(guess)
# Increment the guesses taken by player by 1 as each chance goes by
	guesses_taken = guesses_taken + 1
# Developing game logic using if statements
	if guess < number:
		print('Your guess is too low try a higher number')
	if guess > number:
		print('Your guess is too high try a lower number')
	if guess == number:
		break
	# If player wins display this message
if guess == number:
	guesses_taken = str(guesses_taken)
	print('Good Job, ' + pName +'! You guessed the number in '+ guesses_taken + ' guesses!')
	# If player loses display this message
if guess != number:
	number = str(number)
	print("You've had 6 chances to guess the number.\n The number was " + number)
