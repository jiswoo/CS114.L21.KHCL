from decimal import *

getcontext().prec = 6

n = float(input())

c = (5/9)*(n - 32)

k = 273.15 + c

c = Decimal(c)
k = Decimal(k)

print(c.normalize(), k.normalize())
