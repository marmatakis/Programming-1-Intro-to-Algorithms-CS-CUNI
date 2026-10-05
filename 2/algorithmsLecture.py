# Determine if a number is a power of 10

n = int(input("Enter n: "))

# My solution, doesn't account for 1 = 10^0
while n >= 10:
    n -= 10 * (n // 10)
print(n)
if n != 0:
    print("no")
else:
    print("yes")

# proffesor's solution, 1 = 10^0 works correctly
while n % 10 == 0:
    n //=10
print(n)
if n == 1:
    print("power of 10")
else:
    print("not a power of 10")

# Determine if a number is a power of b
b = 2
n = int(input("Enter n: "))
while n % b == 0:
    n //= b
print(n)
if n == 1:
    print("power of", b)
else:
    print("not a power of", b)


# !! convert any base with any digits to base 10
# each step multiply the previous result by base and add current digit
b = int(input("Enter base: "))
d = input("Enter digits: ")
n = 0
for c in d: # loop over all digits
    n = b * n + int(c)
    print('n = ', n)
print('result =', n)

# convert n in base 10 to any base
b = int(input("Enter base: "))
n = int(input('Enter n: '))

s = '' # string result
while n > 0:
    d = n % b # get last digit in base b
    n //= b
    s = str(d) + s
print(s)