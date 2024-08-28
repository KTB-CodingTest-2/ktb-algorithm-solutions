N = int(input())

count = 0
row = [0] * N

# 추가된 배열들
cols = [False] * N  # 각 열에 퀸이 있는지 여부
diagonal1 = [False] * (2 * N - 1)  # 왼쪽 대각선
diagonal2 = [False] * (2 * N - 1)  # 오른쪽 대각선

def is_promising(x):
    return not (cols[row[x]] or diagonal1[x - row[x] + (N-1)] or diagonal2[x + row[x]])

def n_queens(x):
    global count
    if x == N:
        count += 1
        return
    
    for i in range(N):
        row[x] = i
        if is_promising(x):
            # 퀸 배치 후 해당 열과 대각선을 사용 중으로 표시
            cols[i] = diagonal1[x - i + (N-1)] = diagonal2[x + i] = True
            n_queens(x + 1)
            # 재귀가 끝난 후 원래대로 복구 (백트래킹)
            cols[i] = diagonal1[x - i + (N-1)] = diagonal2[x + i] = False

n_queens(0)
print(count)