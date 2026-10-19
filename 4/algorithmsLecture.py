# # What is the big-O running time of this program?

n = int(input("Enter n: "))

s = 0 # 1 * A
s += 10 # 1 * B
for i in range(n): # n * C
    s += i # n * D
    s += 4 # n * E
print(s)

# # total time = A + B + n * (C+D+E) = O(n)


# # What is the big-O running time of this program?
# O(n^2)

n = int(input("Enter n: "))

s = 0 # 1

# outer loop
for i in range(n): # n
    s += i # n
    # inner loop
    for j in range(n): # n
        s += i * j # n^2
        s += 10 # n^2

print(s)


n = int(input("Enter n: "))

while n > 0:
    print(n % 10) # last digit
    n = n // 10
    

n = int(input("Enter n: "))

prime = True
for i in range(2, n):
    if n % i:
        prime = False
        break
    
print(prime)

from math import sqrt
n = int(input("Enter n: "))
# Find all prime numbers <= n

prime = (n+1) * [True]
for i in range(2, int(sqrt(n)) + 1):
    for j in range(i+1, n+1):
        if j % i == 0:
            prime[j] = False
print(prime)

for i in range(len(prime)):
    if prime[i]:
        print(i)