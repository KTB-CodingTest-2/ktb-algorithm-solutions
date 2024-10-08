import sys

N, M = 0, 0
sequence = []
visited = []
answer = []

def back(cnt, start):
    global N, M, sequence, visited, answer

    if cnt == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(start, N):
        answer.append(sequence[i])
        back(cnt + 1, i)
        answer.pop()

readline = sys.stdin.readline
N, M = map(int, readline().split())
sequence = list(map(int, readline().split()))
sequence.sort()
visited = [False] * N

if M == 1:
    output = '\n'.join(map(str, sequence))
    print(output)
else:
    back(0, 0)
