def match_ends(li):
    count = 0
    for i in li:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1

    return count


print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))
