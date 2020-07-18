def fb(n):
    return "Fizz"*(n % 3 < 1)+"Buzz"*(n % 5 < 1) or None


i = 1
while i <= 20:
    print(i, fb(i))
    i = i + 1
