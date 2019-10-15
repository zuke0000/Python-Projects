import sys
import math

i = 1000

for i in range(1000, 1200):
	while i % 5 == 0:
		print(i, i + 1, i + 2, i + 3, str(i + 4) + " " )
		i += 1
if i == 1199:
	print(str(1200) + " " )