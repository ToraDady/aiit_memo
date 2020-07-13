# coding: utf-8

def fix_first(s):
    f = s[0]  # ゼロ番目の要素を取得
    return f + s[1:].replace(f, "*")


print(fix_first("babble"))
print(fix_first("google"))
print(fix_first("apple"))
print(fix_first("orange"))
