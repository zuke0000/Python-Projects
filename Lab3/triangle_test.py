import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a + b <= c or a + c <= b or c + b <= a: print("False")
else:
	print("True")
