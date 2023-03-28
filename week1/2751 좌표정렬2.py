import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)    # 맨첨에는 print(num[i])라고 했는데 에러가 떴다. 그냥 i만 써줘도 충분할듯