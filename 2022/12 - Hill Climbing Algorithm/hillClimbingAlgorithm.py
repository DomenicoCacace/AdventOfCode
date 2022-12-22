def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    depths, start, end = parse(lines)
    
    path = dijkstra(depths, start, end)
    showPath(depths, path)
    print("Solution (part 1): " + str(len(path) - 1))
    path = bfs(depths, end, 1)
    showPath(depths, path)
    print("Solution (part 2): " + str(len(path) - 1))

    


def parse(lines):
    depths = []

    for line in lines:
        row = []
        line = line.strip()
        for c in line:
            if c == 'S':
                row.append(1)
                startPos = (len(depths), len(row) - 1)
            elif c == 'E':
                row.append(26)
                endPos = (len(depths), len(row) - 1)
            else:
                row.append(ord(c) - ord('a') + 1)
        depths.append(row)

    return depths, startPos, endPos

def getNeighbors(matrix, x, y, reverse=False):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(matrix) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(matrix[0]) - 1:
        neighbors.append((x, y + 1))

    ret = []
    for neighbor in neighbors:
        if reverse:
            if -(matrix[neighbor[0]][neighbor[1]] - matrix[x][y]) <= 1:
                ret.append(neighbor)
        else:
            if (matrix[neighbor[0]][neighbor[1]] - matrix[x][y]) <= 1:
                ret.append(neighbor)

    return ret


def dijkstra(matrix, start, end):
    dist = [[float('inf') for i in range(len(matrix[0]))] for j in range(len(matrix))]
    prev = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]
    dist[start[0]][start[1]] = 0

    q = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            q.append((i, j))

    while len(q) > 0:
        u = min(q, key=lambda x: dist[x[0]][x[1]])
        q.remove(u)

        if u == end:
            break

        for v in getNeighbors(matrix, u[0], u[1]):
            alt = dist[u[0]][u[1]] + 1
            if alt < dist[v[0]][v[1]]:
                dist[v[0]][v[1]] = alt
                prev[v[0]][v[1]] = u

    path = []
    u = end
    while u is not None:
        path.append(u)
        u = prev[u[0]][u[1]]

    return path[::-1]



def showPath(matrix, path):
    mat = [['.' for i in range(len(matrix[0]))] for j in range(len(matrix))]
    dirs = {(1, 0): 'v', (-1, 0): '^', (0, 1): '>', (0, -1): '<'}
    diff = lambda a, b: (a[0] - b[0], a[1] - b[1])
    for i in range (len(path) - 1):
        mat[path[i][0]][path[i][1]] = dirs[diff(path[i + 1], path[i])]
    
    mat[path[-1][0]][path[-1][1]] = 'E'
    for row in mat:
        print(''.join(row))


# find the shortest path from start to any node with value endval
def bfs(matrix, start, endval):
    q = [start]
    prev = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]
    explored = set()
    explored.add(start)
    while q:
        v = q.pop(0)
        if matrix[v[0]][v[1]] == endval:
            break
        for neighbor in getNeighbors(matrix, v[0], v[1], reverse=True):
            if neighbor not in explored:
                explored.add(neighbor)
                q.append(neighbor)
                prev[neighbor[0]][neighbor[1]] = v
    
    path = []
    u = v
    while u is not None:
        path.append(u)
        u = prev[u[0]][u[1]]

    return path[::-1]
    
            


if __name__ == "__main__":
    main()  