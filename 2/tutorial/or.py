def NAND(a,b):
    return 1 if not (a and b) else 0

def OR(a,b):                                                                                                                                                                                                        
    return NAND(NAND(a,a), NAND(b, b))                                                                                                                                                                    
                                                                                                                                                                                                                    
for i in range(4):                                                                                                                                                                                                  
    print(f"{(i&2)//2} {i&1} {OR((i&2)//2, i&1)}")    