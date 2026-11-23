# ============================================================
# YOUR PROGRAM
# ============================================================
# Input n is already on the data stack.

PROGRAM = r"""
CALL factorial
PRINT
HALT
factorial:
DUP
JZ base
DUP
PUSH 1
SUB
CALL factorial
MUL
RET
base:
POP
PUSH 1
RET
"""

# ============================================================
# DO NOT MODIFY BELOW THIS LINE
# ============================================================

def parse_program(source):
    raw=[line.strip() for line in source.splitlines() if line.strip()]
    labels={}; program=[]; address=0
    for line in raw:
        if line.endswith(':'): labels[line[:-1]]=address
        else:
            program.append(line); address+=1
    return program, labels

def run_vm(source, initial_stack=None):
    program,labels=parse_program(source)
    data_stack=list(initial_stack or []); call_stack=[]; output=[]; pc=0; steps=0
    while True:
        if steps>=100000: raise RuntimeError('Program did not halt')
        line=program[pc]; steps+=1; parts=line.split(); op=parts[0]; next_pc=pc+1
        if op=='PUSH': data_stack.append(int(parts[1]))
        elif op=='POP': data_stack.pop()
        elif op=='DUP': data_stack.append(data_stack[-1])
        elif op=='SWAP': data_stack[-1],data_stack[-2]=data_stack[-2],data_stack[-1]
        elif op in ('ADD','SUB','MUL'):
            b=data_stack.pop(); a=data_stack.pop()
            data_stack.append(a+b if op=='ADD' else a-b if op=='SUB' else a*b)
        elif op=='PRINT': output.append(str(data_stack[-1]))
        elif op=='JMP': next_pc=labels[parts[1]]
        elif op=='JZ':
            value=data_stack.pop()
            if value==0: next_pc=labels[parts[1]]
        elif op=='CALL':
            call_stack.append(pc+1); next_pc=labels[parts[1]]
        elif op=='RET': next_pc=call_stack.pop()
        elif op=='HALT': break
        else: raise ValueError(f'Unknown instruction: {op}')
        pc=next_pc
    return output

import sys

def main():
    data=sys.stdin.read().split()
    if not data: return
    t=int(data[0]); out=[]
    for i in range(t):
        result=run_vm(PROGRAM,initial_stack=[int(data[i+1])]); out.append(result[-1])
    sys.stdout.write('\n'.join(out))
if __name__=='__main__': main()