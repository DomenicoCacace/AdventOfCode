import re

with open("input.txt", "r") as f:
    lines = f.readlines()

totalOverlap = 0
partialOverlap = 0

for line in lines:
    line = re.split(r"[\s,-]", line.strip())
    line = [int(x) for x in line]

    26-67,72-92

    if line[0] <= line[2] and line[1] >= line[3]:
        totalOverlap += 1
    elif line[2] <= line[0] and line[3] >= line[1]:
        totalOverlap += 1
    elif line[0] <= line[2] and line[1] <= line[3] and line[1] >= line[2]:
        partialOverlap += 1
    elif line[2] <= line[0] and line[3] <= line[1] and line[3] >= line[0]:
        partialOverlap += 1

print("Solution (part 1): ", str(totalOverlap))
print("Solution (part 1): ", str(totalOverlap + partialOverlap))

