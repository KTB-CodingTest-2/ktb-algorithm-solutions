import sys
from collections import deque

"""
조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n,3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11
"""

def bfs(start_team_id):
    cnt = 0
    visited[start_team_id] = True
    dq = deque()
    dq.append(start_team_id)

    while len(dq) > 0:
        now_team_id = dq.pop()
        cnt += team_infos[now_team_id][2] # 팀원 수 누적

        for sub_team_id in edges[now_team_id]:
            if not visited[sub_team_id]:
                visited[sub_team_id] = True
                dq.append(sub_team_id)
    
    return cnt

readline = sys.stdin.readline
csv_string = "조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11".rstrip()
keyword = "아웃"
orgs = csv_string.split('\n')
target_team_ids = [] # keyword가 포함되어 있는 팀 id 리스트
team_len = len(orgs)
edges = [[] for _ in range(team_len+1)] # 각 노드에서 갈 수 있는 간선들
team_infos = [[] for _ in range(team_len+1)] # (팀 id, 이름, 팀원 수)

for i in range(1, team_len):
    infos = orgs[i].split(",")
    # print(infos)
    team_id = int(infos[0])
    team_name = infos[1]
    team_num = int(infos[3])
    team_infos[i] = (team_id, team_name, team_num)

    if infos[2] != '':
        supervise_id = int(infos[2])
        edges[supervise_id].append(team_id) # 상위 조직의 간선에 추가
    
    if keyword in team_name:
        target_team_ids.append(team_id)
    

answer = 0
visited = [False] * (team_len+1)
for target_team_id in target_team_ids:
    if visited[target_team_id]:
        continue

    answer += bfs(target_team_id)
print(answer)