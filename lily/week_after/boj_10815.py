import sys
import bisect

# 방법 1. 이분 탐색
readline = sys.stdin.readline
N = int(input())
arr = sorted(map(int, readline().split()))
M = int(input())
brr = list(map(int, readline().split()))

for b in brr:
    idx = bisect.bisect_left(arr, b)
    if idx < N and arr[idx] == b:
        print(1, end=" ")
    else:
        print(0, end=" ")

# 방법 2. set
readline = sys.stdin.readline
N = int(input())
arr = set(map(int, readline().split()))
M = int(input())
brr = list(map(int, readline().split()))

for b in brr:
    if b in arr:
        print(1, end=" ")
    else:
        print(0, end=" ")