t = input()

def compress(a):
    if len(a) <= 1:
        return a
    if a[0] == a[1]:
        return compress(a[1:])
    
    return a[0] + compress(a[1:])

print(compress(t))