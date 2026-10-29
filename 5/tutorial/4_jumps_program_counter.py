n = int(input())

def binToDec(a):
    res = 0
    a = str(a)
    for i in range(len(a)):
        res *= 2
        res += int(a[i])
    return res

registers = [0, 0, 0, 0]
memory = [0] * 256

instructions = []
for i in range(n):
    bits = input()
    value = binToDec(bits)
    instructions.append(value)

index = 0
steps = 0
while True:
    steps += 1
    value = instructions[index]
    opcode = (value >> 12) & 0b1111
    rd = (value >> 10) & 0b11
    rs = (value >> 8) & 0b11
    imm = value & 0b11111111
    
    if opcode == 0:
        pass
    if opcode == 1:
        registers[rd] = imm
    if opcode == 2:
        registers[rd] = (registers[rd] + registers[rs]) & 0xFF
    if opcode == 3:
        registers[rd] = (registers[rd] - registers[rs]) & 0xFF
    if opcode == 4:
        registers[rd] = registers[rd] & registers[rs]
    if opcode == 5:
        registers[rd] = registers[rd] | registers[rs]
    if opcode == 6:
        registers[rd] = registers[rd] ^ registers[rs]
    if opcode == 7:
        registers[rd] = memory[imm]
    if opcode == 8:
        memory[imm] = registers[rd]
    
    if opcode == 9:
        index = imm
        continue
    if opcode == 10:
        # print(f'JZ R{rd} {imm}')
        if registers[rd] == 0:
            index = imm
            continue
    if opcode == 11:
        # print(f'JNZ R{rd} {imm}')
        if registers[rd] != 0:
            index = imm
            continue
    if opcode == 15:
        break
    
    index += 1

print(" ".join(list(map(str, registers))))
print(f"STEPS {steps}")