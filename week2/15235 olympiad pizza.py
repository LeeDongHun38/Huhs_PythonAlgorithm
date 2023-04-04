from collections import deque

n=int(input())
pizza=list(map(int,input().split()))

memo=[0 for i in range(n)]
 
queue=deque()

for i in range(n):
    queue.append([i,0])

count=0

while queue:
    num,get=queue.popleft()
    count+=1

    get+=1

    if pizza[num]==get:
        memo[num]=count

    else:
        queue.append([num,get])

memo=map(str,memo)

print(' '.join(memo))