n = int(input())

left = [-1] * (n+1)
right = [-1] * (n+1)

for i in range(n):
    s = input().split()
    left[i] = int(s[1])
    right[i] = int(s[2])

diameter = 0

def height(n):
    global diameter
    if n == -1:
        return 0
    lh = height(left[n])
    rh = height(right[n])
    diameter = max(diameter, lh + rh)
    return 1 + max(lh, rh)

height(0)
print(diameter)