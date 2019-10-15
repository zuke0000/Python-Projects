import sys
import math

year = int(sys.argv[1])
isLeapYear = (year % 4 == 0) and (year % 100 != 0) or  (year % 400 == 0)
print(isLeapYear)

