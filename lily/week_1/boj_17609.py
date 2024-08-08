# 회문
import sys

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def check_palindrome_or_not(input_str):
    start_idx = 0
    end_idx = len(input_str) - 1
    
    while start_idx < end_idx:
        if input_str[start_idx] == input_str[end_idx]:
            start_idx += 1
            end_idx -= 1
            continue
        
        # 두 경우 중에 하나라도 회문이면 유사 회문
        if is_palindrome(input_str, start_idx + 1, end_idx) or is_palindrome(input_str, start_idx, end_idx - 1):
            return 1
        return 2

    return 0

readline = sys.stdin.readline
T = int(readline())
input_strs = []
for i in range(T):
    input_strs.append(readline().rstrip('\n'))

for input_str in input_strs:
    print(check_palindrome_or_not(input_str))