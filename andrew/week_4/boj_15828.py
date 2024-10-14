import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

buffer = deque()

while True:
    num = int(input())
    if num == -1:
        break
    if len(buffer) == N:
        continue
    if num != 0:
        buffer.append(num)
    else:
        buffer.popleft()
print(" ".join(map(str, buffer) if buffer else "empty"))
