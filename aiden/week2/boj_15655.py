import sys
input = sys.stdin.readline

def combination(arr, M):
    combinations = []
    if M == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:], M - 1):
            combinations.append([elem] + rest)
    return combinations

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

for seq in combination(arr, M):
    print(*seq)