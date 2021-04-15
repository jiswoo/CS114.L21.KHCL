h, w = map(int, input().split())
result = [list(map(int, input().split())) for i in range(h)]
top, left, bottom, right = map(int, input().split())
for i in range(h):
    if (i < top) | (i > bottom):
        result[i] = [0] * w
    result[i][:left] = [0] * left
    result[i][right+1:] = [0] * (w - right - 1)
for i in range(h):
    print(*result[i])
