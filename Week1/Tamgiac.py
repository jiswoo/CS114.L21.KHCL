import math
a = float(input())
b = float(input())
c = float(input())
p = (a + b +c)/2
x = p * (p - a) * (p - b) * (p - c)
s = math.sqrt(x)
result = round(s,2)
if (a < b +c) and (b < c + a) and (c < a + b):
    if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
            print('Tam giac vuong, dien tich =',int(result))
    elif (a == b) and (b == c):
        print('Tam giac deu, dien tich =',result)
    elif (a == b) or (b == c) or (c == a):
        print('Tam giac can, dien tich =',result)
    else:
        print('Tam giac thuong, dien tich =',result)
else:
    print('Khong phai tam giac')
