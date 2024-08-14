from itertools import combinations
from bisect import bisect_left, bisect_right

def subset_sums(arr):
    # 모든 부분집합의 합을 계산하여 리스트로 반환
    sums = [sum(comb) for r in range(len(arr) + 1) for comb in combinations(arr, r)]
    return sums

def meet_in_the_middle(arr, S):
    n = len(arr)
    # 배열을 절반으로 나누기
    left = arr[:n//2]
    right = arr[n//2:]

    # 두 부분으로 나눈 배열 각각의 부분수열 합 구하기
    left_sums = subset_sums(left)
    right_sums = subset_sums(right)

    # 오른쪽 부분의 합을 정렬
    right_sums.sort()
    
    answer = 0

    # 왼쪽 부분의 합과 오른쪽 부분의 합을 이용하여 S를 만드는 경우의 수 찾기
    for sum_left in left_sums:
        target = S - sum_left
        low = bisect_left(right_sums, target)
        high = bisect_right(right_sums, target)
        answer += high - low

    # S가 0인 경우, 공집합의 경우를 하나 빼줘야 함
    if S == 0:
        answer -= 1

    return answer

# 입력 처리
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Meet in the Middle 기법을 통해 결과 계산
answer = meet_in_the_middle(arr, S)

# 결과 출력
print(answer)

