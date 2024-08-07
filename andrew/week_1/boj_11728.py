from collections import deque

N, M = map(int, input().split())
A, B = deque(map(int, input().split())), deque(map(int, input().split()))

result = deque()

while A and B:
    result.append(A.popleft() if A[0] <= B[0] else B.popleft())

result.extend(A or B)

print(*result)
