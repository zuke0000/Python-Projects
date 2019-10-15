import sys
import math
d = int(512)
f = float(1595.1680010754388)
s = str('Hello, World')

print ("e = %14d" % d) # Push d forward 14 spaces
print ("e = %-14d" % d)

print ("e = %14.2f" % f) # push forward and print 2 decimal numbers
print ("e = %.7f" % f) # print any number before decial and 7 after decimal

print ("e = %14s" % s) # Print last letters of string
print ("e = %-14.3s" % s) # Print first 5 letters of string
