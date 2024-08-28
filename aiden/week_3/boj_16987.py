N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

max_broken = 0

# 계란
def back(x):
    global max_broken

    if x == N:
        broken_eggs = sum(1 for egg in eggs if egg[0] <= 0)  # 깨진 계란의 수 세기
        max_broken = max(max_broken, broken_eggs)
        return
    
    if eggs[x][0] <= 0:
        back(x + 1)
        return
    
    hit_any_egg = False  # 다른 계란을 쳤는지 여부
    for i in range(N):
        if i != x and eggs[i][0] > 0:  # 다른 계란이면서 깨지지 않은 계란
            hit_any_egg = True

            # 계란을 친다
            eggs[x][0] -= eggs[i][1]  # 현재 계란의 내구도가 상대 계란의 무게만큼 깎임
            eggs[i][0] -= eggs[x][1]  # 상대 계란의 내구도가 현재 계란의 무게만큼 깎임

            # 다음 계란으로 넘어감
            back(x + 1)

            # 백트래킹: 원래 상태로 돌려놓음
            eggs[x][0] += eggs[i][1]
            eggs[i][0] += eggs[x][1]

    # 어떤 계란도 치지 않은 경우 다음으로 넘어감
    if not hit_any_egg:
        back(x + 1)

# 백트래킹 시작
back(0)
print(max_broken)