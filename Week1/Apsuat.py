from decimal import *

getcontext().prec = 6

pound = float(input())

result = pound*(0.453592/(2.54*2.54))

result = Decimal(result)
print(result.normalize())
