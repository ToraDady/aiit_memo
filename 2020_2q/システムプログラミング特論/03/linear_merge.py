def linear_merge(li1, li2):
    li3 = li1 + li2
    return sorted(li3)


print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))
