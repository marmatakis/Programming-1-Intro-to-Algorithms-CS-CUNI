s = input()
n = int(input())
words = set()

for i in range(n):
    words.add(input())

def canBeBuilt(a, i=1):
    if a == "" or a in words:
        return True
    if i > len(a):
        return False
    if a[:i] in words and canBeBuilt(a[i:], 1):
        return True

    return canBeBuilt(a, i+1)

print("YES" if canBeBuilt(s) else "NO")