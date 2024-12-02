from collections import deque
import sys
input=sys.stdin.readline

def output(command):
    cmd = command[0]
    if cmd == 'push_front':
        mydeq.appendleft(int(command[1]))
    elif cmd == 'push_back':
        mydeq.append(int(command[1]))
    elif cmd == 'pop_front':
        return mydeq.popleft() if mydeq else -1
    elif cmd == 'pop_back':
        return mydeq.pop() if mydeq else -1
    elif cmd == 'size':
        return len(mydeq)
    elif cmd == 'empty':
        return 1 if not mydeq else 0
    elif cmd == 'front':
        return mydeq[0] if mydeq else -1
    elif cmd == 'back':
        return mydeq[-1] if mydeq else -1

N = int(input())
mydeq = deque()

for i in range(N):
    command = input().split()
    result = output(command)
    if result is not None:
        print(result)