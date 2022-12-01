with open("input.txt", "r") as f:
    lines = f.readlines()

lines = lines[0]
floor = 0
inBasement = -1

for i in range(len(lines)):
    if lines[i] == "(":
        floor += 1
    elif lines[i] == ")":
        floor -= 1

    if floor < 0 and inBasement == -1:
        inBasement = i + 1

print("Solution (part 1): " + str(floor))
print("Solution (part 2): " + str(inBasement))