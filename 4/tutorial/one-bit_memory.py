q = int(input())

current = "0"
next_val = "0"

for i in range(q):
    inp = input().split()
    if inp[0] == "READ":
        print(current)
    elif inp[0] == "TICK":
        current = next_val
    elif inp[0] == "WRITE":
        next_val = inp[1]