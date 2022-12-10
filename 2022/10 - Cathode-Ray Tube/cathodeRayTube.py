with open("input.txt", "r") as f:
    lines = f.readlines()

crt = [[' ' for _ in range(40)] for _ in range(6)]
crtRow = -1
strength = 0
clk = 1
X = 1

for line in lines:
    line = line.strip().split(' ')
    if line[0] == "addx":
        for _ in range(2):
            if (clk-1)%40 == 0:
                crtRow += 1
            if (clk-1)%40 in [X-1, X, X+1]:
                crt[crtRow][(clk-1)%40] = '#'
            if (clk+20) % 40 == 0:
                strength += X*clk
            clk += 1
        X += int(line[1])
    elif line[0] == "noop":
        if (clk-1)%40 == 0:
                crtRow += 1
        if (clk-1)%40 in [X-1, X, X+1]:
            crt[crtRow][(clk-1)%40] = '#'
        if (clk+20) % 40 == 0:
            strength += X*clk
        clk += 1

print("Solution (part 1):", strength)

print("Solution (part 2):")
for row in crt:
    print(''.join(row))

