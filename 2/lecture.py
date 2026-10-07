# calculate factorial of n
n = int(input("Enter n: "))
f = 1
for x in range(1, n+1): # 1 ... n
    f *= x
    print('x =', x)
    if x == 3:
        break
print(n, '! is', f)


for x in range(0, 10, 2): # step by 2
    print(x)

# print 1+2+3+4+ ... +n = s
n = int(input("Enter n: "))
s = 0
o = ''
for i in range(n+1):
    s += i
    # if i == 4:
    #     continue
    o += str(i)
    if i == n:
        break
    o += ' + '
    
o += ' = ' + str(s)
print(o)

import math as m
# from math import * # not recommended 

# estimate pi by "hitting darts at a dartboard"
import random
n = int(input("Enter n: "))
hits = 0
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # print(x, y)
    if (x**2 + y**2) < 1:
        hits += 1
print(hits)
frac = hits / n
pi = frac * 4
print('fraction that hit=', frac)
print('pi ~=', pi)
    
# next character in unicode, relevant to caesar's cipher
# c = input('enter a letter: ')
# print('the next character in unicode is', chr(ord(c) + 1))

c = input('enter a letter (A- Z): ')
print('its position in the alphabet is #', ord(c) - 65)
