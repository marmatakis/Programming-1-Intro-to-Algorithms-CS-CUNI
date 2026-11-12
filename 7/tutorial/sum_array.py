# ============================================================
# YOUR ASSEMBLY PROGRAM
# Edit only the text between the triple quotes.
# Input: memory[240] = N, memory[0..N-1] = array
# Output: memory[241] = array sum (mod 256)
# ============================================================

PROGRAM = """
# TODO: write your TinyCPU assembly here
LOAD R0, 240 # N
MOVI R1, 0 # i
MOVI R2, 0 # sum

repeat:
JZ R0, finish
LOADR R3, R1
ADD R2, R3

MOVI R3, 1
SUB R0, R3
ADD R1, R3
JMP repeat


finish:
STORE R2, 241
HALT
"""

import sys

OP={"NOP":0x0,"MOVI":0x1,"ADD":0x2,"SUB":0x3,"AND":0x4,"OR":0x5,"XOR":0x6,"LOAD":0x7,"STORE":0x8,"JMP":0x9,"JZ":0xA,"JNZ":0xB,"LOADR":0xC,"STORER":0xD,"HALT":0xF}

def _num(s):
    if s.startswith(("0x","0X")): return int(s,16)
    if s.startswith(("0b","0B")): return int(s,2)
    return int(s)

def _reg(s):
    v=int(s[1:])
    if not 0<=v<=3: raise ValueError('bad register')
    return v

def _clean(raw):
    line=raw.split('#',1)[0].strip()
    if not line: return None,[]
    label=None; rest=line
    if ':' in line:
        a,b=line.split(':',1); label=a.strip(); rest=b.strip()
    return label, rest.replace(',',' ').split() if rest else []

def _enc(op,rd=0,rs=0,imm=0):
    if not 0<=imm<=255: raise ValueError('immediate out of range')
    return ((op&15)<<12)|((rd&3)<<10)|((rs&3)<<8)|(imm&255)

def assemble(src):
    parsed=[_clean(x) for x in src.splitlines()]
    labels={}; addr=0
    for label,tok in parsed:
        if label is not None: labels[label]=addr
        if tok: addr+=1
    out=[]
    for _,t in parsed:
        if not t: continue
        op=t[0].upper()
        if op in ('NOP','HALT'): out.append(_enc(OP[op]))
        elif op=='MOVI': out.append(_enc(OP[op],rd=_reg(t[1]),imm=_num(t[2])))
        elif op in ('ADD','SUB','AND','OR','XOR','LOADR','STORER'): out.append(_enc(OP[op],rd=_reg(t[1]),rs=_reg(t[2])))
        elif op in ('LOAD','STORE'): out.append(_enc(OP[op],rd=_reg(t[1]),imm=_num(t[2])))
        elif op=='JMP': out.append(_enc(OP[op],imm=labels[t[1]] if t[1] in labels else _num(t[1])))
        elif op in ('JZ','JNZ'): out.append(_enc(OP[op],rd=_reg(t[1]),imm=labels[t[2]] if t[2] in labels else _num(t[2])))
        else: raise ValueError('unknown instruction '+op)
    return out

def run(program, initial_memory=None, max_steps=100000):
    r=[0,0,0,0]; m=[0]*256
    if initial_memory:
        for a,v in initial_memory.items(): m[a]=v&255
    pc=0; steps=0
    while True:
        if not 0<=pc<len(program): raise RuntimeError('PC outside program')
        if steps>=max_steps: raise RuntimeError('step limit')
        w=program[pc]; steps+=1
        op=(w>>12)&15; rd=(w>>10)&3; rs=(w>>8)&3; imm=w&255; npc=pc+1
        if op==0x0: pass
        elif op==0x1: r[rd]=imm
        elif op==0x2: r[rd]=(r[rd]+r[rs])&255
        elif op==0x3: r[rd]=(r[rd]-r[rs])&255
        elif op==0x4: r[rd]&=r[rs]
        elif op==0x5: r[rd]|=r[rs]
        elif op==0x6: r[rd]^=r[rs]
        elif op==0x7: r[rd]=m[imm]
        elif op==0x8: m[imm]=r[rd]
        elif op==0x9: npc=imm
        elif op==0xA:
            if r[rd]==0: npc=imm
        elif op==0xB:
            if r[rd]!=0: npc=imm
        elif op==0xC: r[rd]=m[r[rs]]
        elif op==0xD: m[r[rs]]=r[rd]
        elif op==0xF: break
        else: raise RuntimeError('unsupported opcode')
        pc=npc
    return r,m,steps


# ============================================================
# DO NOT MODIFY BELOW THIS LINE
# ReCodEx input/output adapter for Problem 4.
# ============================================================

def _cases():
    lines=[x.strip() for x in sys.stdin if x.strip()]
    return lines[1:1+int(lines[0])] if lines else []

def _prepare(line):
    p=[int(x) for x in line.split()]
    if 4==1: return {240:p[0]},241
    if 4==2: return {240:p[0],241:p[1]},242
    if 4==3: return {240:p[0]},241
    if 4==4:
        n=p[0]; vals=p[1:]; m={240:n}
        if len(vals)!=n: raise ValueError("Expected N array values")
        for i,v in enumerate(vals): m[i]=v
        return m,241
    if 4==5:
        n,target=p[:2]; vals=p[2:]; m={240:n,241:target}
        if len(vals)!=n: raise ValueError("Expected N array values")
        for i,v in enumerate(vals): m[i]=v
        return m,242

def main():
    program=assemble(PROGRAM)
    out=[]
    for case in _cases():
        initial,result_address=_prepare(case)
        _,memory,_=run(program,initial)
        out.append(str(memory[result_address]))
    sys.stdout.write("\n".join(out))

if __name__=="__main__":
    main()
