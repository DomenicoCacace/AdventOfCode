def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    monkeys = parse(lines)
    global GCD
    GCD = 1
    mods = set([m.mod for m in monkeys])
    for mod in mods:
        GCD = GCD * mod

    for _ in range(20):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items[0]
                item, dest = monkey.analyzeItem(item, anxiety=3)
                dest = monkeys[dest]
                monkey.throwTo(item, dest)

    # get the two max inspected values of the monkeys
    max1 = max(monkeys, key=lambda x: x.inspected)
    monkeys.remove(max1)
    max2 = max(monkeys, key=lambda x: x.inspected)
    monkeys.append(max1)
    print("Solution (part 1): ",max1.inspected*max2.inspected)

    monkeys = parse(lines)
    for _ in range(10000):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items[0]
                item, dest = monkey.analyzeItem(item, anxiety=1)
                dest = monkeys[dest]
                monkey.throwTo(item, dest)

    # get the two max inspected values of the monkeys
    max1 = max(monkeys, key=lambda x: x.inspected)
    monkeys.remove(max1)
    max2 = max(monkeys, key=lambda x: x.inspected)
    monkeys.append(max1)
    print("Solution (part 2): ",max1.inspected*max2.inspected)



def parse(lines):
    monkeys = []
    for i in range(0, len(lines), 7):
        items = lines[i+1].replace(",", "").strip().split()[2:]
        items = [int(item) for item in items]
        operand = lines[i+2].replace(",", "").strip().split()[-2]
        increment = lines[i+2].replace(",", "").strip().split()[-1]
        #check if numeric
        if increment.isnumeric():
            increment = int(increment)
        else:
            operand = '^'
            increment = 2
        mod = int(lines[i+3].replace(",", "").strip().split()[-1])
        ifTrue = int(lines[i+4].replace(",", "").strip().split()[-1])
        ifFalse = int(lines[i+5].replace(",", "").strip().split()[-1])
        
        m = Monkey(mod, ifTrue, ifFalse, operand, increment)
        m.items = items
        monkeys.append(m)
    return monkeys


class Monkey:
    id = 0
    def __init__(self, mod, ifTrue, ifFalse, op, increment):
        self.id = Monkey.id
        Monkey.id += 1
        self.items = []
        self.mod = mod
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.op = op
        self.increment = increment
        self.inspected = 0

    def throwTo(self, item, other):
        other.items.append(item)
        self.items.remove(item)
        #print("Throw {} from {} to {}".format(item, self.id, other.id))

    def analyzeItem(self, item, anxiety):
        idx = self.items.index(item)
        if self.op == '+':
            item = item + self.increment
        elif self.op == '*':
            item = item * self.increment
        elif self.op == '^':
            item = item * item
        item = item % GCD
        item = item//anxiety
        self.items[idx] = item
        self.inspected += 1
    
        return item, self.test(item)

    def test(self, item):
        if item % self.mod == 0:
            return self.ifTrue
        else:
            return self.ifFalse

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __repr__(self) -> str:
        return f"Monkey {self.id}: {self.items}, {self.inspected}"

        


if __name__ == "__main__":
    main()
