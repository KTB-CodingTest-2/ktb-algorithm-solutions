class Stack:
    def __init__(self):
        self.box = []
        self.output = []  # 출력을 저장하기 위한 리스트

    def push(self, item):
        self.box.append(item)
        self.output.append('+')  # 리스트에 출력 저장
        
    def pop(self):
        self.box.pop()
        self.output.append('-')  # 리스트에 출력 저장
    
    def size(self):
        return len(self.box)
    
    def is_empty(self):
        return len(self.box) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.box[-1]
        return None
    
n = int(input())
integer = [int(input()) for _ in range(n)]
stack = Stack()

current = 1  
possible = True  # 수열을 만들 수 있는지 여부를 저장

for number in integer:
    while current <= number:
        stack.push(current)
        current += 1
    
    if stack.peek() == number:
        stack.pop()
    else:
        possible = False
        break

if possible:
    for op in stack.output:  # 저장된 출력 리스트에서 출력
        print(op)
else:
    print("NO")