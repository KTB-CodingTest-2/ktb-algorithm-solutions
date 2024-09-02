import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []

for _ in range(N):
    for n in map(int, input().split()):
        heapq.heappush(q, n)
    q = heapq.nlargest(N, q)

heapq.heapify(q)
print(heapq.heappop(q))