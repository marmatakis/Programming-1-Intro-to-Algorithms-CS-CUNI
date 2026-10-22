# build a list with 1,000,000 elements

n = int(input("enter n: "))

l = []
for i in range(n):
    l.append(i)

print('built first list')

m = []
for i in range(n):
    m.insert(0, i) # insert i at the beginning

print('built second list')


m = []
for line in open('4/matrix.txt', 'r'):
    m.append(list(map(int, line.split())))

print(m)

# add 3 numbers
def add(x, y, z):
    return x + y + z
print(add(3, 4, 5))

# average of numbers in a list
def avg(l):
    s = 0
    for x in l:
        s += x
    return s / len(l)

print(avg([1,2,3,4,5,6,7,8]))

# Is a square matrix symmetric?
def symm(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[i][j]:
                return False
    return True

print(symm(m))

# Add two matrices

def matrix_add(m, n):
    m_height, m_width = len(m), len(m[0])
    n_height, n_width = len(n), len(n[0])
    assert m_height == n_height and m_width == n_width
    k = []
    for i in range(m_height):
        k.append([0] * m_width)
    print(m, k)
    for i in range(m_height):
        for j in range(m_width):
            k[i][j] = m[i][j] + n[i][j]
    return k

print(matrix_add(m, [[2, 4, 6], [6, 8, 12], [6, 18, 20]]))