# Return a list of all pythagorean triples a,b,c
# s.t. a < b < c < n and a^2 + b^2 = c^2

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def triples(n):
    return [
        (a,b,c)
        for a in range(n) for b in range(a + 1, n) for c in range(b + 1, n)
        if a**2 + b**2 == c**2 and gcd(a,b) == 1
    ]
    # improve this to sqrt()

x = [1,2,3,4]
print({y+1 for y in x})
print(triples(100))

print(set([x % 2 for x in range(1_000_000)]))
print({x % 2 for x in range(1_000_000)})

def table(n):
    # return len({a * b for a in range(n) for b in range(n)})
    return (n**2 - n)/ 2 + n

def table2(n):
    return len({a * b for a in range(n) for b in range(n)})
    # return (n**2 - n)/ 2 + n

# print(table(4))

import matplotlib.pyplot as plt

t = []
t2 = []
for i in range(100):
    t.append(table(i))
    t2.append(table2(i))

plt.plot(t, range(100))
plt.plot(t2, range(100))
plt.show()

print({x**2 : x**3 for x in range(10)})
x = {'a': 'b'}
r = {value: key for key, value in x.items()}
print(r)

def inc(x):
    return x + 1

def twice(f, x): # higher-order function
    return f(f(x))

# Apply f to x n times
def n_times(n, f, x):
    if n == 0:
        return x
    y = n_times(n-1, f, x)
    return f(y)

# print(n_times(5, inc, 5))

print(list(map(inc, [10, 20, 30])))

[x + 1 for x in [10, 20, 30]]

# Map f over the sequence a, returning a list
def map2(f, a):
    return [f(x) for x in a]

from math import sqrt
print(sum(map2(sqrt, range(1_000_000))))


def odd(x):
    return x % 2 == 1
print(list(filter( odd, [2,3,4,5,6,7,8])))

[x for x in [2,3,4,5,6,7,8] if odd(x)]

# return the value x in a for which f(x) is largest
def max_by(f, a):
    x = a[0]
    for i in range(1, len(a)):
        if f(a[i]) > f(x):
            x = a[i]
    return x

s = ['cat', 'horse', 'dog', 'wolf']
print(max_by(len, s), max(s, key=len))


# Sort the values in a using key function f
def sort_by(f, a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if f(a[j]) > f(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    
print(sorted(s, key=len))

print((lambda x: x + 2)(5))

print(sorted(s, key=lambda s: s[-1]))

# combine all letters in s, ignoring punctuation
def to_word(s):
    return "".join(filter(str.isalpha, s.lower()))

def frequent():
    count = {}
    for line in open('war_and_peace'):
        for w in line.split():
            w = to_word(w)
            count[w] = count.get(w, 0) + 1
            
    words = sorted(count.items(), key= lambda kv: kv[1], reverse=True)
    print(words[:10])
