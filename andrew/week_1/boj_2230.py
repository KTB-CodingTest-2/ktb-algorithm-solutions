import sys

N, M = map(int, sys.stdin.readline().split())
A = sorted([int(sys.stdin.readline()) for _ in range(N)])

left, right = 0, 0
result = float('inf')

while left < N and right < N:
    diff = A[right] - A[left]

    if diff >= M:
        result = min(result, diff)
        left += 1
    else:
        right += 1

    if left > right:
        right = left

print(result)