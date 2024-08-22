def backtrack(s, idx, used, result):
    if idx == len(s):  # 모든 숫자를 다 처리했을 때
        if len(used) == max(used):  # 사용된 숫자의 개수가 최대 숫자와 같아야 함 (1부터 N까지)
            print(" ".join(map(str, result)))  # 복원된 순열 출력
            return True  # 탐색 종료
        return False  # 숫자가 부족하면 종료

    # 1자리 숫자 처리
    num = int(s[idx])  # 한 자리 숫자 추출
    if 1 <= num <= 50 and num not in used:  # 유효한 숫자인지 확인
        used.add(num)
        result.append(num)
        if backtrack(s, idx + 1, used, result):  # 재귀 호출
            return True
        used.remove(num)  # 백트래킹
        result.pop()

    # 2자리 숫자 처리 (인덱스 범위 내에서만)
    if idx + 1 < len(s):
        num = int(s[idx:idx + 2])  # 두 자릿수 숫자 추출
        if 10 <= num <= 50 and num not in used:  # 유효한 숫자인지 확인
            used.add(num)
            result.append(num)
            if backtrack(s, idx + 2, used, result):  # 재귀 호출
                return True
            used.remove(num)  # 백트래킹
            result.pop()

    return False  # 현재 경로가 유효하지 않음을 알림

# 입력 처리
s = input().strip()

# 백트래킹 시작
used = set()  # 이미 사용된 숫자를 추적하기 위한 집합
backtrack(s, 0, used, [])