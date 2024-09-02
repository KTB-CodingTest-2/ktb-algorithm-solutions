import sys
from collections import deque

N = sys.stdin.readline().rstrip()
dq = deque()

for _ in range(int(N)):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push_front': #X: 정수 X를 덱의 앞에 넣는다.
        dq.appendleft(command[1])
    elif command[0] == 'push_back': #X: 정수 X를 덱의 뒤에 넣는다.
        dq.append(command[1])
    elif command[0] == 'pop_front': #덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif command[0] == 'pop_back': #덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq) - 1])
            dq.pop()
    elif command[0] == 'size': #덱에 들어있는 정수의 개수를 출력한다.
        print(len(dq))
    elif command[0] == 'empty': #덱이 비어있으면 1을, 아니면 0을 출력한다.
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front': #덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == 'back': #덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq) - 1])
