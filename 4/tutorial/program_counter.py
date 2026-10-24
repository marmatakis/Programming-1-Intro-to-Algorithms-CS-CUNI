inp = list(map(int, input().split()))
w, q = inp[0], inp[1]

m = 2**w - 1
pc = 0

# algorithms taught by Adam Dingle
def binToDec(a):
    res = 0
    a = str(a)
    for i in range(len(a)):
        res *= 2
        res += int(a[i])
    return res

def decToBin(a):
    res = ""
    while a != 0:
        res = str(a % 2) + res
        a //= 2
    return ("0" * (w-len(res))) + res

for i in range(q):
    command = input().split()
    if command[0] == "INC":
        pc += 1
    elif command[0] == "RESET":
        pc = 0
    elif command[0] == "LOAD":
        pc = binToDec(command[1])
    
    if pc > m:
        pc = 0
    print(decToBin(pc))
    