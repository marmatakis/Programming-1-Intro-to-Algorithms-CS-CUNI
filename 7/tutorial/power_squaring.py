inp = list(map(int, input().split()))
a, b = inp[0], inp[1]

def pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return pow(a, b // 2) ** 2
    else:
        return pow(a, b -1) * a

print(pow(a, b))