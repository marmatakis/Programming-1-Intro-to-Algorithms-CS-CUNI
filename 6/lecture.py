import random

def randArray(n):
    a = []
    for i in range(n):
        a.append(random.randint(1, n))
    return a

# Is an array sorted?
def is_sorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False    # not sorted
    return True

a = randArray(10)
print(a)
print(is_sorted(a))

def insertionSort(t: list):
    n = len(t)
    for i in range(n):
        x = t[i]
        j = i - 1
        # while t[j] > x:
        while j >= 0 and t[j] > x:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = x
    return t

# Compute n!
def fac_iter(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

print(fac(10), fac_iter(10))
print(insertionSort(a))

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def foo(n):
    if n == 0:
        return
    print(f' down {n}')
    foo(n-1)
    print(f' up {n}')
    
def a():
    print('a')
    return
def b():
    print('b')
    a()
    print('b')
def c():
    print('c')
    b()
    print('c')

# c()

def foo(n):
    print(n)
    foo(n+1)
# foo(1)


# Merge sorted arrays a and b into c
# Assume that len(c) = len(a) + len(b)
def merge(a, b, c):
    i = j = 0
    for k in range(len(c)):
        if i >= len(a):
            c[k] = b[j]
            j += 1
        elif j >= len(b):
            c[k] = a[i]
            i += 1 
        elif a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
    return c

def merge(a, b, c):
    i = j = 0
    for k in range(len(c)):
        if j >= len(b) or (i < len(a) and a[i] < b[j]):
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
    return c

def mergesort(a):
    print(a)
    if len(a) < 2:
        return
    
    mid = len(a) // 2
    b = a[:mid] # O(n)
    c = a[mid:] # O(n)
    mergesort(b)
    mergesort(c)
    
    return merge(b, c, a) # O(n)

print(mergesort(randArray(10)))

def abc(n):
    if n == 0:
        return 0
    return n + abc(n-1)
