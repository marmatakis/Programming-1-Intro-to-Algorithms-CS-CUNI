import random

# 1
n = int(input("How many dice? "))
s = ""
t = 0
for i in range(n):
    r = random.randint(1, 6)
    s += str(r)
    t += r
    if i != n-1:
        s += " "
print(s)
print("total:", t)

# 2
s = ""
h = 0
count = 0
while h != 3:
    flip = "H" if random.randint(0, 1) == 0 else "T"
    s += flip
    if flip == "H":
        h += 1
    count += 1
print(s)
print(count, "flips")

# 3
n = int(input("Enter N: "))
for i in range(n):
    s = ""
    for j in range(n-i-1):
        s += " "
    for j in range(n-i, n+1):
        s += "*"
    print(s)

# 5
s = input("Enter string: ")
t = ""
for i in range(len(s)):
    t += s[i]
    if i != len(s) - 1:
        t += " "
print(t)

# 6
s = input("Enter string: ")
complete = False
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        complete = True
        print("double")
        break
if not complete:
    print("nothing")

# 7
c = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
     "n", "p", "q", "r", "s", "y", "t", "v", "w", "x", "z"]
v = ["a", "e", "i", "o", "u"]
# here since there are only 5 vowels we could in theory just
# random.randint and if the random is a vowel index then redraw
# we do not know lists yet :)
password = ""
for i in range(10):
    if i % 2 == 0:
        password += c[random.randint(0, len(c)-1)]
        continue
    password += v[random.randint(0, len(v)-1)]
print(password)

# 8 solution doesn't account for s = t, will not print anything
s = input("Enter S: ")
t = input("Enter T: ")

for i in range(len(s)):
    if ord(s[i]) > ord(t[i]):
        print(s)
        break
    elif ord(s[i]) < ord(t[i]):
        print(t)
        break

# 9
def startsWith(s, t):
    for i in range(len(t)):
        if s[i] != t[i]:
            return False
    return True
print(startsWith("abacus", "aba"))

# 10
s = input("Enter string: ")
found = False
for item in s:
    if item in v:
        print("vowels")
        found = True
        break
if not found:
    print("no vowels")

# 11
s = input("Enter string: ")
found = False
for letter in s:
    if ord(letter) > 128:
        print("unicode")
        found = True
        break
if not found:
    print("ascii")

# 12
s = input("Enter string: ")
result = ""
for i in range(len(s)):
    if i == 0:
        result += chr(ord(s[i])-32)
        continue
    if s[i-1] == " " and s[i] != " ":
        result += chr(ord(s[i])-32)
        continue
    result += s[i]
print(result)    