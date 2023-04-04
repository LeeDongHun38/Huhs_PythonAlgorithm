from collections import deque
import sys

d = deque()
n = int(input())

for i in range(n):
    value =  sys.stdin.readline().split()

    if value[0] == "push_front":
        d.appendleft(value[1])
    elif value[0] == "push_back":
        d.append(value[1])
    elif value[0] == "pop_front":
        if d:
            print(d[0])
            d.popleft()
        else:
            print("-1")
    elif value[0] == "pop_back":
        if d:
            print(d[len(d) - 1])
            d.pop()
        else:
            print("-1")
    elif value[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif value[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif value[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")

    