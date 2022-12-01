with open("input.txt", "r") as f:
    lines = f.readlines()

maxCalories = [0, 0, 0]
currentElfCalories = 0

for line in lines:
    if line != "\n":
        currentElfCalories += int(line)
    else:
        if currentElfCalories > min(maxCalories):
            maxCalories[maxCalories.index(min(maxCalories))] = currentElfCalories
        currentElfCalories = 0

print("Solution (part 1): " + str(max(maxCalories)))
print("Solution (part 2): " + str(sum(maxCalories)))
