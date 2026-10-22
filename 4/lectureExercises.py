
# 1
import time

n = int(input('Enter n: '))
print("start")
t = time.time()

a = []
for i in range(n): # runs n times
    a.append(i) # runs 1 time, simply allocates to available memory
    
print(f"executed 1 in {time.time() - t} seconds")

t = time.time()

a = []
for i in range(n): # runs n times
    a += [i] # runs 2 times, creates a new list in place of a
    
print(f"executed 2 in {time.time() - t} seconds")


# 2
import sys
words = [0] * 30
for line in sys.stdin:
    for word in line.split():
        words[len(word)] += 1

print(words)
words_sum = sum(words)
for i in range(len(words)):
    print(f"{i+1}: {"*" * (round(words[i] * 100 / words_sum))}")

# 3
import sys
m = 0
col = 0
cols = -1
for line in sys.stdin:
    cols += 1
    for num in list(map(int, line.split())):
        if num > m:
            m = num
            col = cols

print(f"Column {col} contains {m}.")

# 4
n = int(input("Enter n:"))
def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i != j:
                row.append("0")
                continue
            row.append("1")
        matrix.append(row)
    return matrix

m = identity_matrix(n)
for col in m:
    print(" ".join(col))

# 5
import sys
s = []
m = 0
for line in sys.stdin:
    line = list(map(int, line.split()))
    if len(s) == 0:
        s = [0] * len(line)
    m_row = 0
    for i in range(len(line)):
        num = line[i]
        m_row += num
        s[i] += num
    m = max(m, m_row)

m = max(m, max(s))
print(m)

# 6
def matrix_add(a, b):
    c = []
    for i in range(len(a)):
        row = a[i]
        c.append([0] * len(row))
        for j in range(len(a)):
            c[i][j] += a[i][j] + b[i][j]
    return c

print(matrix_add([[2, 4, 6], [6, 8, 12], [6, 18, 20]], [[2, 4, 6], [6, 8, 12], [6, 18, 20]]))

# 7
def matrix_multiply(a, b):
    c = []
    h = len(a)
    w = len(b)
    for i in range(h):
        c.append([0] * w)
    
    print(c)
    
    for i in range(h):
        print(a[i])
        for j in range(w):
            for x in range(w):
                c[i][j] += a[i][x] * b[x][j]
    return c
    
print(matrix_multiply([[1,3], [4,5], [6,7]], [[1,2], [3,4]]))
