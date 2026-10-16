s = input()
p = input()
res = ""
for i in range(len(s)):
    if s[i] == p:
        res += s[i]
    else:
        res += "*"
print(res)