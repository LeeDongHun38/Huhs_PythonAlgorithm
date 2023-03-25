import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append((y,x))

li.sort()

for i in range(n):
    print(li[i][1], li[i][0])