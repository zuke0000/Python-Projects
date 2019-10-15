import sys
import math
import random


n = int(sys.argv[1])
x = int(sys.argv[2])
i = int(sys.argv[3])
j = int(sys.argv[4])

numbers = (sorted(random.sample(range(1, x), n)))

print (numbers)
print (numbers[i-1])
while i < j:
	print (numbers[i])
	i += 1