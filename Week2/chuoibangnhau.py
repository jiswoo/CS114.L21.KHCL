q = int(input())
for i in range (0, q):
    a = list(input())
    b = list(input())
    temp = 0
    for j in range(0, len(a)):
        for k in range(0, len(b)):
            if a[j] == b[k]:
                temp += 1
    if temp != 0:
        print('YES')
    else:
        print('NO')
