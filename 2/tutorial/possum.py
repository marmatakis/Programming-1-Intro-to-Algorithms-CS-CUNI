s = 0
while True:
    n = int(input())
    if n == -1:
        break
    if n > 0:
        s += n
print(s)