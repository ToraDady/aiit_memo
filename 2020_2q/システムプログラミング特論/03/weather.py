# coding: utf-8

sum = ncold = 0
print('今週の天気を入力してください')

for i in range(0, 7):
    temp = int(input())
    sum = sum + temp
    if temp < 0:
        ncold += 1

avt = sum / 7.0

print('今週宇野平均気温は、', avt)
print(ncold, '日間氷点下でした')
