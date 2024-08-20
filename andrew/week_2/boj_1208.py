import sys
from itertools import combinations
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

def sub_sums(seq_list):
    sum_list = defaultdict(int)
    for i in range(len(seq_list) + 1):
        for subset in combinations(seq_list, i):
            sum_list[sum(subset)] += 1
    return sum_list

def solve(N, S, sequence):
    mid = N // 2
    left_half = sequence[:mid]
    right_half = sequence[mid:]

    left_sums = sub_sums(left_half)
    right_sums = sub_sums(right_half)

    total_cnt = 0

    for left_sum, left_cnt in left_sums.items():
        right_sum = S - left_sum
        if right_sum in right_sums:
            total_cnt += left_cnt * right_sums[right_sum]

    if S == 0:
        total_cnt -= 1

    return total_cnt


N, S = map(int, input().split())
sequence = list(map(int, input().split()))

result = solve(N, S, sequence)
print(result)