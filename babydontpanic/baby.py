from mathler import Mathler
from typing import List

def main ():

	equation = "504/12"
	guess = "41+2+2"
	while (guess):
		if (Mathler.IsAValidSequence(guess) == 0):
			print ("There's a invalid character or sequence of characters in your guess\n")
			guess = 0
			continue
		if (Mathler.IsAValidEquation(guess) == 0):
			print ("The result of your equation must be 42!\n")
			guess = 0
			continue
		#if (Mathler.IsTheCorretEquation(guess) == 0):
		#	print ("You're correct! Thank's to play our game\n")
		#	continue
		print ("Try again\n")
		guess = 0

if __name__ == "__main__":
    main()
