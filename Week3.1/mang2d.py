from sys import stdin

arr = []
r, c = stdin.readline().split()
column = [1] * int(c)
for i in range(int(r)):
    arr.append([])
    arr[i] = list(map(int, stdin.readline().split()))
    for j in range(int(c)):
        if column[j] < len(str(arr[i][j])):
            column[j] = len(str(arr[i][j]))

for i in range(int(r)):
    for j in range(int(c)):
        arr[i][j] = str(arr[i][j]).rjust(column[j])
    print(*arr[i])
