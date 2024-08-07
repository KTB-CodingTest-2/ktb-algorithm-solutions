import sys
input = sys.stdin.readline

N, S = map(int, input().split())
sequence = list(map(int, input().split()))

start,end =0,0
sum = sequence[start]
min_len = N+1
while True:
    if sum < S:
        end += 1
        if end == N:
            break
        sum += sequence[end]
    elif sum >= S:
        min_len = min(min_len ,end - start + 1)
        sum -= sequence[start]
        start += 1

print(min_len if min_len != N + 1 else 0)

