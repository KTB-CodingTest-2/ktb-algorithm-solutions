answer = []

while True :
    text = input()
    stack = []

    if text == "." :
        break

    for item in text :
        if item == '[' or item == '(' :
            stack.append(item)
        elif item == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() 
            else : 
                stack.append(item)
                break
        elif item == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(item)
                break
    if len(stack) == 0 :
        answer.append('yes')
    else :
        answer.append('no')

print(*answer, sep='\n')