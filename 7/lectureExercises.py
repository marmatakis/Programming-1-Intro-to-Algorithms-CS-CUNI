# 1 
def my_max(*a):
    return max(*a)

# 2
import sys
words = {}
for line in sys.stdin:
    for word in line.split():
        if word not in words:
            words[word] = 0
        words[word] += 1
print(len(words))

# 3
def same_values(l, m):
    return set(l) == set(m)

print(same_values([1,2], [2,1]))

# 4 
n = int(input())
t = set()
for i in range(n):
    t.add(input())
    
m = int(input())
for i in range(m):
    word = input()
    if word in t:
        t.remove(word)
        print(word)

# 5
t = input()
letters = {}

for i in range(len(t)):
    if t[i] not in letters:
        letters[t[i]] = 0
    letters[t[i]] += 1

pairs = []
for letter, n in letters.items():
    pairs.append((n, letter))
pairs.sort(reverse=True)

for n, letter in pairs:
    print(f'{letter} {n}')

# 6
def combine(d : dict, e: dict):
    r = {}
    for x, y in d.items():
        if y not in e:
            continue
        z = e[y]
        if z:
            r[x] = z
    return r

d = { 'žába' : 'frog', 'kočka' : 'cat', 'kráva' : 'cow' }
e = { 'cow' : 'vaca', 'cat' : 'gato', 'dog' : 'perro' }

# print(combine(d, e))

# 7
# a.
# worst case - O(nlogn) + O(n)
# best case - O(n)
def hasDuplicates(a: list[int]):
    a.sort()
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return True
    return False

# b.
# worst case - O(n)
# best case - O(1)
def hasDuplicates2(a: list[int]):
    l = set()
    for item in a:
        if item in l:
            return False
        l.add(item)

# c.
# in both the worst and best, the 2nd algorithm will be much faster

# d.
import random
import time
def randList(n = 1_000_000, k = 1_000_000):
    l = []
    for i in range(n):
        l.append(random.randrange(k))
    return l

l = randList()
s = time.time()
hasDuplicates(l)
print(f'Time 1 - {time.time()-s}')
s = time.time()
hasDuplicates(l)
print(f'Time 2 - {time.time()-s}')

# Time 1 - 0.4033975601196289
# Time 2 - 0.04958319664001465

# The 2nd algorithm runs about 10 times as fast, impressive :)

# e.
def randList2(n = 1_000_000):
    l = []
    for i in range(n, 0, -1):
        l.append(i)
    return l

l = randList2()
s = time.time()
hasDuplicates(l)
print(f'Time 1 - {time.time()-s}')
s = time.time()
hasDuplicates(l)
print(f'Time 2 - {time.time()-s}')

# Time 1 - 0.08994746208190918
# Time 2 - 0.08582472801208496

# They are both about the same when elements are unique

# 8
a = randList(n=10_000, k=1_000_000_000)
b = set(randList(n=10_000, k=1_000_000_000))
print(a, b)
c = []
for item in a:
    if item in b:
        c.append(item)

print(len(c))

def same_dict(a: dict, b: dict):
    return set(a.values()) == set(b.values()) and set(a.keys()) == set(b.keys())

print(same_dict({ 10 : 20, 30 : 40 }, { 30 : 40, 10 : 20 }))
