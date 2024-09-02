N = int(input())
packet = []

while True:
    p = int(input())
    if p == -1:
        break
    packet.append(p)

q1 = []

for i in packet:
    if i == 0:
        if q1:  # 리스트가 비어있지 않은 경우에만 요소 제거
            q1.pop(0)
    else:
        if len(q1) < N:  # 큐가 가득 차지 않았을 때만 요소 추가
            q1.append(i)

# 큐에 남아 있는 값 모두 출력하기
if q1:
    print(' '.join(map(str, q1)))
else:
    print('empty')

