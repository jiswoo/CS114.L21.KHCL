from sys import stdin, stdout
from bisect import bisect_left
n = int(stdin.readline())
result = list(map(int, stdin.readline().split()))

while True:
    arr = list(map(int, stdin.readline().split()))
    if len(arr) == 0:
        break
    if arr[1] > result[-1]:
        stdout.write(str(result[-arr[0]]) + ' ')
        stdout.write(str(result[-1]) + '\n')
    elif arr[1] < result[0]:
        stdout.write(str(result[0]) + ' ')
        stdout.write(str(result[arr[0] - 1]) + '\n')
    else:
        pos = bisect_left(result, arr[1])
        i, j = pos, pos + 1
        for y in range(arr[0]):
            if i < 0:
                i, j = -1, arr[0]
                break
            if j == len(result):
                i, j = -arr[0] - 1, 0
                break
            if arr[1] - result[i] <= result[j] - arr[1]:
                i -= 1
            else:
                j += 1
        stdout.write(str(result[i + 1]) + ' ')
        stdout.write(str(result[j - 1]) + '\n')
