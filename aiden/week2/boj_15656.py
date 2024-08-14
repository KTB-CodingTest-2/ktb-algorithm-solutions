import sys
input = sys.stdin.readline

def combination(arr, N, M):
    combinations = []
    if M == 0:
        return [[]]
    
    for i in range(N):
        elem = arr[i]
        for rest in combination(arr[:], N , M - 1):
            combinations.append([elem] + rest)
    return combinations

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

for seq in combination(arr, N, M):
    print(*seq)