import sys
import math
import random


n = int(sys.argv[1]) # Number of Decks

Number = ["Ace ", "Queen ", "King ","Joker ", "2 ", "3 ", "4 ", "5 ", "6 " , "7 ", "8 ", "9 ", "10 "]
Type = ["Spades", "Diamonds", "Hearts", "Clubs"]


while n > 0:
	i = 5
	while i > 0:
		Card = (str(random.choice(Number)) + "of " + str(random.choice(Type)))
		print (Card)
		i -= 1
	n -= 1
	if n != 0:
		print()
		print()
