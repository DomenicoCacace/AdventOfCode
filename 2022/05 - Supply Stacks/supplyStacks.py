with open("input.txt", "r") as f:
    lines = f.readlines()

crates_1 = [[] for _ in range(len(lines[0])//4)]
crates_2 = [[] for _ in range(len(lines[0])//4)]

# separate the list when an empty line is found

for i in range(len(lines)):
    if lines[i] == "\n":
        lines = lines[i+1:]
        for i in range(len(crates_1)):
            crates_1[i].pop()
            crates_1[i].reverse()
            crates_2[i].pop()
            crates_2[i].reverse()
        break
    
    for j in range(0, len(lines[i]), 4):
        if lines[i][j:j+3] != "   ":
            crates_1[j//4].append(lines[i][j+1])
            crates_2[j//4].append(lines[i][j+1])

for m in lines:
    m = m.split()
    amount = int(m[1])
    fromCrate = int(m[3])-1
    toCrate = int(m[5])-1

    toMove = crates_1[fromCrate][-amount:]
    toMove.reverse()
    crates_1[fromCrate] = crates_1[fromCrate][:-amount]
    crates_1[toCrate].extend(toMove)

    toMove = crates_2[fromCrate][-amount:]
    crates_2[fromCrate] = crates_2[fromCrate][:-amount]
    crates_2[toCrate].extend(toMove)

sol1 = ""
sol2 = ""
for i in range(len(crates_1)):
    sol1 += crates_1[i][-1]
    sol2 += crates_2[i][-1]

print("Solution (part 1): ", sol1)
print("Solution (part 2): ", sol2)
