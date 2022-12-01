with open("input.txt", "r") as f:
    lines = f.readlines()

totSurface = 0
totLength = 0

for line in lines:
    surfaces = []
    line = line.strip().split('x')
    dimensions = [int(x) for x in line]
    dimensions.sort()

    surfaces.append(dimensions[0]*dimensions[1])
    surfaces.append(dimensions[0]*dimensions[2])
    surfaces.append(dimensions[1]*dimensions[2])
    totSurface += sum(surfaces)*2 + min(surfaces)

    totLength += 2*(dimensions[0]+dimensions[1])
    totLength += dimensions[0]*dimensions[1]*dimensions[2]


print("Solution (part 1): ", totSurface)
print("Solution (part 2): ", totLength)

