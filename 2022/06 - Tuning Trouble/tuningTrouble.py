with open("input.txt", "r") as f:
    lines = f.readlines()

lines = lines[0].strip()
startOfPacket = lines[0:4]

for i in range(4, len(lines)):
    if len(set(startOfPacket)) == 4:
        print("Solution (part 1):", str(i))
        break
    startOfPacket = startOfPacket[1:] + lines[i]

startOfPacket = lines[0:14]

for i in range(14, len(lines)):
    if len(set(startOfPacket)) == 14:
        print("Solution (part 2):", str(i))
        break
    startOfPacket = startOfPacket[1:] + lines[i]
