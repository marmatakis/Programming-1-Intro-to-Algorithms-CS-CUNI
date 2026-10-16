def half_adder(a, b):
    return (a + b) % 2, (a + b) // 2
    
n = int(input())
for i in range(n):
    s = input().split()
    res = half_adder(int(s[0]), int(s[1]))
    print(res[0], res[1])