from math import sqrt

# immutable vector of any number of dimensions
class Vec:
    def __init__(self, *args):
        # self.a = [*args]
        self.a = args
    def __repr__(self):
        t = [str(x) for x in self.a]
        s = ' '.join(t)
        return '['+s+']'
    
    def dims(self): # return of dimensions of vector
        return len(self.a)

    def length(self):
        return sqrt(sum([item * item for item in self.a]))

    def __add__(self, w):
        assert len(self.a) == len(w.a)
        # z = [self.a[i] + w.a[i] for i in range(self.dims())]
        z = [a+b for a, b in zip(self.a, w.a)]
        return Vec(*z)
    
    def __mul__(self, w):
        assert len(self.a) == len(w.a)
        s = 0
        for i in range(w.dims()):
            s += self.a[i] * w.a[i]
        return s
        

v = Vec(3, 4)
print(v * Vec(2, 5))

print([x * x for x in range(1, 10)])

l = [10, 20, 30]
m = [x+1 for x in l]
print(m)

s = [(x, x **2) for x in range(1, 11)]
print(s)

# Project Euler #1

s = sum([x for x in range(1000) 
            if x % 3 == 0 or x % 5 == 0])

print(s)

from random import randrange
import time

def foo():
    a = [randrange(1000) for i in range(10_000_000)]
    b = [randrange(1000) for i in range(10_000_000)]
    
    t = time.time()
    c = sum([a[i] * b[i] for i in range(len(a))])
    print('no zip', time.time() - t)
    t = time.time()
    d = sum([x*y for x,y in zip(a, b)])
    print('with zip', time.time() - t)

# foo()

# print([(x, y) for x in range(4) for y in range(4) if x != y])

# [[1, 2], [3,4], [5,6]]
def flatten(m):
    return [m[x][y] for x in range(len(m)) for y in range(len(m[x]))]

# print(flatten([[1, 2], [3,4], [5,6]]))

def foo2():
    return [[(x, y) for x in range(4)] for y in range(4)]

print(foo2())


def identity(n):
    return [[int(x == y) for y in range(n)] for x in range(n)]

print(identity(3))