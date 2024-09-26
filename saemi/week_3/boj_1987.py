R, C = map(int, input().split())

graph = [list(input()) for i in range(R)]

visited=[0]*26
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtracking(x, y, count):
    global ans
    ans = max(ans, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited[ord(graph[nx][ny])-ord('A')]==0:
            visited[ord(graph[nx][ny])-ord('A')]=1
            backtracking(nx,ny,count+1)
            visited[ord(graph[nx][ny])-ord('A')]=0
 
visited[ord(graph[0][0])-ord('A')]=1
backtracking(0, 0, 1)
print(ans)