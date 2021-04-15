n = int(input())
for i in range(0, n):
    x = int(input())
    if x <= 2:
        print(4 - x)
    else:
        xt = x // 2
        xp = x - xt
        print(xp - xt)
