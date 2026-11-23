
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
call_stack = Stack()
n = int(input())
pc = 0

labels = {}
instructions = []

for i in range(n):
    inp = input().split()
    instructions.append(inp)
    if inp[0].endswith(":"):
        labels[inp[0][:-1]] = i

while instructions[pc][0] != "HALT":
    inp = instructions[pc]
    if inp[0] == "CALL":
        label = inp[1]
        call_stack.push(pc+1)
        pc = labels[label]
        continue
    if inp[0] == "JZ":
        val = stack.pop()
        label = inp[1]
        if val == 0:
            pc = labels[label]
            continue
    if inp[0] == "RET":
        pc = call_stack.pop()
        continue
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
    if inp[0] == "SWAP":
        stack.swap()
    pc += 1
    


    
    
