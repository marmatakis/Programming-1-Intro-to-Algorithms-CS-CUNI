def NAND(a,b):
    return 1 if not (a and b) else 0

def AND(a,b):                                                                                                                                                                                                       
    return NAND(NAND(a, b), 1)                                                                                                                                                                                        
                                                                                                                                                                                                                    
for i in range(4):                                                                                                                                                                                                  
    print(f"{(i&2)//2} {i&1} {AND((i&2)//2, i&1)}")    