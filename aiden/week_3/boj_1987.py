import sys
input = sys.stdin.readline

def dfs(maps, right, left, visited_mask):
    global max_count, memo
    
    # 메모이제이션: 이미 동일한 상태를 탐색한 경우
    if (right, left, visited_mask) in memo:
        return memo[(right, left, visited_mask)]
    
    # 현재 경로 길이 갱신
    max_count = max(max_count, bin(visited_mask).count('1'))
    
    # 최대 길이가 26이면 더 이상 탐색할 필요가 없음
    if max_count == 26:
        return max_count

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    best_path = max_count

    for dr, dc in directions:
        nr, nl = right + dr, left + dc
        if 0 <= nr < R and 0 <= nl < C:
            next_char = maps[nr][nl]
            bit = 1 << (ord(next_char) - ord('A'))
            if not visited_mask & bit:
                # 해당 알파벳을 방문 표시하고 다음 경로 탐색
                best_path = max(best_path, dfs(maps, nr, nl, visited_mask | bit))

    # 메모이제이션: 현재 상태를 기록
    memo[(right, left, visited_mask)] = best_path
    return best_path

# 입력 처리
R, C = map(int, input().split())
maps = [input().strip() for _ in range(R)]

# 비트마스크로 방문 상태 관리
visited_mask = 1 << (ord(maps[0][0]) - ord('A'))  # 첫 번째 알파벳 방문 처리

max_count = 1  # 초기 경로 길이
memo = {}  # 메모이제이션을 위한 딕셔너리

# DFS 시작
dfs(maps, 0, 0, visited_mask)

# 결과 출력
print(max_count)

