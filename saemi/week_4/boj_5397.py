N = int(input())

answer = []
for _ in range(N):
    leftPass = []
    rightPass = []
    text = input()
    for item in text:
        if item == '-':
            if leftPass: #왼쪽 스택에 있을 경우
                leftPass.pop()
        elif item == '<': # 왼스택에 있는 문자 오른쪽 스택으로
            if leftPass:
                rightPass.append(leftPass.pop())
        elif item == '>': # 오스택에 있는 문자 왼쪽 스택으로
            if rightPass:
                leftPass.append(rightPass.pop())
        else:
            leftPass.append(item)

    leftPass.extend(reversed(rightPass)) # 오른쪽 스택에 있는 문자들은 뒤집어서 붙여야 한다.
    answer.append(''.join(leftPass))

print(*answer, sep='\n')