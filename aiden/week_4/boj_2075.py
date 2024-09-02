import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

# 처음 N개의 숫자를 힙에 넣음
for _ in range(N):
    numbers = list(map(int, input().split()))
    for number in numbers:
        if len(heap) < N:
            heapq.heappush(heap, number)
        else:
            # 현재 힙의 루트(최솟값)보다 큰 경우에만 힙에 삽입
            if number > heap[0]:
                heapq.heappushpop(heap, number)

# 마지막에 남은 힙의 루트가 N번째로 큰 값
print(heap[0])