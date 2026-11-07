q = int(input())

def binToDec(a):
    res = 0
    a = str(a)
    for i in range(len(a)):
        res *= 2
        res += int(a[i])
    return res

def decToBin(a, w):
    res = ""
    while a != 0:
        res = str(a % 2) + res
        a //= 2
    return ("0" * (w-len(res))) + res

registers = [0, 0, 0, 0]
memory = [0] * 256

codes = {"NOP" : 0, "MOVI": 1, "ADD": 2, "SUB": 3,
         "AND": 4, "OR": 5, "XOR": 6, "LOAD": 7, 
         "STORE": 8, "JMP": 9, "JZ": 10, "JNZ": 11, "HALT": 15}

address = 0
label_addresses = {}

inps = []
for i in range(q):
    inp = input().split()
    if inp[0][len(inp[0]) - 1] == ":":
        label_addresses[inp[0][:-1]] = int(address)
        continue
    address += 1
    inps.append(inp)

for inp in inps:
   
    cmd = inp[0]
    opcode = codes[cmd]
    rd = 0
    rs = 0
    imm = 0
    if cmd == "JMP":
        if inp[1] not in label_addresses:
            imm = int(inp[1])
        else:
            imm = int(label_addresses[inp[1]])
    if cmd in ["ADD", "SUB", "AND", "OR", "XOR"]:
        rd = int(inp[1][1:])
        rs = int(inp[2][1:])
    if cmd in ["MOVI", "LOAD", "STORE"]:
        rd = int(inp[1][1:])
        imm = int(inp[2])
    
    if cmd in ["JZ", "JNZ"]:
        rd = int(inp[1][1:])
        if inp[2] not in label_addresses:
            imm = int(inp[2])
        else:
            imm = int(label_addresses[inp[2]])
    
    value = (opcode << 12) | (rd << 10) | (rs << 8) | imm
    print(decToBin(value, 16))
    
    