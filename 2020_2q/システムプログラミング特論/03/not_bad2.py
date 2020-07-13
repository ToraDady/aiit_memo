# coding: utf-8


def not_bad(s):

    not_index = s.find('not')
    bad_index = s.find('bad')
    if not_index >= 0 and not_index < bad_index:
        return s.replace(s[not_index: bad_index + len('bad')], 'good')
    else:
        return s


print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad!'))
print(not_bad('This tea is not hot'))
print(not_bad("It's bad yet not"))
