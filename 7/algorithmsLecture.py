
# Solve the tower of Hanoi: move n discs 
# from peg (start) to peg (goal)

def solve(n, start, goal):
    # base case
    if n == 0:
        # print(f'move disc 1 from {start} to {goal}')
        return 0
    
    # recursive case
    other = 6 - start - goal
    m = solve(n-1, start, other) # move (n-1) to other
    # print(f'move disc {n} from {start} to {goal}')
    m += 1
    m += solve(n-1, other, goal)
    return m
    
# print(solve(64, start=1, goal=3))

from random import randrange

def nums(n):
    a = []
    for i in range(n):
        a.append(randrange(n))
    return a

# Choose a pivot p and partition a[lo:hi] into two
# partitions a[lo:k] and a[k:hi] such that
#   all elements in a[lo:k] are <= p
#   all elements in a[k:hi] are >= p
# return k
# Neither partition can be empty!

def partition(a, lo, hi):
    i = lo
    j = hi - 1
    p = a[randrange(lo, hi)]
    
    while True:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        
        if j <= i:
            return i
        
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

# Sort a[lo:hi] in place
def qsort(a, lo, hi):
    if hi - lo <= 1:
        return
    
    k = partition(a, lo, hi)
    qsort(a, lo, k)
    qsort(a, k, hi)
    
    return a
    
def quicksort(a):
    return qsort(a, 0, len(a))
    
a = nums(12)
print(a)
print(quicksort(a))