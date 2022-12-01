with open("input.txt", "r") as f:
    lines = f.readlines()
lines = lines[0]

visits = {}
visits["0,0"] = 1
i = 0
j = 0
for k in range(len(lines)):
    if lines[k] == "^":
        j += 1
    elif lines[k] == "v":
        j -= 1
    elif lines[k] == ">":
        i += 1
    elif lines[k] == "<":
        i -= 1

    idx = str(i) + "," + str(j)
    if idx in visits:
        visits[idx] += 1
    else:
        visits[idx] = 1

print("Solution (part 1): " + str(len(visits))) 

visits = {}
visits["0,0"] = 2
i_santa = 0
j_santa = 0
i_robot = 0
j_robot = 0
for k in range(0, len(lines), 2):
    if lines[k] == "^":
        j_santa += 1
    elif lines[k] == "v":
        j_santa -= 1
    elif lines[k] == ">":
        i_santa += 1
    elif lines[k] == "<":
        i_santa -= 1
    else:
        break

    idx = str(i_santa) + "," + str(j_santa)
    if idx in visits:
        visits[idx] += 1
    else:
        visits[idx] = 1

    if lines[k+1] == "^":
        j_robot += 1
    elif lines[k+1] == "v":
        j_robot -= 1
    elif lines[k+1] == ">":
        i_robot += 1
    elif lines[k+1] == "<":
        i_robot -= 1
    else:
        break

    idx = str(i_robot) + "," + str(j_robot)
    if idx in visits:
        visits[idx] += 1
    else:
        visits[idx] = 1

print("Solution (part 1): " + str(len(visits))) 
