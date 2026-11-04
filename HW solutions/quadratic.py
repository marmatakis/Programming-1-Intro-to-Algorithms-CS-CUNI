'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
A = int(input())
B = int(input())
#X+Y=A
#x*y=B
#X = A-Y 
# (A-Y)*Y = B 
# (AY-Y^2) = B 
# B- AY + Y^2
# Y^2 - AY + B= 0
# A^2 - 4B >= 0
# A^2 >= 4B 


class Solution:
    def __init__(self, A, B):
        self.A = A 
        self.B = B 
    def solve(self):
        arr=set()
        if(A*A < 4*B):
            return arr
        det = A*A - 4*B
        l = 0
        r = 100000000009
        ans=0
        while(l<=r):
            mid=(l+r)//2
            if(mid*mid<=det):
                ans = (mid) 
                l = mid+1
            else:
                r = mid-1
       # print(ans)
        if(ans*ans != det):
            return arr
        # finding the nearest perfect square to the determinant using binary search 
        x1 = (A+ans)
        x2 = (A-ans)
        
        if((x1&1)==0):
            x1//=2 
            y1 = A - x1 
            arr.add(f"X = {x1}, Y = {y1}")
        if((x2 & 1)==0):
            x2//=2
            y2 = A - x2 
            arr.add(f"X = {x2}, Y = {y2}")
        return arr 

inst = Solution(A,B)
res = inst.solve()
if(len(res) == 0):
    print("No solution")
else:
    for s in res:
        print(s)