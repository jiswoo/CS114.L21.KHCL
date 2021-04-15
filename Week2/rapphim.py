#
k = list(map(int, input().split()))
m = k[0]
n = k[1]
a = k[2]
Wid = 0
Len = 0

while m > 0:
    Len += 1
    m = m - a

while n > 0:
    Wid += 1

    n -= a
print(Len * Wid)
