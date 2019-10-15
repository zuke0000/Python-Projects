import sys
import random

stake = int(sys.argv[1]) # Amount of money
goal = int(sys.argv[2]) # Amount of money wanted
trials = int(sys.argv[3]) # amount of tries

bets = 0
wins = 0
for t in range(trials):
	cash = stake
	while cash > 0 and cash < goal:
		bets += 1
		if random.randrange(0, 2) == 0: # 50% chance of winning 
			cash += 1
		else:
			cash -= 1
	if cash == goal: 
		wins += 1

print(str(100 * wins//trials) + '% wins')
print('Avg # bets: ' + str(bets//trials))