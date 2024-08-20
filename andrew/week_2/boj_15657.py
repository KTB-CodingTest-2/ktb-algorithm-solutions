import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
sequence = sorted(map(int, sys.stdin.readline().rstrip().split(" ")))


def backtrack(start, current):
    if len(current) == M:
        print(" ".join(map(str, current)))
        return

    for i in range(start, N):
        backtrack(i, current + [sequence[i]])


backtrack(0, [])