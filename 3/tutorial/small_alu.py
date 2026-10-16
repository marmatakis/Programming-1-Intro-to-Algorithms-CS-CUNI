def full_adder(a, b, carry_in):
    return (a+b+carry_in) % 2, (a+b+carry_in) // 2

def NAND(a,b):
    return 1 if not (a and b) else 0

def NOT(a, b=0):
    b = 0
    return NAND(a, 1)

def AND(a,b):                                                                                                                                                                                                       
    return NAND(NAND(a, b), 1)                                                                                                                                                                                        

def OR(a,b):                                                                                                                                                                                                        
    return NAND(NAND(a,a), NAND(b, b))                                                                                                                                                                    

def XOR(a,b):                                                                                                                                                                                                       
    return NAND(NAND(NAND(a,b), NAND(NAND(a, a), NAND(b, b))), 1)                                                                                                                                                                                                   

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
    if s[0] == "ADD":
        res = add_bits(s[1], s[2])
        zero = 0
        for i in range(len(res[0])):
            if res[0][i] == "0":
                zero += 1
        print(res[0], "1" if zero == len(res[0]) else "0")
        continue
    elif s[0] == "SUB":
        inv = invert_bits(s[2])
        res = add_bits(s[1], inv)
        zero = 0
        for i in range(len(res[0])):
            if res[0][i] == "0":
                zero += 1
        print(res[0], "1" if zero == len(res[0]) else "0")
        continue
    func = AND
    if s[0] == "OR":
        func = OR
    elif s[0] == "XOR":
        func = XOR
    elif s[0] == "NOT":
        func = NOT
        
    a = s[1]
    b = s[2]
    res = ["0"] * len(a)
    zero = 0
    for i in range(len(a)):
        res[i] = str(func(int(a[i]), int(b[i])))
        if res[i] == "0":
            zero += 1
    
    print("".join(res), "1" if zero == len(a) else "0")
    