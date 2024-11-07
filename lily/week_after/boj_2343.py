import sys

readline = sys.stdin.readline
N, M = map(int, readline().split())
arr = list(map(int, readline().split()))

left = max(arr)
right = sum(arr)

answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0
    count = 1
    
    for length in arr:
        if total + length > mid:  # 현재 블루레이에 더 이상 담을 수 없는 경우
            count += 1  # 새로운 블루레이 필요
            total = length  # 새 블루레이에 현재 강의 추가
        else:
            total += length  # 현재 블루레이에 강의 추가
    
    if count <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
