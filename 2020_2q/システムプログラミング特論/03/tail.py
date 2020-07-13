# coding: utf-8

f = open('small.txt', 'rU')
a = f.readlines()
a.reverse()
for i in a:
    print(i.replace('\n', ''))

f.close
'''
改行コードで悩んだらこちら
https: // qiita.com/ringCurrent/items/aa0044a0cfee91762c80
'''
