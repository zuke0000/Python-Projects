import sys
import math

n = int(sys.argv[1])
factor = 2
while factor**2 <= n:
	while (n % factor == 0):
		n //= factor
		print(str(factor) + ' ', end='')
		while n % factor == 0:
			n //= factor
	factor += 1
if n > 1:
	print(n, end='')
print()
