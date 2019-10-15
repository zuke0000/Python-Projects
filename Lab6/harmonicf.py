import sys

def harmonic(n):
	total = 0.0 
	for i in range(1, n+1):
		total += 1.0 / float(i)
	return total

a = int(sys.argv[1])
b = int(sys.argv[2])

value = harmonic(a)
value2 = harmonic(b)

print(value)
print(value2)
