
class Stack:
    def __init__(self):
        self.a = []
        
    def push(self, x):
        self.a.append(x)
    
    def pop(self):
        return self.a.pop()
    
    def is_empty(self):
        return self.a == []

class Queue():
    def __init__(self):
        self.a = []
    
    def enqueue(self, x):
        self.a.append(x)
        
    def dequeue(self):
        return self.a.pop(0)

    def is_empty(self):
        return self.a == []

def test():
    q = Queue()
    for i in range(100_000):
        q.enqueue(i)
    while not q.is_empty():
        print(q.dequeue())


class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = self.tail = None
    
    def enqueue(self,x):
        n = Node(x, None)
        if self.head == None:
            self.head = self.tail = n
            return
        self.tail.next = n
        self.tail = n
    
    def dequeue(self):
        assert self.head != None, 'queue is empty'
        x = self.head.val
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return x
    
    def is_empty(self):
        return self.head == None
    
def test(n):
    q = Queue()
    for i in range(n):
        q.enqueue(i)
    while not q.is_empty():
        print(q.dequeue())
# test(100_000)

class Set:
    def __init__(self):
        self.a = []
    
    def add(self, x): # O(n)
        if x not in self.a:
            self.a.append(x)
    
    def remove(self, x):
        if x in self.a:
            self.a.remove(x)
    
    def contains(self, x):
        return x in self.a

