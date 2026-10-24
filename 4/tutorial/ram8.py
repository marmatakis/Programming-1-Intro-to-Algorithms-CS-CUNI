import sys

inp = list(map(int, input().split()))
w, q = inp[0], inp[1]
mem = []
for i in range(8):
    mem.append("0"*w)

def binToDec(a):
    res = 0
    a = str(a)
    for i in range(len(a)):
        res *= 2
        res += int(a[i])
    return res

for line in sys.stdin:
    line = line.split()
    # print(line)
    if line[0] == "WRITE":
        adr = binToDec(line[1])
        mem[adr] = line[2]
    elif line[0] == "READ":
        adr = binToDec(line[1])
        print(mem[adr])
    elif line[0] == "DUMP":
        print(" ".join(mem))