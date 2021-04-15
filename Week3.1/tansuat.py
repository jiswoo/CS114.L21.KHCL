q = int(input())
result = []
for i in range(q):
    n, k = list(map(int, input().split()))
    data = list(map(int, input().split()))
    result.append(data.count(k))
for i in result:
    print(i)
