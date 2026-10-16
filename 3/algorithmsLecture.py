n = int(input("Enter n: "))

# Is an prime?
# for n in range(1980, 2026):
prime = True
for i in range(2, n):
    if n % i == 0: # n is divisible by i
        # print(i, "is a factor of", n)
        prime = False
        break
if prime:
    print(n, "is prime")
else:
    print(n, "is not prime")
    
# look for the next prime number after n
from math import sqrt
while True:
    prime = True
    for i in range(2, int(sqrt(n))+1):
        if i > n*n:
            break
        if n % i == 0:
            prime = False
            break
    if prime:
        print(n, "is prime")
        break
    n += 1

n = int(input("Enter n: "))

# Find the prime factors of n using tirivial division !
i = 2
s = ""
while i*i <= n:
    if n % i == 0:
        s += str(i) + ' * '
        n = n // i
    else:
        i += 1
s += str(n)
print(s)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

# # Compute gc(a,b) !
while b != 0:
    print('a =', a, 'b =', b)
    a, b = b, a % b # simultaneous assignment
    
print(a)
    
