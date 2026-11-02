# 1 - random array
import random
import matplotlib.pyplot as plt
def generateRandomNAscending(n):
    t = []
    c = 0
    for i in range(n):
        c += random.randint(1, 10)
        t.append(c)
    return t

def generateRandomTo10N(n):
    t = []
    for i in range(n):
        t.append(random.randint(1, 10*n))
    return t

def binarySearch(t, a):
    lo = 0
    hi = len(t) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if t[mid] == a:
            return mid
        if t[mid] < a:
            lo = mid + 1
        elif t[mid] > a:
            hi = mid - 1
    return -1

vals = []
for i in range(100000):
    n = 100
    ascending = generateRandomNAscending(n)
    random10N = generateRandomTo10N(n)
    # print(ascending, random10N)
    count = 0
    for item in random10N:
        if binarySearch(ascending, item) != -1:
            print(item)
            count += 1
    print(count)
    vals.append(count)

plt.plot(vals)
plt.show()
print(vals, sum(vals) / 100000)
# The verdict is that we will probably see 10 on average if n is large, but a bit unclear why

# 2 - integer sqaure root
def findSquareRoot(n):
    lo = 0
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        square = mid ** 2
        if square == n:
            return mid
        if n > square:
            lo = mid + 1
        if n < square:
            hi = mid - 1
    return - 1

print(findSquareRoot(2500))

# 3 - missing number
s = [1, 2, 3, 4, 6, 7]

def findMissingFromN(t):
    lo = 0
    hi = len(t) - 1
    if t[0] != 1: # special case that fails for t[mid - 1] (mid is 0)
        return 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if t[mid] != mid + 1 and t[mid - 1] == mid:
            return mid + 1
        if t[mid] != mid + 1:
            print(t[mid], mid + 1)
            hi = mid - 1
        else:
            lo = mid + 1
    
    return -1

print(findMissingFromN(s))

# 4 - maximum comparisons
def maximumBinarySearchComparisons(n): # basically just log2(n)
    count = 0
    while n > 0:
        count += 1
        n //= 2
    return count

print(maximumBinarySearchComparisons(10000))

# 5 - ascending and descending
s = [4, 8, 10, 20, 37, 50, 52, 102, 7]

def findMaxInAscendingDecreasing(t):
    # first find where the sequence stops increasing
    lo = 0
    hi = len(t) - 1
    i = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if t[mid - 1] < t[mid] > t[mid + 1]:
            i = mid
            break
        if t[mid] > t[mid + 1]:
            hi = mid - 1
        elif t[mid - 1] < t[mid]:
            lo = mid + 1
    return t[i]

print(findMaxInAscendingDecreasing(s))

# 6 - infinite binary seaerch
s = []
for i in range(100):
    s.append((i+1) ** 3)
print(s)

def findSmallestVal(t, n):
    hi = 1
    lo = 0
    # first find a range lo-hi where n is contained
    while t[hi - 1] < n:
        lo = hi
        hi *= 2
        print(hi)
    
    # and then find the smallest t[mid] >= n
    while lo <= hi:
        mid = (lo + hi) // 2
        if t[mid - 1] < n and t[mid] >= n:
            return t[mid]
        if t[mid] > n:
            hi = mid - 1
        if t[mid] < n:
            lo = mid + 1
    return -1
    
print(findSmallestVal(s, 10000))

# 7 - adaptive bubblesort
s = generateRandomTo10N(100)
s.sort()
# best case now O(n), worst case still O(n^2)
def bubbleSort(t):
    n = len(t)
    for i in range(n-1, 0, -1):
        count = 0
        for j in range(i):
            if t[j] > t[j + 1]:
                count += 1
                t[j], t[j + 1] = t[j + 1], t[j]
        print(count)
        if count == 0:
            return t
    return t

print(s)
print(bubbleSort(s))

# 8 - selection moves
# maximum times an element might move is n-1
def selectionSort(t):
    n = len(t)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if t[j] < t[m]:
                m = j
        t[m], t[i] = t[i], t[m]
    return t

print(s)
print(selectionSort(s))
