'''
http://www.codewars.com/trainer/python
DONE
'''

boards = [
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    ,
    [[5, 3, 4, 6, 7, 8, 9, 1, 2],
     [6, 7, 2, 1, 9, 0, 3, 4, 9],
     [1, 0, 0, 3, 4, 2, 5, 6, 0],
     [8, 5, 9, 7, 6, 1, 0, 2, 0],
     [4, 2, 6, 8, 5, 3, 7, 9, 1],
     [7, 1, 3, 9, 2, 4, 8, 5, 6],
     [9, 0, 1, 5, 3, 7, 2, 1, 4],
     [2, 8, 7, 4, 1, 9, 6, 3, 5],
     [3, 0, 0, 4, 8, 1, 1, 7, 9]]
]


def sumElements(_list):
    return sum(_list)


def validateRows(board):
    flag = True
    # validar soma de linhas
    for i in range(0, len(board)):
        if sumElements(board[i]) != 45:
            return False
    return True


def validateColumns(board):
    for i in range(0, len(board)):
        data = [0] * len(board)
        for j in range(0, len(board)):
            data[j] = board[i][j]
        if sumElements(data) != 45:
            return False
    return True


def validateSubMatrix(board):
    for i in range(0, len(board) - 2, 3):
        for j in range(0, len(board) - 2, 3):
            acc = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    acc += board[k][l]
            if acc != 45:
                return False
    return True


def containZero(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                return False
    return True

def containsDuplicateInRowOrColumn(board):
    # verify duplicates in row
    for i in range(0, len(board)):
        dictRow = {}
        dictColumn = {}
        for j in range(0, len(board)):
            if board[i][j] in dictRow:
                return False
            else:
                dictRow[board[i][j]] = True
            if board[j][i] in dictColumn:
                return False
            else:
                dictColumn[board[j][i]] = True
    return True

def validSolution(board):
    flag = validateRows(board) \
           and validateColumns(board) \
           and validateSubMatrix(board) \
           and containZero(board)\
           and containsDuplicateInRowOrColumn(board)
    return flag


print(validSolution(boards[0]))
print(validSolution(boards[1]))
