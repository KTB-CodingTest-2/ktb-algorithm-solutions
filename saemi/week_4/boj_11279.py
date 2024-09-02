import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []
answer = []
count = 0

for index in range(N):
    n = int(input())
    if n == 0:
        count += 1
        if q == []:
            answer.append(0)
        else:
            answer.append(-heapq.heappop(q))
    else:
        heapq.heappush(q, -n)

[print(answer[i]) for i in range(count)]