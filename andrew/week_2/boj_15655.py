import sys

N, M = map(int, sys.stdin.readline().split(" "))
sequence = sorted(map(int, sys.stdin.readline().split(" ")))

def recurion_tree(current_select: list, depth: int) -> list:
    if depth == M:
        if all([current_select[i] < current_select[i+1] for i in range(M-1)]):
            return [current_select]
        return []
    results = []
    for num in range(N):
        if num not in current_select:
            results.extend(recurion_tree(current_select + [num], depth + 1))
    return results

for data in recurion_tree([], 0):
    print(" ".join(map(str, [sequence[num_idx] for num_idx in data])))
