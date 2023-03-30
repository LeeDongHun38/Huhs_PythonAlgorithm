'''
처음 생각
'('에 대한 리스트와 ')'에 대한 리스트를 따로 만든 후 리스트 간의 길이 비교로 VPS 문인지 판단하고자 했다.
정상 작동하나, 한 번에 output이 출력되지 않는 문제가 있었고, 또한 이번 주 주제가 stack인 만큼 stack을 써서 풀이하는게 옳다고 생각했다. 그래서 다시 품..

import sys

n = int(sys.stdin.readline())
l = []
r = []

for i in range(n):
    a = sys.stdin.readline()
    for j in a:
        if j == '(':
            l.append(j)
        elif j == ')':
            r.append(j)

    if len(l) == len(r):
        print('YES')
        while '(' in l:
            l.remove('(')
        while ')' in r:
            r.remove(')')
    else:
        print('NO')
        while '(' in l:
            l.remove('(')
        while ')' in r:
            r.remove(')')

'''


n = int(input())

for i in range(n):
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: 
                print("NO")
                break
    else:
        if not stack: 
            print("YES")
        else: 
            print("NO")