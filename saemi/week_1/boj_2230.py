n, m = map(int, input().split())
data = list()

data = [int(input()) for i in range(n)]
data.sort()

result = 2000000000
interval_gap = 0
start = 0
end = 0

while start < n and end < n:
    interval_gap = data[end] - data[start]
    if interval_gap >= m:
        result = min(interval_gap, result)
        start += 1
    else:
        if end < n:
            end += 1
        else:
            start += 1
        
print(result)