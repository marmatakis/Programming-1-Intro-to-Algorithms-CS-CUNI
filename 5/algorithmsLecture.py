
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    print(a, b)

gcd(108, 42)

# Return true if x is in a
def find(a, x):
    for i in range(len(a)):
        if x == a[i]:
            return True
    return False

# Given a _sorted_ array a, return the index of x,
# or if -1 if not found
def bsearch(a, x):
    n = len(a)
    lo = 0
    hi = n - 1
    
    while lo <= hi:
        mid = (lo + hi) 
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1 

print(bsearch(range(100), 98))

# Given an array of even numbers followed by odd,
# return the index of the first odd value.
def bsearch_odd(a):
    n = len(a)
    lo = 0
    hi = n - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] % 2 == 1: # a[mid] is odd
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

print(bsearch_odd([10, 2, 8, 6, 12, 14, 3, 1, 5, 7, 11, 101]))


# Given an array of sequential numbers, find the one that's missing
# Try this at home, not tested
def bsearch_seq(a):
    n = len(a)
    lo = 0
    hi = n - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == mid: # a[mid] value is equal to the indicy
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

import random
n = 100
# a = random.choices(range(1, n), k=n)

def bubble_sort(a):
    n = len(a)

    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(a):
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    

import time
import matplotlib.pyplot as plt

def test():
    times = []
    r = range(1_000, 15_000, 1_000)
    for n in r:
        a = random.choices(range(1, n), k=n)
        t = time.time()
        bubble_sort(a)
        u = time.time()
        print(f'n = {n}, time = {u - t}')
        times.append(u - t)
    plt.plot(r, times, label="Bubble")
    times = []
    for n in r:
        a = random.choices(range(1, n), k=n)
        t = time.time()
        selection_sort(a)
        u = time.time()
        print(f'n = {n}, time = {u - t}')
        times.append(u - t)
        plt.plot(r, times, label="Selection")
    plt.legend()
    plt.show()
test()