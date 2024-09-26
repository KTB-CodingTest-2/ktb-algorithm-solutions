import sys

def parsing_password(inputs):
    cursor_idx = 0
    password = []
    for char in inputs:
        if char == '<':
            cursor_idx = max(cursor_idx - 1, 0)
        elif char == '>':
            cursor_idx = min(cursor_idx + 1, len(password))
        elif char == '-':
            cursor_idx = max(cursor_idx - 1, 0)
            if cursor_idx == 0:
                continue
            else:
                password.pop(cursor_idx)
        else:
            password.insert(cursor_idx, char)
            cursor_idx += 1
    
    return ''.join(password)

readline = sys.stdin.readline
T = int(readline())
for _ in range(T):
    answer = parsing_password(readline().rstrip())
    print(answer)