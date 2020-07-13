# coding: utf-8

# これは、findメソッドに気が付かなくてやったけど、うまくいかなかった

def not_bad(s):

    a = s.split(" ")

    b = []
    for i, j in enumerate(a):
        if j == "not":
            b.append(i)

        if len(b) == 1 and j == "bad":
            b.append(i)

    if len(b) == 2:
        del a[b[0]:b[1]+1]

        return " ".join(a) + " good"
    else:
        return s


print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad!'))
print(not_bad('This tea is not hot'))
print(not_bad("It's bad yet not"))
