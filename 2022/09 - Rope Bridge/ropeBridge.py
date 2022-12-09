def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    visited = set()
    rope = [(0,0) for x in range(2)]
    visited.add(rope[-1])

    for line in lines:
        direction, amount = line.strip().split(" ")
        amount = int(amount)
        rope = moveRope(rope, direction, amount, visited)
    #printVisited(visited)
    print("Solution (part 1): ", len(visited))

    visited = set()
    rope = [(0,0) for x in range(10)]
    visited.add(rope[-1])

    for line in lines:
        direction, amount = line.strip().split(" ")
        amount = int(amount)
        rope = moveRope(rope, direction, amount, visited)
    #printVisited(visited)
    print("Solution (part 2): ", len(visited))


def moveRope(rope, direction, amount, visited):
    directions = {'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}
    move = lambda x, y: (x[0] + y[0], x[1] + y[1])
    for _ in range(amount):
        rope[0] = move(rope[0], directions[direction])
        for node in range(len(rope)-1):
            if needsMoving(rope[node], rope[node+1]):
                dx = rope[node][0] - rope[node+1][0]
                dy = rope[node][1] - rope[node+1][1]
                rope[node+1] = move(rope[node+1], [x//(abs(x) or 1) for x in [dx, dy]])
        visited.add(rope[-1])
    return rope


def printVisited(grid):
    for y in range(30, -30, -1):
        for x in range(-30, 30):
            if (x,y) in grid:
                print("#", end="")
            else:
                print(".", end="")
        print()


def needsMoving(head, tail, radius=1):
    # determine if the tail is in a 3x3 grid around the head
    if head[0] - radius <= tail[0] <= head[0] + radius and head[1] - radius <= tail[1] <= head[1] + radius:
        return False
    return True



if __name__ == "__main__":
    main()
    