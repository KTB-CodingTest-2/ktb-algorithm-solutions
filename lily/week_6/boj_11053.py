import sys

readline = sys.stdin.readline
N = int(readline())
seq = list(map(int, readline().split()))
dp = [1] * N # i번째 수를 마지막으로 가지는 부분 증가 수열의 길이
answer = 0

for i in range(N):
    max_len = 0
    for j in range(i+1):
        if seq[i] > seq[j]: # 특정 값보다 크다는 것은 특정 값에서의 수열의 마지막에 붙일 수 있다는 의미
            dp[i] = max(dp[i], dp[j] + 1)
    answer = max(answer, dp[i])

print(answer)
