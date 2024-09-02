class Stack:
    def __init__(self):
        self.box = []

    def push(self, item):
        self.box.append(item)

    def pop(self):
        return self.box.pop()
    
    def size(self):
        return len(self.box)
    
    def is_empty(self):
        return len(self.box) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.box[-1]
        return None
    
def bracket(string):
    stack = Stack()
    for ch in string:
        if ch in '([':
            stack.push(ch)
        elif ch == ')':
            if stack.is_empty() or stack.peek() != '(':
                return False
            stack.pop()
        elif ch == ']':
            if stack.is_empty() or stack.peek() != '[':
                return False
            stack.pop()
    return stack.is_empty()

while True:
    string = input().rstrip()
    
    if string == ".":
        break

    if bracket(string):
        print("yes")
    else:
        print("no")