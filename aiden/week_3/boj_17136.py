from collections import deque
import sys
input = sys.stdin.readline

def can_place(maps, r, c, size):
    if r + size > 10 or c + size > 10:  # 경계 검사
        return False
    for i in range(size):
        for j in range(size):
            if maps[r + i][c + j] != 1:  # 색종이를 덮을 수 있는지 확인
                return False
    return True

def place_paper(maps, r, c, size, value):
    for i in range(size):
        for j in range(size):
            maps[r + i][c + j] = value  # 색종이 붙이기(0) 또는 떼기(1)

def bfs(maps):
    queue = deque([(maps, 0, [5, 5, 5, 5, 5], 0, 0)])
    visited = set()  # 중복 상태 방지
    min_count = 26

    while queue:
        curr_maps, count, papers_left, r, c = queue.popleft()

        # 이미 최소값 이상 사용했다면 더 이상 탐색할 필요 없음 (가지치기)
        if count >= min_count:
            continue

        # 종이의 모든 칸을 탐색한 경우
        if r == 10:
            min_count = min(min_count, count)
            continue

        # 다음 행으로 이동
        if c == 10:
            queue.append((curr_maps, count, papers_left, r + 1, 0))
            continue

        # 현재 위치가 1이면 색종이를 붙여야 함
        if curr_maps[r][c] == 1:
            for size in range(5, 0, -1):
                if papers_left[size - 1] > 0 and can_place(curr_maps, r, c, size):
                    new_maps = [row[:] for row in curr_maps]
                    place_paper(new_maps, r, c, size, 0)
                    new_papers_left = papers_left[:]
                    new_papers_left[size - 1] -= 1
                    state = (tuple(tuple(row) for row in new_maps), tuple(new_papers_left))
                    if state not in visited:
                        visited.add(state)
                        queue.append((new_maps, count + 1, new_papers_left, r, c + size))
        else:
            queue.append((curr_maps, count, papers_left, r, c + 1))  # 다음 칸으로 이동

    return -1 if min_count == 26 else min_count

# 입력 처리
maps = [list(map(int, input().split())) for _ in range(10)]

# BFS 시작
result = bfs(maps)
print(result)