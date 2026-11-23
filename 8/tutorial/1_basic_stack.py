
class Stack:
    def __init__(self):
        self.a = []
    
    def push(self, x):
        self.a.append(x)
    
    def pop(self):
        if self.size() == 0:
            return "EMPTY"
        return self.a.pop()
    
    def top(self):
        if self.size() == 0:
            return "EMPTY"
        return self.a[self.size() - 1]
    
    def size(self):
        return len(self.a)

stack = Stack()
n = int(input())

for i in range(n):
    inp = input().split()
    if inp[0] == "PUSH":
        stack.push(inp[1])
    if inp[0] == "POP":
        print(stack.pop())
    if inp[0] == "TOP":
        print(stack.top())
    if inp[0] == "SIZE":
        print(stack.size())