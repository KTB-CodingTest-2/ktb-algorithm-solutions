def dfs(index):
    global ans

    if len(nums) == index:
        print(*ans)
        exit()

    if nums[index] != "0": # 앞자리가 0이 아님
        single = nums[index] # 한자리수
        double = nums[index : index + 2] # 두자리수
        # 한자리수
        if int(single) <= length and single not in ans:
            ans.append(single)
            dfs(index + 1)
            ans.pop()
        # 두자리수
        if int(double) <= length and double not in ans:
            ans.append(double)
            dfs(index + 2)
            ans.pop()

ans = list()
nums = input().rstrip()

if len(nums) < 10: 
    length = len(nums)
else:
    length = 9 + (len(nums) - 9) // 2

dfs(0)