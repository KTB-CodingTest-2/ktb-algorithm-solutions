import sys
input = sys.stdin.readline

def Permutation(arr,M):
    result = []
    if M == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in Permutation(arr[:i] + arr[i+1:], M-1):
            result.append([elem]+rest)
    return result

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)

for perm in Permutation(arr, N, M):
    print(*perm)




