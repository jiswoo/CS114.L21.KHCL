s = input()
s1 = s.split()
a = int(s1[0])
b = int(s1[1])
c = a - (b % a)
if ((b // a) % 2 == 0):
    print(b % a)
else:
    print(c)
