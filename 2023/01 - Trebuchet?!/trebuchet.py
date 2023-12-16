
def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    print(f"Solution (part 1): {part1(lines)}")
    print(f"Solution (part 2): {part2(lines)}")
    

def part1(lines):
    calib = 0
    for line in lines:
        d1 = 0
        d2 = 0
        for c in line:
            if c.isnumeric():
                d1 = int(c)
                break
        for c in reversed(line):
            if c.isnumeric():
                d2 = int(c)
                break
        
        calib = calib + d2 + d1*10
    return calib

def part2(lines):
    toSub = {'one':'o1e', 'two':'2to', 'three':'t3e', 'four':'f4r', 'five':'f5e', 'six':'s6x', 'seven':'s7n', 'eight':'e8h', 'nine':'n9e'}
    maxSize = 5

    newLines = []
    for line in lines:
        replaced = line

        found = False
        for i in range(len(replaced)-maxSize):
            if line[i].isnumeric():
                found = True
                break
            for word in toSub.keys():
                if word in replaced[i:i+maxSize]:
                    replaced = replaced.replace(word, str(toSub[word]))
                    found = True
                    break
            if found:
                break

        found = False
        for i in range(len(replaced)-maxSize, 0, -1):
            if line[i+maxSize-1].isnumeric():
                found = True
                break
            for word in toSub.keys():
                if word in replaced[i:i+maxSize]:
                    replaced = replaced.replace(word, str(toSub[word]))
                    found = True
                    break
            if found:
                break

        newLines.append(replaced)
        
    return part1(newLines)

if __name__ == "__main__":
    main()
