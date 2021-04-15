from sys import stdout, stdin
arr = {}
while 1:
    a = stdin.readline().split()
    if len(a) == 0:
        quit(0)
    if a[0] == '0':
        quit(0)
    if a[0] == '1':
        arr[a[1]] = 1
    elif a[0] == '2':
        if a[1] in arr:
            stdout.write('1\n')
        else:
            stdout.write('0\n')
    else:
        arr.pop(a[1], None)
