f = open('small.txt', 'rU')
pat = "but"

a = f.readlines()

for i in a:
    p = i.lower().find(pat)
    if p >= 0:
        b = i.replace(i[p:3], '***' + i[p:3] + '***')
        print(b.replace('\n', ''))
    else:
        print(i.replace('\n', ''))

f.close()
