from random import randrange

class Node:
    def __init__(self, val, left = None, right = None):
        self.val, self.left, self.right = val, left, right

a = []

# Append all values from t to a, in order
def extract(t):
    if t == None:
        return
    extract(t.left)
    a.append(t.val)
    extract(t.right)
    

class TreeSet:
    def __init__(self):
        self.root = None

    def contains(self, x):
        p = self.root
        while p != None:
            if p.val == x:
                return True
            elif x < p.val:
                p = p.left
            elif x > p.val:
                p = p.right
        return False
    
    def add(self, x): # also called insert()
        if self.root == None: # insert into empty tree
            self.root = Node(x)
            return
        
        p = self.root
        while x != p.val:
            if x < p.val:
                if p.left == None:
                    p.left = Node(x)
                    return
                else:
                    p = p.left
            else:
                if p.right == None:
                    p.right = Node(x)
                    return
                else:
                    p = p.right
            
                

d = Node(30)
a = Node(20, right=d)
b = Node(100)
r = Node(50, a, b)

# Count the nodes in a binary tree
def count(r):
    if r == None:
        return 0
    return 1 + count(r.right) + count(r.left)
print(count(r))

# Build a complete binary tree of height h
# Every value is a random number from 0 to 9
def complete(h):
    if h == 0:
        return Node(randrange(10))
    
    l = complete(h-1)
    r = complete(h-1)
    return Node(randrange(10), l, r)

t = complete(10)
print(count(t))


def build():
    t = TreeSet()
    for i in range(1000):
        t.add(randrange(1000))
    return t

