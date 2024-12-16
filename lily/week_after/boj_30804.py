import sys

readline = sys.stdin.readline

N = int(readline()) # 과일의 개수
fruits = list(map(int, readline().split()))
dic = {} # 각 과일에 대한 개수
# for f in fruits:
#     if f in dic:
#         dic[f] += 1
#     else:
#         dic[f] = 1

left, right = 0, 0
f = fruits[0]
dic[f] = 1
"""
left~right까지의 과일 개수가 2개 이하라면 right를 늘리고
아니면 left를 줄임
=> 끝까지 탐색
"""

answer = 0

while right < N:
    if len(dic) <= 2:
        answer = max(answer, right-left+1)
        right += 1
        if right == N:
            break

        f = fruits[right]
        if dic.get(f):
            dic[f] += 1
        else:
            dic[f] = 1
    else:
        f = fruits[left]
        dic[f] -= 1
        if dic[f] == 0:
            del dic[f]
        left += 1

print(answer)