s = str(input())

#print(s.split(" "))
s1 = s.split((" "))
xxx = int(s1[0])
yyy = int(s1[1])

a = (4*xxx - yyy) // 2
b = xxx - a

print(a, b)
