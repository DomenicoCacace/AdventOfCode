def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    matrix = [[0 for x in range(len(lines[0].strip()))] for y in range(len(lines))]
    mask =   [[0 for x in range(len(lines[0].strip()))] for y in range(len(lines))]
    score =  [[0 for x in range(len(lines[0].strip()))] for y in range(len(lines))]

    for i in range(len(lines)):
        line = lines[i].strip()
        for j in range(len(line)):
            matrix[i][j] = int(line[j])

    for i in range(1, len(matrix)-1):
        mask[i] = setVisibilityMask(matrix[i])

    for i in range(1, len(matrix[0])-1):
        col = setVisibilityMask([matrix[k][i] for k in range(len(matrix))])
        for j in range(1, len(matrix)-1):
            mask[j][i] |= col[j]
            
    visible = (len(matrix[0])-1)*4 + countOnes(mask)
    print("Solution (part 1): ", visible)


    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            score[i][j] = countShorter(j, matrix[i])
            col = [matrix[k][j] for k in range(len(matrix))]
            score[i][j] *= countShorter(i, col)
    
    maxScore = 0
    # print the score matrix
    for i in range(len(score)):
        for j in range(len(score[i])):
            if score[i][j] > maxScore:
                maxScore = score[i][j]

    print("Solution (part 2): ", maxScore)



def countShorter(pos, row):
    p1 = 0
    for i in range(pos-1, -1, -1):
        p1 += 1
        if row[i] >= row[pos]:
            break
    p2 = 0
    for i in range(pos+1, len(row)):
        p2 += 1
        if row[i] >= row[pos]:
            break

    return p1*p2

def setVisibilityMask(row):
    mask = [0 for x in range(len(row))]
    maxInRow = row[0]
    for i in range(1, len(row)-1):
        if row[i] > maxInRow:
            maxInRow = row[i]
            mask[i] |= 1
    maxInRow = row[-1]
    for i in range(len(row)-2, 0, -1):
        if row[i] > maxInRow:
            maxInRow = row[i]
            mask[i] |= 1
    return mask

def countOnes(matrix):
    count = 0
    for j in range(1, len(matrix)-1):
        for i in range(1, len(matrix[j])-1):
            if matrix[j][i] == 1:
                count += 1
    return count

if __name__ == "__main__":
    main()

