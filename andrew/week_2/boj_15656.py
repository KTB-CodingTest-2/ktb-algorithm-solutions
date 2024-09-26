import sys

N, M = map(int, sys.stdin.readline().split(" "))
sequence = sorted(map(int, sys.stdin.readline().split(" ")))

def recursion_tree(current_select: list, depth: int) -> list:
    if depth == M:
        return [current_select]
    results = []
    for num in range(N):
        results.extend(recursion_tree(current_select + [num], depth + 1))
    return results

for data in recursion_tree([], 0):
    print(" ".join(map(str, [sequence[num_idx] for num_idx in data])))
