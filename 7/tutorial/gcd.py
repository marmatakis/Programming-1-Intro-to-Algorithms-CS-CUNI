inp = list(map(int, input().split()))
a, b = inp[0], inp[1]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(a, b))