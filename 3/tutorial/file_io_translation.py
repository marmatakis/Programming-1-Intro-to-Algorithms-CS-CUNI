words = []
translation = []
with open("dictionary.txt", "r") as d:
    for line in d:
        line = line.split()
        words.append(line[0])
        translation.append(line[1])

inp = open("input.txt", "r")
output = open("output.txt", "w")
untranslated = []
for line in inp:
    line2 = line.split()
    out = ""
    for word in line2:
        if not word in words:
            if word not in untranslated:
                untranslated.append(word)
            continue
        line = line.replace(word, translation[words.index(word)])
    output.write(line)
untranslated.sort()
# if len(untranslated) != 0:
#     output.write("\n")
for item in untranslated:
    output.write(item)
    if untranslated.index(item) != len(untranslated) -1:
        print("writing new line")
        output.write("\n")
inp.close()
output.close()