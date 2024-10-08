# n개의 리스트
# M개의 부분 수열

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []

def make_array(point):
    if len(stack) < m:
        for i in range(point, n):
            if arr[i] in stack:
                continue
            stack.append(arr[i])
            make_array(i+1)  
            stack.pop()
    else:
        print(*stack)
        return
make_array(0)