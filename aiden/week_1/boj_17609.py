import sys
input = sys.stdin.readline

def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

T = int(input())
for _ in range(T):
    st = input().strip()
    start, end = 0, len(st)-1
    ans = 0

    while start < end:
        if st[start] == st[end]:
            start += 1
            end -= 1
        else:
            if is_palindrome(st, start+1,end) or is_palindrome(st, start,end-1):
                ans = 1
            else:
                ans = 2
            break
    print(ans)