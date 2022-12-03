with open("input.txt", "r") as f:
    lines = f.readlines()

niceStrings = 0
badSubstrings = ["ab", "cd", "pq", "xy"]

for line in lines:
    line = line.strip()

    vowels = 0
    doubles = 0
    noBadSubstrings = True
    if line[len(line)-1] in ['a', 'e', 'i', 'o', 'u']:
        vowels+=1
    for i in range(len(line)-1):
        if line[i:i+2] in badSubstrings:
            noBadSubstrings = False
            break
        if vowels < 3 and line[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels+=1
        if doubles <= 0 and line[i] == line[i+1]:
            doubles += 1


    if (vowels >= 3) and (doubles > 0) and noBadSubstrings:
        niceStrings += 1

print("Solution (part 1): ", str(niceStrings))

niceStrings = 0
for line in lines:
    pairs = {}
    letterInBetween = False
    pairOfLetters = False


    for i in range(len(line)-2):
        if not letterInBetween and line[i] == line[i+2]:
           letterInBetween = True
        if not pairOfLetters:
            pair = line[i:i+2]
            if pair in pairs:
                if pairs[pair] != i-1:
                    pairOfLetters = True
            else:
                pairs[pair] = i
        
    if letterInBetween and pairOfLetters:
        niceStrings += 1

print("Solution (part 2): ", str(niceStrings))
