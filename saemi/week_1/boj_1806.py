n, s = map(int, input().split())
data = list(map(int, input().split()))

length = 0
sum = list()
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += data[end]
        end += 1
        
    if interval_sum >= s:
        length = end - start
        sum.append(length)
    
    interval_sum -= data[start]

if sum == []:
    print(0)
else:
    sum.sort()
    print(sum[0]) 