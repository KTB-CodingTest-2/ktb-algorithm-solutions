import sys

N, S = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))


def solution():
    left = current_sum = 0
    min_length = float('inf')

    for right in range(N):
        current_sum += sequence[right]

        while current_sum >= S:
            min_length = min(min_length, right - left + 1)
            current_sum -= sequence[left]
            left += 1

    return min_length if min_length != float('inf') else 0


print(solution())