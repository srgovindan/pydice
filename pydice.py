# Python Dice Roller v.1.0
# Created by srgovindan, 9 June 2018.
# Thanks to RK & MK.

from __future__ import print_function
import sys
import random
import re
pat = re.compile(r'\d+[d]\d+', re.I|re.M)

def diceDiceBaby():
	# Initialize variables.
	delim_d = 'd'
	delim_plus = '+'
	dice = ''
	roll = 0
	result = 0
	print('\nWhat dice? Enter in NdX or NdX+Y format. q to quit.')
	dice = raw_input()
	# User input variables or quit with 'q'.
	while re.match(pat, dice):
		# Extract values.
		numDice, diceTemp = dice.split('d')
		if delim_plus in diceTemp:
			diceType, diceBonus = diceTemp.split('+')
		else:
			diceType = diceTemp
			diceBonus = 0
		# Calculate random dice rolls.
		for x in range(0,int(numDice)):
			roll = random.randint(1,int(diceType))
			print('Rolled a',roll)
			result = result + roll
		if diceBonus != 0:
			result = result + int(diceBonus)
		return result
		continue
	# Return error on incorrect input format or quit program on user input.
	else:
		if dice == 'q':
			print('No dice :(\n')
			sys.exit()
		print('Please enter input in NdX or NdX+Y format.')
		diceDiceBaby()

def main():
	result = diceDiceBaby()
	print ('Final value : ', result)
	main()

print('\nGot Dice?')
main()
