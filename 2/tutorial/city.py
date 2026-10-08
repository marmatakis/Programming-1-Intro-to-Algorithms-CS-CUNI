import math

start1 = False
start2 = False
s1 = []
s2 = []
a = 0
b = 0
while True:
    s = input()
    if s == "# BEGIN TASK 1":
        start1 = True
        continue
    if s == "# END TASK 1":
        start1 = False
        s1.sort()
        s2.sort()
        for i in range(len(s1)):
            a += abs(s2[i] - s1[i])
        continue
    if s == "# BEGIN TASK 2":
        start2 = True
        continue
    if s == "# END TASK 2":
        
        ab = int(str(a) + str(b))
        gcd = math.gcd(ab, 162000)
        ab = ab // gcd
        den = 162000 // gcd
        # print(gcd, f"frac {ab} / {den}")
        res = 0
        while ab != 0:
            res += ab % 10
            ab //= 10
        while den != 0:
            res += den % 10
            den //= 10
        print(a)
        print(b)
        print(res)
        
        start2 = False
        break
    s = s.split()
    if start1:
        s1.append(int(s[0]))
        s2.append(int(s[1]))
    
    if start2:
        s = list(map(int, s))
        prev = 0
        inc = (s[1] - s[0]) > 0
        if inc:
            prev = s[0] - 1
        else:
            prev = s[0] + 1
        # print(inc)
        safe = True
        for item in s:
            diff = item - prev
            # print(item, diff)
            if (diff > 0 and not inc) or (diff < 0 and inc):
                safe = False
                break
            if abs(diff) > 3 or diff == 0:
                safe = False
                break
            prev = item
        if safe:
            b += 1
        # print(s, safe)
