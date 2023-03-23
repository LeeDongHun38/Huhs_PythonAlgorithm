import sys

a = int(sys.stdin.readline())   # 한개의 정수를 입력받는 방법
num = [0] * 10001   # 입력값이 10000개까지 주어질 수 있으므로 10000개의 list를 미리 만들어 놓는데, 이때 0부터 세는 불편함을 없애고자 10001개의 list를 만든다.

for i in range(a):
    num[int(sys.stdin.readline())] += 1   # 리스트 각 요소에 0을 할당해놓고 입력값을 받을 떄마다 해당 인덱스에 1을 더해준다.

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)    # 0보다 큰 수를 갖는 인덱스를 찾아 해당 개수만큼 출력해주면 된다.
