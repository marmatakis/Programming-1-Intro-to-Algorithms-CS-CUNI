letters = list(input())
letters.sort()

def permutations(letters):
    if len(letters) == 1:
        return [letters]

    result = []
    for i in range(len(letters)):
        current = letters[i]
        remaining = letters[:i] + letters[i+1:]
        for p in permutations(remaining):
            result.append([current] + p)
    return result


for p in permutations(letters):
    print("".join(p))