from math import gcd
n = int(input())
arr = []
def plus_fraction(x, y):
    pot=gcd(x,y)
    x1 = x //pot
    x2 = y //pot
    if (x2 != 1):
        s = str(x1)+" "+str(x2)
        return s
    else:
        return  x1
for i in range(0,n):
    arr.append(input())

#print(plus_fraction(x, y))
for i in arr:
    k = i.split()
    t = tuple(k)
    x = int(t[0])
    y = int(t[1])
    print(plus_fraction(x, y))
