import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1], "r")
    print(f)
    print(sys.argv)
    print("here")
else:
    f = sys.stdin
    print("else")
    print(sys.argv)

    