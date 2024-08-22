import sys
input = sys.stdin.readline

def combination(arr, M):
    combinations = []
    if M == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:], M - 1):
            combinations.append([elem] + rest)
    return combinations

while True:
    # 한 줄의 입력을 받아 공백으로 나눈 뒤 정수 리스트로 변환
    data = list(map(int, input().split()))
    
    # 첫 번째 숫자를 K로 저장
    K = data[0]
    
    # K가 0이면 입력 종료
    if K == 0:
        break
    
    # 나머지 숫자들을 리스트 S로 저장
    S = data[1:]
    
    # itertools.combinations를 사용하여 6개 숫자의 조합을 생성
    for comb in combination(S, 6):
        print(*comb)
    
    # 각 테스트 케이스 후에 빈 줄 출력
    print()