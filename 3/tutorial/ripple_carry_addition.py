def full_adder(a, b, carry_in):
    return (a+b+carry_in) % 2, (a+b+carry_in) // 2

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
    res = add_bits(s[0], s[1])
    print(res[0], res[1])