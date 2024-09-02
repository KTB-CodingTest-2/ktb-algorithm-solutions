import sys
from itertools import combinations


def lotto(numbers):
    for combination in combinations(numbers, 6):
        print(' '.join(map(str, combination)))
    print()


while True:
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    k = line[0]

    if k == 0:
        break

    numbers = line[1:]
    lotto(numbers)