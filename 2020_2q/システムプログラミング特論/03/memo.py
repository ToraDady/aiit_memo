# coding: utf-8

# リスト
colors = ['red', 'green', 'blue']

colors[0]  # red

len(colors)  # 3

c2 = colors
c2  # ['red', 'green', 'blue']

c4 = c2 + ['cyan', 'yellow']
c4  # ['red', 'green', 'blue', 'cyan', 'yellow']


# 文字列
s = "023-456-789"
s.split("-")  # ['023', '456', '789']

li = ["abc", "def"]
"-".join(li)  # abc-def

s = "abcdefghejk"
s.find("cd")  # 2 左から探す
s.index("cd")  # 2 左から探すfindと一緒　みつからなかったときの挙動がことなる
s.rfind("cd")  # 2 右から探す
s.rindex("cd")  # 2 右から探す
s.find("xy")  # -1
# s.index("xy")  # ValueError: substring not found

s.replace("ab", "xxx")  # xxxcdefghejk

s = "  abc  "
s.strip()  # 'abc'
s.lstrip()  # 'abc  '
s.rstrip()  # '  abc'

m = "hello"
m.upper()  # 'HELLO'
m = "HOGE"
m.lower()  # 'hoge'

m.isalpha()  # True
m.isdigit()  # False
m.isspace()  # False

s = "abcdef"
s.startswith("ab")  # True
s.endswith("ab")  # False
s.endswith("ef")  # True


p = 'Winning isn\'t everything \nWist\'s the only thing.\nhoge.\
unko porori'

# print(p)
'''
Winning isn't everything
Wist's the only thing.
hoge.unko porori
'''

p = """
Winning isn't everything 
Wist's the only thing.
hoge.unko porori2
"""
# print(p)
'''

Winning isn't everything 
Wist's the only thing.
hoge.unko porori2

'''

l = [21, 4, 5]
del l[1]  # [21, 5]

range(5, 10, 2)  # [5, 7, 9]
list(range(5, 10, 2))  # [5, 7, 9]

# 制御文
sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + i ** 2
    # print(i, sum)

sum = 0
for i in range(1, 11):
    sum = sum + i ** 2
    # print(i, sum)


i = 0
sum = 0
while i <= 10:
    sum = sum + i ** 2
    #print(i, sum)
    i += 1

# if in
colors = ['red', 'blue', 'green', "green"]
# if 'green' in colors:
#     print('ok')  # 'ok' あるかないかの判定なのでgreenが２つでも一回しか通らない


# リスト処理
c = ['red', 'green', 'blue', 'cyan', 'yellow', 'nagenta']
c.append('red')  # ['red', 'green', 'blue', 'cyan', 'yellow', 'nagenta', 'red']
c.count("red")  # 2
c.index('blue')  # 2
# ↓ ['green', 'blue', 'cyan', 'yellow', 'nagenta', 'red'] redをひとつだ消す
c.remove('red')
c.pop()  # ['green', 'blue', 'cyan', 'yellow', 'nagenta'] 最後尾ひとつを消す
c.pop(1)  # ['green', 'cyan', 'yellow', 'nagenta'] 前の要素から1番目が消える
c.insert(0, 'black')  # ['black', 'green', 'cyan', 'yellow', 'nagenta']

d = ['aa', 'xx', 'zz', 'bb', 'cc']
sorted(d)  # ['aa', 'bb', 'cc', 'xx', 'zz']


li = [1, 10, 100, 5, 25]
min(li)  # 1
max(li)  # 100
li.sort()  # [1, 5, 10, 25, 100]
li.reverse()  # [100, 25, 10, 5, 1]
li.append([1, 3, 5])  # [100, 25, 10, 5, 1, [1, 3, 5]]
li.extend([1, 3, 5])  # [100, 25, 10, 5, 1, [1, 3, 5], 1, 3, 5]

li2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
li2d[0][2]  # 3
print(li2d)


'''

   msg = "Hello Global!"


   def say_hi():
       global msg
       msg = "change global 2 local "
       print(msg)


   say_hi()
   print(msg)


   for i in range(0, 10):
       if i == 5:
           continue
           # break
       print(i)

   else:
       print("Finish")
    '''
