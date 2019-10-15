import sys
import math



i = 1
while i <= 50:
 ends_in_one    = (i%10 == 1)
 ends_in_two    = (i%10 == 2) 
 ends_in_three  = (i%10 == 3)
 ends_in_eleven = (i == 11) 
 in_tens = (i%10 == 0)
 ends_in_any    = not (ends_in_one or ends_in_two or ends_in_three or ends_in_eleven or in_tens)

 if ends_in_eleven:
 	print (str(i) + 'th Hello') 
 elif ends_in_one:
 	print (str(i) + 'st Hello')

 if ends_in_two:
 	print (str(i) + 'nd Hello')
 if ends_in_three:
 	print (str(i) + 'rd Hello')
 if in_tens:
 	print (str(i) + 'th Hello')
 if ends_in_any:
 	print (str(i) + 'th Hello')

 i += 1
