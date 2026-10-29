
def binarySearch(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low+high) // 2
        if x == l[mid]:
            return mid
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
    return -1

print(binarySearch(range(1, 100), 89))
    