# 4 project euler
p = 0 # largest so far
for i in range(1000):
    for j in range(i, 1000):
        if str(i*j) == str(i*j)[::-1]:
            p = max(p, i*j)
print('the larget palindrome is', p)
import math
x = 14
print(f"{math.pi:.2f}")
print(str(math.pi)[:5])

import sys
count = 0
for line in sys.stdin:
    count += 1
    
print(count)

l = [3, 4, 8, 7, 9, 3, 4, 10]

# sum of items in list l
s = 0
for i in range(len(l)):
    s += l[i]
print(s)
s = 0
for item in l:
    s += item
print(s)

l = []
for x in range(10):
    l.append(x**2)
print(l)

l = [4]
while True:
    print(f'length = {len(l):,d}')
    l = l + l
