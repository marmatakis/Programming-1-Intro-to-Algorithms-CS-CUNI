
class Stack:
    def __init__(self):
        self.a = []
    
    def push(self, x):
        self.a.append(int(x))
    
    def pop(self):
        if self.size() == 0:
            return "EMPTY"
        return self.a.pop()
    
    def top(self):
        if self.size() == 0:
            return "EMPTY"
        return self.a[self.size() - 1]
    
    def dup(self):
        self.push(self.top())
    
    def swap(self):
        size = self.size()
        self.a[size-1], self.a[size-2] = self.a[size-2], self.a[size-1]
    
    def add(self):
        b = self.pop()
        a = self.pop()
        self.push(a+b)
    
    def sub(self):
        b = self.pop()
        a = self.pop()
        self.push(a-b)
    
    def mul(self):
        b = self.pop()
        a = self.pop()
        self.push(a*b)
    
    def size(self):
        return len(self.a)

stack = Stack()
n = int(input())

for i in range(n):
    inp = input().split()
    if inp[0] == "PUSH":
        stack.push(inp[1])
    if inp[0] == "POP":
        stack.pop()
    if inp[0] == "PRINT":
        print(stack.top())
    if inp[0] == "SIZE":
        print(stack.size())
    if inp[0] == "DUP":
        stack.dup()
    if inp[0] == "ADD":
        stack.add()
    if inp[0] == "SUB":
        stack.sub()
    if inp[0] == "MUL":
        stack.mul()
    if inp[0] == "HALT":
        exit()
    if inp[0] == "SWAP":
        stack.swap()