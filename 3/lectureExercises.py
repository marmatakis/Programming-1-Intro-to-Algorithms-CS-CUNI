# 1
import sys
words = 0
for line in sys.stdin:
    words += 1 # a bit unreliable method but whatever
    for c in line:
        if c == " ":
            words += 1

# 2
import sys
maxLength = 0
for line in sys.stdin:
    length = 0
    for c in line:
        if c == " ":
            length = 0
            continue
        length += 1
    maxLength = max(maxLength, length)
print(maxLength)

# 3
import random
l = []
while len(l) != 5:
    r = random.randint(1, 25)
    if r in l:
        continue
    l.append(r)
print(l)

# 4
import sys
maxLength = 0
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
freq = [0] * 26
total = 0
l = ""
maxL = 0
for line in sys.stdin:
    for c in line:
        for i in range(len(letters)):
            if c.upper() == letters[i]:
                freq[i] += 1
                if freq[i] > maxL:
                    maxL = freq[i]
                    l = letters[i]
                total += 1
print(f"Most frequent letter: {l} ({maxL})")
for i in range(len(letters)):
    letter = letters[i]
    amount = int((freq[i] * 100 / total) + 0.5)
    # interesting idea on how to round using just int and without round
    print(f"{letter}: {amount * "*"}")

# 5
import random
n = int(input("Enter N: "))
heard = []
while True:
    r = random.randint(1, n)
    if r in heard:
        print(f"Person {r} heard the rumor again")
        break
    heard.append(r)
    print(f"Person {r} heard the rumor.")
print(f"{len(heard)} people heard the rumor in all.")

# 6
import random
n = int(input("Enter an amount of visits N:"))
success = 0
fail = 0
games = []
for i in range(n):
    total = 100
    count = 0
    while True:
        if total <= 0:
            print(f"unsuccessful visit, lost 100 in {count} games")
            games.append(count)
            fail += 1
            break
        if total >= 200:
            print(f"successful visit, won 100 in {count} games")
            games.append(count)
            success += 1
            break
        r = random.randint(0, 1)
        count += 1
        if r == 0:
            total -= 10
            # print(f"lost -10, {total} left")
            continue
        total += 9
        # print(f"won +9, {total} left")
print(f"Percent of successful visits: {(success / (success+ fail) * 100):.2f}%")
print(f"Average amount of games: {(sum(games)/len(games)):.2f}")

# 7
import random
n = int(input("Enter an amount of simulations N:"))
lens = []
success = 0
fail = 0
for i in range(n):
    x = 0
    y = 0
    count = 0
    while True:
        if count != 0 and x == 0 and y == 0:
            print(f"Robot has won in {count} steps")
            lens.append(count)
            success += 1
            break
        if abs(x) + abs(y) >= 50:
            print(f"Robot has lost in {count} steps")
            lens.append(count)
            fail += 1
            break
        if random.randint(0, 1) == 0:
            if random.randint(0, 1) == 0:
                x -= 1
            else:
                x += 1
        else:
            if random.randint(0, 1) == 0:
                y -= 1
            else:
                y += 1
        count += 1
        # print(f"Position of the robot: ({x},{y})")
        
# print(f"Percent of successful simulations: {(success / (success+ fail) * 100):.2f}%")
# print(f"Average amount of steps: {(sum(lens)/len(lens)):.2f}")

# 8 - project Euler problem 8 solution
n = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
m = 0
for i in range(len(n)):
    s = 1
    if i + 13 > len(n) -1:
        break
    for j in range(i, i + 13):
        s *= int(n[j])
    m = max(m, s)
print(m)

# 9 - project Euler problem 9
print(200*375 *425)
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print(a,b,c)
print("finish")