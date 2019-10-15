import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
total = a + b
diff = a - b
prod = a * b
quot = a / b
exp = a ** b

print (str(a) + ' +  ' + str(b) + ' = ' + str(total))
print (str(a) + ' -  ' + str(b) + ' = ' + str(diff))
print (str(a) + ' *  ' + str(b) + ' = ' + str(prod))
print (str(a) + ' /  ' + str(b) + ' = ' + str(quot))
print (str(a) + ' ** ' + str(b) + ' = ' + str(exp))