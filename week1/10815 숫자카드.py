# 이진탐색 알고리즘 오랜만에 해서 까먹음.. 복습하자


import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
newCard = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, newCard[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')