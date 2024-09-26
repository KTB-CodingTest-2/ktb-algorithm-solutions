# n개의 리스트
# M개의 부분 수열

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = list()

def dep_stack():
    if len(temp) == m:
        print(*temp)
        return
    else:
        for i in arr:
            if i in temp:
                continue
            temp.append(i)
            dep_stack()
            temp.pop()

dep_stack()