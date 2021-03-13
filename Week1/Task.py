n = int(input())
k = int(input())
p = int(input())
q = int(input())

k1 = (p - 1) * 2 + q
result1 = k1 - k
result2 = k1 + k
#print(k1)
if (result1 <= 0 and result2 >n) or k == n:
    print(-1)
else:
    if result1 > 0:
        p1 = (result1 - 1) // 2 + 1
        q1 = (result1 - 1) % 2 + 1
        print(str(p1) + " " + str(q1))
    else:
        p1 = (result2 - 1) // 2 + 1
        q1 = (result2 - 1) % 2 + 1
        print(str(p1)+" "+str(q1))
