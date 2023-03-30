a = int(input())
b = 2
while True:
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if b >= a:
        print((a - (b // 2)) * 2)
        break