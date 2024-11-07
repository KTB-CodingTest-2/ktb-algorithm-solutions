import sys
from collections import deque

# o == 빈 공간
# X == 벽
# I == 도연
# P == 사람

def dfs(x,y):
    global count
    visited[x][y] = True

    if graph[x][y] == 'P':
        count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 캠퍼스 밖으로 벗어나지 않고, 방문했던 위치가 아니며, 벽이 아닌 경우에만 이동
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] != 'X':
            dfs(nx,ny)

input = sys.stdin.readline
N, M = map(int, input().strip().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

graph = list(input() for _ in range(N))
visited = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            dfs(i,j)

if count == 0:
    print('TT')
else:
    print(count)