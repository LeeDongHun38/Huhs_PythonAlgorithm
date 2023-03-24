a = int(input())
num = []

num = list(map(int, str(a)))
num.sort(reverse = True)

for i in num:
    print(i, end="")