def back():
    if len(arr) == N:
        print("".join(map(str, arr)))
        return True

    for i in range(3):  # s의 1, 2, 3을 각각 시도
        arr.append(s[i])

        if is_good_sequence(arr):  # 좋은 수열인지 확인
            if back():  # 다음 단계로 재귀 호출
                return True
        
        arr.pop()  # 잘못된 경우, 백트래킹
    
    return False  # 유효한 수열이 없으면 False 반환

def is_good_sequence(sequence):
    length = len(sequence)

    for i in range(1, length // 2 + 1):
        if sequence[-i:] == sequence[-2*i:-i]:  # 인접한 부분 수열 비교
            return False  # 나쁜 수열이면 False 반환
    return True  # 좋은 수열이면 True 반환

s = [1, 2, 3]
N = int(input())
arr = []

back()