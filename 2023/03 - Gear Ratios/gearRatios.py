import math
import re

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    print(f"Solution (part 1): {part1(lines)}")
    print(f"Solution (part 2): {part2(lines)}")
    
def part1(lines):
    schematic = parseLines(lines)
    retval = 0

    for partNumber in schematic.partNumbers:
        #print()
        adjCells = schematic.getAdjacentCells(partNumber.row, partNumber.col, partNumber.col+partNumber.digits)
        #print(f"{partNumber.val}, row {partNumber.row}, col {partNumber.col}, len {partNumber.digits}")
        for cell in adjCells:
            #print(f"{schematic.rows[cell[0]][cell[1]]} ({cell[0]}, {cell[1]})")
            if schematic.isSymbol(cell[0], cell[1]):
                retval += partNumber.val
                break

    return retval

def part2(lines):
    schematic = parseLines(lines)
    retval = 0

    for gear in schematic.symbols:
        if gear.isGear():
            partNums = schematic.getAdjacentPartNumbers(gear.row, gear.col, gear.col)
            #print(f"\nrow {gear.row}, col {gear.col}, adjacent {len(partNums)}")
            if len(partNums) == 2:
                #print(f"{partNums[0].val}*{partNums[1].val}")
                retval += partNums[0].val*partNums[1].val
        
    return retval

def parseLines(lines):
    schematic = Schematic()
    lineNum = 0

    for line in lines:
        line = line.strip()
        schematic.rows.append(line)

        # find part numbers
        matches = re.finditer(r'\d+', line)
        for match in matches:
            partNumber = PartNumber(lineNum, int(match.start()), int(match.group()))
            schematic.partNumbers.append(partNumber)

        # find symbols
        for i in range(len(line)):
            c = line[i]
            if not (c.isnumeric() or c == '.'):
                symbol = Symbol(lineNum, i, c)
                schematic.symbols.append(symbol)

        lineNum += 1
    
    return schematic


class PartNumber:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.digits = math.floor(math.log10(val)+0.01)

class Symbol:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self. val = val

    def isGear(self):
        return self.val == '*'

class Schematic:
    def __init__(self):
        self.rows = []
        self.partNumbers = []
        self.symbols = []
    
    def getAdjacentCells(self, rowNumber, startPos, endPos):
        minRow = max(0, rowNumber-1)
        maxRow = min(len(self.rows)-1, rowNumber+1)
        minCol = max(0, startPos-1)
        maxCol = min(len(self.rows[0])-1, endPos+1)

        adjacentPositions = set()
        for i in range(minRow, maxRow+1):
            for j in range(minCol, maxCol+1):
                adjacentPositions.add((i, j))

        for j in range(startPos, endPos):
            adjacentPositions.remove((rowNumber, j))
        
        return adjacentPositions

    def getAdjacentPartNumbers(self, row, startPos, endPos):
        minRow = max(0, row-1)
        maxRow = min(len(self.rows)-1, row+1)
        minCol = max(0, startPos-1)
        maxCol = min(len(self.rows[0])-1, endPos+1)

        retval = [x for x in self.partNumbers if (minRow <= x.row <= maxRow) and ((minCol <= x.col <= maxCol) or (minCol <= x.col+x.digits <= maxCol))]
        return retval

    def isSymbol(self, row, col):
        val = self.rows[row][col]
        return not (val.isnumeric() or val == '.') 
    
    def partNumbersByRow(self, row):
        retval = [x for x in self.partNumbers if x.row == row]


if __name__ == "__main__":
    main()