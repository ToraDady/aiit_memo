def fast_last(s):
    if len(s) < 2:
        ret = ""
    else:
        ret = s[:2] + s[-2:]
    return ret


s1 = "Spring"
s2 = fast_last(s1)
print(s2)

s1 = "hello"
s2 = fast_last(s1)
print(s2)

s1 = "a"
s2 = fast_last(s1)
print(s2)

s1 = "abc"
s2 = fast_last(s1)
print(s2)
