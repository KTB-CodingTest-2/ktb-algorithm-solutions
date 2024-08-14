import sys
input = sys.stdin.readline
A = []
N, M = map(int, input().split())
for _ in range(N):
    A.append(int(input()))

A.sort()

start, end = 0,0
mul = 0
gap = max(A) - min(A)
while start < N and end < N:
    mul = abs(A[start] - A[end])
    if mul >= M:
        gap = min(mul,gap)
        start += 1
    elif mul < M:
        end += 1
print(gap)