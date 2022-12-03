import re

registers = {}

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    operations = parseInput(lines)
    result = run(operations)
    print("Solution (part 1): ", result)


    registers.clear()
    for line in lines:
        if re.search(r"(\d+) -> b\n", line) is not None:
            lines.remove(line)
            lines.append(str(result) + " -> b")
            break

    operations = parseInput(lines)
    result = run(operations)
    print("Solution (part 2): ", result)



def parseInput(lines):
    operations = []
    for line in lines:
        line = line.strip().split(' ')

        dest = line[-1]
        
        # assignment
        if len(line) == 3:
            src = getOperand(line[0])
            operations.append(Assignment(dest, src))
        
        # complement
        elif len(line) == 4:
            op1 = getOperand(line[1])
            operations.append(Complement(dest, op1))
        
        # operations with two operands
        elif len(line) == 5:
            op1 = getOperand(line[0])
            op2 = getOperand(line[2])
            
            if line[1] == "AND":
                operations.append(And(dest, op1, op2))
            elif line[1] == "OR":
                operations.append(Or(dest, op1, op2))
            elif line[1] == "LSHIFT":
                operations.append(LShift(dest, op1, op2))
            elif line[1] == "RSHIFT":
                operations.append(RShift(dest, op1, op2))
    return operations

def getOperand(op):
    if isinstance(op, int) or op.isnumeric():
        return int(op) 
    if op in registers:
        return registers[op]
    return op

def runOperation(op):
    if isinstance(op, Assignment):
        registers[op.dest] = getOperand(op.src1)
    elif isinstance(op, Complement):
        registers[op.dest] = getOperand(op.src1) ^ 0xFFFF
    elif isinstance(op, And):
        registers[op.dest] = getOperand(op.src1) & getOperand(op.src2)
    elif isinstance(op, Or):
        registers[op.dest] = getOperand(op.src1) | getOperand(op.src2)
    elif isinstance(op, LShift):
        registers[op.dest] = getOperand(op.src1) << getOperand(op.src2)
        registers[op.dest] &= 0xFFFF
    elif isinstance(op, RShift):
        registers[op.dest] = getOperand(op.src1) >> getOperand(op.src2)
        registers[op.dest] &= 0xFFFF

def run(operations):
    while len(operations) > 0:
        ready = [op for op in operations if op.hasNoParents()]

        for op in ready:
            runOperation(op)

        for x in operations:
            if x.hasOperand(op.dest):
                x.parents.remove(op.dest)
        operations.remove(op)
   
    return registers['a']

class Operation:
    def __init__(self, dest, src1, src2=None):
        self.parents = []
        self.dest = dest
        self.src1 = src1
        self.src2 = src2
        if not isinstance(src1, int):
            self.parents.append(src1)
        if src2 != None and not isinstance(src2, int):
            self.parents.append(src2)

    def hasOperand(self, op):
        return self.src1 == op or self.src2 == op

    def hasNoParents(self):
        return len(self.parents) == 0


class And(Operation):
    def __str__(self):
        return f"{self.src1} AND {self.src2} -> {self.dest}"

class Or(Operation):
    def __str__(self):
        return f"{self.src1} OR {self.src2} -> {self.dest}"

class LShift(Operation):
    def __str__(self):
        return f"{self.src1} LSHIFT {self.src2} -> {self.dest}"

class RShift(Operation):
    def __str__(self):
        return f"{self.src1} RSHIFT {self.src2} -> {self.dest}"

class Assignment(Operation):
    def __str__(self):
        return f"{self.src1} -> {self.dest}"

class Complement(Operation):
    def __str__(self):
        return f"NOT {self.src1} -> {self.dest}"
    


if __name__ == "__main__":
    main()

