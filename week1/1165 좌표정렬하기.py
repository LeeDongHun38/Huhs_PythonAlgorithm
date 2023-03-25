import sys

n = int(sys.stdin.readline())
li = []

# if n=3, input = (1,1),(1,-1),(2,4)
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x,y))

li.sort()
# sorted li = [(1, -1), (1, 1), (2, 4)]

for i in range(n):
    print(li[i][0], li[i][1])



'''
첫 for문에 있는 'li.append((x,y))'를 'li.append(x,y)'라 써서 계속 error가 났다.

map 함수의 사용법에 대해 더 공부할 필요가 있을 것 같다.

'''