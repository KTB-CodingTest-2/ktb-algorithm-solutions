import sys

s = sys.stdin.readline().rstrip()
answer = -1
for i in range(0, len(s) - 2):    
    if s[i] == s[i+1] and s[i] == s[i+2]:
        answer = max(answer, int(s[i:i+3]))
    
print(answer)