def dfs(index):
    global answer

    if index == n:
        count = [checkEgg for checkEgg in egg if checkEgg[0] <= 0]
        answer = max(answer, len(count))
        return

    if egg[index][0] <= 0:
        dfs(index+1)
    else:
        is_broken = True
        for i in range(n):
            if egg[i][0] > 0 and index != i:
                is_broken = False
                egg[index][0] -= egg[i][1]
                egg[i][0] -= egg[index][1]
                dfs(index+1)
                egg[index][0] += egg[i][1]
                egg[i][0] += egg[index][1]
        if is_broken:
            dfs(n)

    
n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(0)
print(answer)