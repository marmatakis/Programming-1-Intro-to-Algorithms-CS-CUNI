inp = list(map(int, input().split()))
w, q = inp[0], inp[1]

register = "0" * w
next_val = "0" * w

for i in range(q):
    cmd = input().split()
    if cmd[0] == "READ":
        print(register)
    elif cmd[0] == "TICK":
        register = next_val
    elif cmd[0] == "LOAD":
        next_val = cmd[1]
