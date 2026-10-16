def full_adder(a, b, carry_in):
    return (a+b+carry_in) % 2, (a+b+carry_in) // 2

def NAND(a,b):
    return 1 if not (a and b) else 0

def NOT(a):
    return NAND(a, 1)

def invert_bits(a):
    s = ["0"] * len(a)
    for i in range(len(a)):
        s[i] = str(NOT(int(a[i])))
        # print(s)
    one = ("0" * (len(a)-1)) + "1"
    return add_bits("".join(s), one)[0]

def add_bits(a, b):
    a = a[::-1]
    b = b[::-1]
    # print(a, b)
    s = ["0"] * len(a)
    carry = 0
    for i in range(len(a)):
        a1 = int(a[i])
        b1 = int(b[i])
        res = full_adder(a1, b1, carry)
        s[i] = str(res[0])
        carry = int(res[1])
        # print(s, carry)
    return "".join(s)[::-1], carry
    
t = int(input())
for i in range(t):
    s = input().split()
    # res = add_bits(s[0], s[1])
    # print(res[0], res[1])
    inv = invert_bits(s[1])
    res = add_bits(s[0], inv)[0]
    print(res)
    