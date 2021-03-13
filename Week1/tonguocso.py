n = int(input())

def sumOfAll(n):
    sum = 0
    x = n//2 + 1
    for i in range(1,x):
        if n % i == 0:
            sum+=i
    print(sum)

sumOfAll(n)
