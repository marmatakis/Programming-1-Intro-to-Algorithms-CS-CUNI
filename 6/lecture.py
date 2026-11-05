import math
from random import randrange

# l = [2, 4, 6, 8, 10]

# points = [(2, 3), (5, 6), (-1, -4), (1, 1)]

# total = 0
# for x,y in points:
#     total += math.sqrt(x**2 + y**2)
    
# print(total)

import matplotlib.pyplot as plt

dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

def walk(n):
    x, y = 0, 0
    xs, ys = [], []
    # idea with mod 2 and (-1)^n
    for i in range(n):
        dx, dy = dirs[randrange(4)]
        x += dx
        y += dy
        xs.append(x)
        ys.append(y)
        print(f'x = {x}, y = {y}')
        
    plt.plot(xs, ys)
    plt.show()

# walk(1000)

# def foo(x):
#     y = x + x
#     return

# print(foo(10))

x = 20      # global variable
y = 30      # 

def abc(z):
    q = z + x       # local variable
    global y
    y = 40
    return q

def avg(x, y, *a):
    print(a)
    return sum(a) / len(a)

# print(avg(10, 7 , 30, 40, 50))

def foo(x, y, z, a, b, c):
    return x + y + z + a + b + c

# print(foo(*[10, 7 , 30, 40, 50, 100]))

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #return True if this point is the origin
    def is_origin(self):
        return self.y == self.x == 0
    
    def distance(self, q):
        return sqrt((self.x - q.x) ** 2 +  (self.y - q.y) ** 2)

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def length(self):
        return self.start.distance(self.end)

p = Point(10, 10)
q = Point(12, 12)

l = Line(p, q)
print(l.length())

# p.x = 10
# p.y = 20
# print(type(p), p, p.x, p.y, p.is_origin(), p.distance(Point(4, 5)))
