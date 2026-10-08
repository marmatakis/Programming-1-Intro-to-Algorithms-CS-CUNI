def NAND(a,b):
    return 1 if not (a and b) else 0

def XOR(a,b):                                                                                                                                                                                                       
    return NAND(NAND(NAND(a,b), NAND(NAND(a, a), NAND(b, b))), 1)                                                                                                                                                                                                   
                                                                                                                                                                                                                    
for i in range(4):                                                                                                                                                                                                  
    print(f"{(i&2)//2} {i&1} {XOR((i&2)//2, i&1)}")