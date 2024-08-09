import sys

N = int(sys.stdin.readline())


def is_check(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


for _ in range(N):
    s = sys.stdin.readline().strip()
    left, right = 0, len(s) - 1
    result = 0
    while left < right:
        if s[left] != s[right]:
            if (result := 1 if is_check(s, left + 1, right) or is_check(s, left, right - 1) else 2) != 0:
                break
        left += 1
        right -= 1
    print(result)
