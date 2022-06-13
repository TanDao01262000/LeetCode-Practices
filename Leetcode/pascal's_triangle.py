
import numpy as np

# Solution 1: recursive


def generate(numRows: int) -> list[list[int]]:

    if numRows == 1:
        return [1]
    elif numRows == 2:
        return [1, 1]
    else:
        i, j = 0, 1
        row = [0] * numRows
        row[0], row[numRows - 1] = 1, 1
        temp = generate(numRows - 1)
        for n in range(1, numRows - 1):
            row[n] = temp[i] + temp[j]
            i, j = i + 1, j + 1
        return row

# Solution 2: loop


def generate(self, numRows: int) -> List[List[int]]:
    res = [[1]]
    for i in range(numRows-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res


# Solution 3: dynamic program
def generate(numRows):
    table = [[1]] + [[1, 1]] + [[0]] * (numRows - 2)
    return generate_help(numRows, table)


def generate_help(numRows, table):
    if table[numRows - 1] != [0]:
        return table[0:numRows]

    i, j = 0, 1
    temp = [0] * numRows
    temp[0], temp[numRows - 1] = 1, 1
    for n in range(1, numRows - 1):
        temp[n] = generate_help(numRows - 1, table)[numRows - 2][i] + generate_help(numRows - 1, table)[numRows - 2][j]
        i, j = i + 1, j + 1

    table[numRows - 1] = temp
    return table[0:numRows]


for i in range(1, 11):
    print(generate(i))
