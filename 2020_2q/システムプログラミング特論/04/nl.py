import sys

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("Oh no, no such file or directry: " + sys.argv[1])


s = f.read()
lines = s.split('\n')

n = 1
for l in lines:
    if l != '':
        print(str(n)+' '+l)
        n += 1
    else:
        print(l)
