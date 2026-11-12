
def my_max(a, b):
    # if a > b:
    #     return a
    # return b
    return a if a > b else b



import sys

# if len(sys.argv) < 2:
#     print(f'usage: {sys.argv[0]} <filename>')
#     exit()

# filename = sys.argv[1]
# lines = words = chars = 0

# for line in open(filename, 'r'):
#     lines += 1
#     words += len(line.split())
#     chars += len(line)
    
# print(f'{lines} lines, {words} words, {chars} chars')


def split(a, frac = 0.5):
    n = int(len(a) * frac)
    return (a[:n], a[n:])

# print(split([1,2,3,4,5,6], 0.2))

def foo(x, *, y, z):
    return 100*x + 10*y + z

# print(foo(3, 4, 5))

from random import randrange
import matplotlib.pyplot as plt

def gen(n):
    x = set()
    d = 0
    for i in range(n):
        y = randrange(n * n)
        if y in x:
            d += 1
        x.add(y)
    print(n, x, d)
    return d  
    

l = []
for n in range(5000):
    l.append(gen(n))
    print(l)
    
plt.plot(l)
plt.show()

d = {'cat': 'kocka', 'dog': 'pes', 'wolf': 'vlk'}
d['rabbit'] = 'kralik'
# print(d['dog'])

print(list(d.keys()))

# for v,k in d.items():
#     print(v, k)


# list(sorted(d.items()))

# count = {}

# for line in open('test.txt', 'r'):
#     for word in line.split():
#         if word not in count:
#             count[word] = 0
#         count[word] += 1

# pairs = []
# for word, n in count.items():
#     pairs.append((n, word))
# pairs.sort(reverse = True)


# for n, word in pairs[:10]:
#     print(f'{word}: {n}')