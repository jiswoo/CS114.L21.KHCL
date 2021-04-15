s = str(input())
s1 = str(input())
def reverse_string1(s):
    return s[::-1]
s2 = reverse_string1(s)
if s1 == s2:
    print('YES')
else:
    print('NO')
