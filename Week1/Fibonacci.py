x = int(input())
x1, x2 = 0, 1
count = 0
#
if 1 <= x <= 30:
   while count <= x:
      if count == x:
         print(x1)
         break
      else:
         soThuN = x1 + x2
         x1 = x2
         x2 = soThuN
         count += 1
else:
   print("So " + str(x) + " khong nam trong khoang [1,30].")
