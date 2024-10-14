# 문제명: 멋쟁이 숫자

# 숫자로만 이루어진 문자열 s가 있습니다. (0 <=  s.length < 1,000)
# 아래의 조건을 모두 만족하는 숫자를 '멋쟁이 숫자'라고 합니다.
#
# **[조건]**
# 1. 길이가 3인 s의 substring을 10진수로 읽은 숫자이다.
# 2. 각 자리의 숫자가 모두 같다.

# **구현사항**

# 문자열s를 입력받아 멋쟁이 숫자를 리턴하는 함수를 만들어주세요.
#
# - 만약, 멋쟁이 숫자가 여러 개 존재하는 경우에는 가장 큰 수를 리턴합니다.
# - 만약, 가장 큰 멋쟁이 숫자가 000이라면 0을 리턴합니다.
# - 만약, 멋쟁이 숫자가 존재하지 않다면 -1을 리턴합니다.

import re

pattern = r"(\d)\1{2}"


def solution(s):
    result = re.findall(pattern, s)
    if not result:
        return -1

    return max(result) * 3


if __name__ == "__main__":
    print(solution(input()))
