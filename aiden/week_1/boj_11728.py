import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

a, b = 0, 0
while a < N or b < M:
    if a == N:  # A 배열이 끝난 경우
        result.append(B[b])
        b += 1
    elif b == M:  # B 배열이 끝난 경우
        result.append(A[a])
        a += 1
    elif A[a] <= B[b]:  # A[a]가 B[b]보다 작거나 같은 경우
        result.append(A[a])
        a += 1
    else:  # B[b]가 A[a]보다 작은 경우
        result.append(B[b])
        b += 1

# 결과 출력
print(*result)
