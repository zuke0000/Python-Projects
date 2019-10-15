import sys
import math

t = int(sys.argv[1]) # t = number of years
p = float(sys.argv[2]) # p = principle
r = float(sys.argv[3]) # r = interest rate

rt = r * t # interest times number of years

x = math.exp(1)

y = x ** rt

interest = p * y

print("%.2f" % interest)