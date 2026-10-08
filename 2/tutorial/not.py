def NAND(a,b):
    return 1 if not (a and b) else 0

def NOT(a):
    return NAND(a, 1)

for i in range(2):
    print(f"{i} {NOT(i)}")