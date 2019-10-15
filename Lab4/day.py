import sys
import math

m = int(sys.argv[1]) # MONTH
d = int(sys.argv[2]) # DAY
y = int(sys.argv[3])  # YEAR


y0 = int(( y - ((0) / 12))+.5)
x  = int( y0 + y0/4 - y0/100 + y0/400) 
m0 = int(m + 12 * ((0) / 12) - 2)
d0 = int((d + x + (31*m0)/ 12)) % 7



if d0 == 1 :
	print ("Monday")
if d0 == 2 :
	print ("Tuesday")
if d0 == 3 :
	print ("Wednesday")
if d0 == 4 :
	print ("Thursday")
if d0 == 5 :
	print ("Friday")
if d0 == 6 :
	print ("Saturday")
if d0 == 0 :
	print ("Sunday")

