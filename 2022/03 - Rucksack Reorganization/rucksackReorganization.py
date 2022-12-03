with open("input.txt", "r") as f:
    lines = f.readlines()

priority = 0
for line in lines:
    line = line.strip()
    firstHalf = set(line[0:int(len(line)/2)])
    secondHalf = set(line[int(len(line)/2):])
    common = firstHalf.intersection(secondHalf)

    for c in common:
        if c.islower():
            priority += ord(c) - ord('a') + 1
        else:
            priority += ord(c) - ord('A') + 27

print("Solution (part 1): ", str(priority))

priority = 0
for i in range(0, len(lines), 3):
    s1 = set(lines[i+0].strip())
    s2 = set(lines[i+1].strip())
    s3 = set(lines[i+2].strip())
    common = s1.intersection(s2)
    common = common.intersection(s3)

    for c in common:
        if c.islower():
            priority += ord(c) - ord('a') + 1
        else:
            priority += ord(c) - ord('A') + 27

print("Solution (part 2): ", str(priority))


    

    

