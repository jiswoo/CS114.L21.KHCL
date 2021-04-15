n = int(input())
key = []
arr = []
result = []
result1 = []
for i in range(0,n):
    key.append(int(input()))
    arr.append(input())
for i in arr:
    x = i.split()
    t = tuple(x)
    tong = 0
    for j in t:
        tong += int(j)
    result.append(tong)  # gia tri tong dang lan luot
for z in key:
    l = z
    result1.append(l)

for i in range(0,n):
    if result[i] % result1[i] == 0:
        print(result[i] // result1[i])
    else:
        print((result[i] // result1[i]) + 1)
