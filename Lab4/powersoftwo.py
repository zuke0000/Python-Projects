import sys
# Accept positive integer n as a command-line argument.
# Write to standard output a table showing the first n
# powers of two.
n = int(sys.argv[1])
power = 1
i = 0
while i <= n:
 # Write the ith power of 2.
 print(str(i) + ' ' + str(power)) 
 power *= 2 
 i = i + 1