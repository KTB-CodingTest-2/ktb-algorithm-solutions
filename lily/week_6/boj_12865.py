import sys

readline = sys.stdin.readline

N, K = map(int, readline().split()) # 물품 수, 배낭 무게
jewels = [(0, 0)] # 각 물품의 무게, 가치 튜플 리스트

for _ in range(N):
    w, v = map(int, readline().split())
    jewels.append((w, v))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)] # 각 물건 별로 각 무게 (1~K) 까지의 최댓값

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = jewels[i]

        if w > j:
            dp[i][j] = dp[i-1][j]
            continue

        dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[N][K])


