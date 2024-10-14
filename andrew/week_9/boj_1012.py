import sys

def input():
    return sys.stdin.readline().rstrip()

# 인접한 배추에 한마리라도 지렁이가 있다면 보호 가능

# 배추들이 몇 군데에 퍼져 있는지 조사하면, 총 몇 마리의 지렁이가 필요한지 알 수 있음

# ( 0, 0 )
# ( 0, 1 )
# ( 1, 1 )

# 4 2
# 4 3
# 4 5

# 2 4
# 3 4

# 7 4
# 8 4
# 9 4

# 7 5
# 8 5
# 9 5

# 7 6
# 8 6
# 9 6

result = []
for _ in range(10):
    result.append(list(map(int, input().split())))