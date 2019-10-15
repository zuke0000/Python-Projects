import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

def my_min(a,b):
	minimum = min(a,b) 
	return minimum
minimumfunc = my_min(a,b)
print (minimumfunc)

def my_log2(a):
	logger = math.log2(a) 
	return logger
logfunc = my_log2(a)
print (logfunc)

def my_max(a,b):
	maximum = max(a,b) 
	return maximum
maximumfunc = my_max(a,b)
print (maximumfunc)

def my_square(my_max):
	square = (maximumfunc**2) 
	return square
squarefunc = my_square(a)
print (squarefunc)

def my_sum(a,b):
	summed = a + b
	return summed
sumfunc = my_sum(a,b)
print (sumfunc)