import sys
import math
import random

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3]) 

m = min(a,b,c)
n = max(a,b,c)

x = [a,b,c]
y = sorted(x)[len(x) // 2]

print (m, y, n)