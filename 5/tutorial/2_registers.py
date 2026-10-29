q = int(input())

def binToDec(a):
    res = 0
    a = str(a)
    for i in range(len(a)):
        res *= 2
        res += int(a[i])
    return res

registers = [0, 0, 0, 0]

for i in range(q):
    bits = input()
    value = binToDec(bits)
    
    opcode = (value >> 12) & 0b1111
    rd = (value >> 10) & 0b11
    rs = (value >> 8) & 0b11
    imm = value & 0b11111111
    
    # print(opcode, rd, rs, imm)
    if opcode == 0:
        # print('NOP')
        pass
    if opcode == 1:
        # print(f'MOVI R{rd} {imm}')
        registers[rd] = imm
    if opcode == 2:
        # print(f'ADD R{rd} R{rs}')
        registers[rd] = (registers[rd] + registers[rs]) & 0xFF
    if opcode == 3:
        # print(f'SUB R{rd} R{rs}')
        registers[rd] = (registers[rd] - registers[rs]) & 0xFF
    if opcode == 4:
        # print(f'AND R{rd} R{rs}')
        registers[rd] = registers[rd] & registers[rs]
    if opcode == 5:
        # print(f'OR R{rd} R{rs}')
        registers[rd] = registers[rd] | registers[rs]
    if opcode == 6:
        # print(f'XOR R{rd} R{rs}')
        registers[rd] = registers[rd] ^ registers[rs]
        
    # if opcode == 7:
    #     print(f'LOAD R{rd} {imm}')
    # if opcode == 8:
    #     print(f'STORE R{rd} {imm}')
    # if opcode == 9:
    #     print(f'JMP {imm}')
    # if opcode == 10:
    #     print(f'JZ R{rd} {imm}')
    # if opcode == 11:
    #     print(f'JNZ R{rd} {imm}')
    # print(opcode)
    # if opcode == 15:
    #     print('HALT')
    #     break
    
    print(" ".join(list(map(str, registers))))