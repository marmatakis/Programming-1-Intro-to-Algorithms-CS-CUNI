# 2

def append(*l):
    t = []
    for item in l:
        t += item
    return t

# print(append([1, 2], [5, 6], [8, 9]))

# 3
def my_max(*l):
    return max(*l)

# print(my_max([2,4,6]))

# 5
from math import sqrt, pi, acos

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #return True if this point is the origin
    def is_origin(self):
        return self.y == self.x == 0
    
    def distance(self, q):
        return sqrt((self.x - q.x) ** 2 +  (self.y - q.y) ** 2)

class Rectangle:
    def __init__(self, p : Point, q : Point):
        self.tl = p
        self.tr = Point(q.x, p.y)
        self.br = q
        self.bl = Point(p.x, q.y)
        self.width = self.tl.distance(self.tr)
        self.height = self.tl.distance(self.bl)
        
        print((self.tl.x, self.tl.y), (self.tr.x, self.tr.y),
              (self.bl.x, self.bl.y), (self.br.x, self.br.y), self.width, self.height)
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def contains(self, p : Point):
        # This function likely works only in one quarter of the x-y plane
        # More experimentation would have to commence in order to get a perfect result
        return (self.tl.x <= p.x <= self.tr.x) and (self.bl.y >= p.y >= self.tl.y)
    
    def intersets(self, s):
        return self.contains(s.tl) or self.contains(s.tr) or self.contains(s.bl) or self.contains(s.br)
    

# print(Rectangle(Point(0, 0), Point(2, 2)).intersets(Rectangle(Point(0, 0), Point(1.5, 1.5))))

# 6
class Circle:
    def __init__(self, p: Point, r):
        self.p = p
        self.r = r
    
    def area(self):
        return pi * (self.r**2)
    
    def circumference(self):
        return 2 * pi * self.r
    
    def contains(self, p: Point):
        return p.distance(self.p) < self.r
    
# print(Circle(Point(0,0), 1).contains(Point(0.5, 0.5)))

# 7
class Vector:
    def __init__(self, *m):
        self.m = m
        self.len = len(m)
    
    def add(self, w):
        newM = []
        for i in range(self.len):
            newM.append(self.m[i] + w.m[i])
        return Vector(newM)
    
    def mul(self, w):
        newM = []
        for i in range(self.len):
            newM[i] = self.m[i] * w
        self.m = newM
        return self
    
    def dot(self, w):
        product = 0
        for i in range(self.len):
            product += self.m[i] * w.m[i]
        return product
    
    def length(self):
        l = 0
        for i in range(self.len):
            l += self.m[i] ** 2
        return sqrt(l)
    
    def angle(self, w):
        return acos(
            self.dot(w) /
            (self.length() * w.length())
        )
    

# print(Vector(1, 2, 3).angle(Vector(2, 3, 4)))

# 8
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
class Date:
    def __init__(self, m, d):
        self.m = m
        self.d = d
    
    def next(self):
        if self.d + 1 > days[self.m]:
            self.m += 1
            self.d = 1
        else:
            self.d += 1
            
        if self.m > 12:
            self.m = 1
        return self
    
    def prev(self):
        if self.d - 1 == 0:
            self.m -= 1
            if self.m == 0:
                self.m = 12
            self.d = days[self.m]
        else:
            self.d -= 1
        return self
    
    def add(self, n):
        # for i in range(n): # Funny solution haha
        #     self = self.next()
        
        # TODO Unfinished solution, should come back to this
        n = n % 365
        for i in range(self.m, 13):
            diff = days[i] - self.d
            if diff < days[i]:
                self.d = diff
            else:
                self.d = 1
                self.m += 1
            if self.d == 0:
                self.d = 1
                self.m += 1
            print(self.d, self.m)
        
        return self

x = Date(3, 1).add(1832)
print(x.m, x.d)
