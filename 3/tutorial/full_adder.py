def full_adder(a, b, carry_in):
    return (a+b+carry_in) % 2, (a+b+carry_in) // 2

t = int(input())
carry = 0
res = 0
for i in range(t):
    s = input().split()
    res = full_adder(int(s[0]), int(s[1]), int(s[2]))
    print(res[0], res[1])
#     carry = res[1]
#     res = res[0]
# print(res, carry)
