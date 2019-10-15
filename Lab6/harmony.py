import sys
import math

n = int(sys.argv[1])


factor = 2
while factor*factor <= n:
	while n % factor == 0: 
		print(str(factor) + ' ', end='')
 		n //= factor
 	factor += 1

if n > 1:
	print(n, end='')
print()
