import itertools
from bisect import bisect_left, bisect_right

def combi_sum(arr):
    sumArray = []

    for i in range(1, len(arr)+1):
        for minihap in itertools.combinations(arr, i):
            sumArray.append(sum(minihap))

    return sumArray

n, s = map(int, input().split())
nums = list(map(int, input().split()))

leftArray = combi_sum(nums[:n//2])
rightArray = combi_sum(nums[n//2:])

count = 0
rightArray.sort()

for left_sum in leftArray:
    right_sum = s - left_sum
    count += bisect_right(rightArray, right_sum) - bisect_left(rightArray, right_sum)

count += leftArray.count(s)
count += rightArray.count(s)

print(count)