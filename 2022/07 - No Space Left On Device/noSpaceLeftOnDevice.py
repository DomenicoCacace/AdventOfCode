def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    dirs = []
    currentDir = None
    for i in range(len(lines)):
        line = lines[i].strip()
        line = line.strip().split(" ")
        
        # command
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    currentDir = currentDir.parent
                else:
                    dirs.append(Directory(line[2], 0, currentDir))
                    if currentDir != None:
                        currentDir.addFile(dirs[-1])
                    currentDir = dirs[-1]

            elif line[1] == "ls":
                i += 1
                line = lines[i].strip().split(" ")
                while line[0] != "$" and line[0] != '':
                    if line[0] == "dir":
                        dirs.append(Directory(line[1], 0, currentDir))
                    else:
                        currentDir.addFile(File(line[1], int(line[0]), currentDir))
                    i += 1
                    line = lines[i].strip().split(" ")
                i -= 1  
    
    sol1 = 0
    dirSizes = []
    for dir in dirs:
        size = dir.getSize()
        dirSizes.append(size)
        if size <= 100000:
            sol1 += size

    sol2 = 0
    dirSizes.sort()
    free = 70000000 - dirSizes[-1]
    for i in range(len(dirSizes)):
        if free + dirSizes[i] >= 30000000:
            sol2 = dirSizes[i]
            break

    print("Solution (part 1):", sol1)
    print("Solution (part 2):", sol2)



def printDir(dir, depth=0):
    print("\t"*depth, " - ",  dir.name, "(dir)")
    depth += 1
    for file in dir.files:
        if isinstance(file, Directory):
            printDir(file, depth)
        else:
            print("\t"*depth, " - ", file.name, "(file, size=", file.size, ")")

class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def getSize(self):
        return self.size

class Directory(File):
    def __init__(self, name, size, parent):
        super().__init__(name, size, parent)
        self.files = []

    def addFile(self, file):
        self.files.append(file)

    def getSize(self):
        size = 0
        for file in self.files:
            size += file.getSize()
        return size

if __name__ == "__main__":
    main()

