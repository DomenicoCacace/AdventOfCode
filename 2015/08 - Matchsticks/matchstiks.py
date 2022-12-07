with open("input.txt", "r") as f:
    lines = f.readlines()

totalDiff_dec = 0
totalDiff_enc = 0

for line in lines:
    line = line.strip()
    diff_dec = 2
    i = 1

    totalDiff_enc += 2 + line.count("\"") + line.count("\\")
    while i < len(line)-1:
        if line[i] == "\\":
            if line[i+1] == "\\" or line[i+1] == "\"":
                diff_dec += 1
                i += 1
            elif line[i+1] == "x":
                diff_dec += 3
                i += 3
        i+=1
    totalDiff_dec += diff_dec

print("Solution (part 1): ", totalDiff_dec)
print("Solution (part 2): ", totalDiff_enc)
