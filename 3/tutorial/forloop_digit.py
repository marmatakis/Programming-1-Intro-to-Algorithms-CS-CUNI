s = input()
digits = "0123456789"
broken = False
for item in s:
    if item in digits:
        print("ano")
        broken = True
        break
# if not broken:
#     print("")