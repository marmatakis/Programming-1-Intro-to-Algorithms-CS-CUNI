# 6
x = int(input('Enter n: '))
for n in range(x):
    s = ""
    while n > 0:
        d = n % 2
        n //= 2
        s = str(d) + s
    print(s)

# 7
n = int(input('Enter n: '))
s1 = 0
s0 = 0
while n > 0:
    d = n % 2
    if d == 0:
        s0 += 1
    if d == 1:
        s1 += 1
    n //= 2
if s1 > s0:
    print('heavy')
if s1 < s0:
    print('light')
if s1 == s0:
    print('balanced')

# 8
n = input('Enter n base 7: ')
res = 0
for d in n:
    res = res * 7 + int(d)
print("base 10:", res)

s = ""
while res > 0:
    d = res % 3
    res //= 3
    s = str(d) + s
print("base 3: ", s)

# 9 
n = int(input("Enter n: "))

rev = 0
while n > 0:
    d = n % 10
    n //= 10
    rev = rev * 10 + d
print("Reversed n: ", rev)
