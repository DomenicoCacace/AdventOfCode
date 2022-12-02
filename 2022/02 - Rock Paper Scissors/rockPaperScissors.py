with open("input.txt", "r") as f:
    lines = f.readlines()

score = 0
for line in lines:
    if line[2] == "X":
        score += 1
        if line[0] == "A":
            score += 3
        elif line[0] == "C":
            score += 6
    elif line[2] == "Y":
        score += 2
        if line[0] == "A":
            score += 6
        elif line[0] == "B":
            score += 3
    elif line[2] == "Z":
        score += 3
        if line[0] == "B":
            score += 6
        elif line[0] == "C":
            score += 3

print("Solution (part 1): ", str(score))

score = 0
for line in lines:
    # lose
    if line[2] == "X":
        if line[0] == "A":
            score += 3
        elif line[0] == "B":
            score += 1
        elif line[0] == "C":
            score += 2
    # draw
    elif line[2] == "Y":
        score += 3
        if line[0] == "A":
            score += 1
        elif line[0] == "B":
            score += 2
        elif line[0] == "C":
            score += 3
    # win
    elif line[2] == "Z":
        score += 6
        if line[0] == "A":
            score += 2
        elif line[0] == "B":
            score += 3
        elif line[0] == "C":
            score += 1

print("Solution (part 2): ", str(score))
