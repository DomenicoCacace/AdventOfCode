with open("input.txt", "r") as f:
    lines = f.readlines()

lights = [[0 for x in range(1000)] for y in range(1000)]

for line in lines:
    line = line.strip().split(' ')
    if line[0] == "turn":
        line = line[1:]

    start = line[1].split(',')
    end = line[3].split(',')
    start = [int(x) for x in start]
    end = [int(x)+1 for x in end]

    if line[0] == "on":
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                lights[i][j] = 1
    elif line[0] == "off":
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                lights[i][j] = 0
    elif line[0] == "toggle":
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                lights[i][j] ^= 1

on = 0
for i in range(1000):
    for j in range(1000):
        on += lights[i][j]

print("Solution (part 1): ", on)

lights = [[0 for x in range(1000)] for y in range(1000)]

for line in lines:
    line = line.strip().split(' ')
    if line[0] == "turn":
        line = line[1:]

    start = line[1].split(',')
    end = line[3].split(',')
    start = [int(x) for x in start]
    end = [int(x)+1 for x in end]

    if line[0] == "on":
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                lights[i][j] += 1
    elif line[0] == "off":
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                lights[i][j] = max(0, lights[i][j]-1)
    elif line[0] == "toggle":
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                lights[i][j] += 2

brightness = 0
for i in range(1000):
    for j in range(1000):
        brightness += lights[i][j]

print("Solution (part 2): ", brightness)





