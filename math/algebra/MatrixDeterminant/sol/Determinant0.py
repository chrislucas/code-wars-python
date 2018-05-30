'''
https://pt.wikipedia.org/wiki/Teorema_de_Laplace
https://pt.wikipedia.org/wiki/Determinante
'''


# Regra de Sarrus
def det33(matrix):
    a1 = (matrix[0][0] * matrix[1][1] * matrix[2][2])
    b1 = (matrix[0][1] * matrix[1][2] * matrix[2][0])
    c1 = (matrix[0][2] * matrix[1][0] * matrix[2][1])

    a2 = (matrix[0][1] * matrix[1][0] * matrix[2][2])
    b2 = (matrix[0][0] * matrix[1][2] * matrix[2][1])
    c2 = (matrix[0][2] * matrix[1][1] * matrix[2][0])
    return (a1 + b1 + c1) - (a2 + b2 + c2)


def det3x3(matrix):
    a = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (
    matrix[0][2] * matrix[1][0] * matrix[2][1])
    b = (matrix[0][1] * matrix[1][0] * matrix[2][2]) + (matrix[0][0] * matrix[1][2] * matrix[2][1]) + (
    matrix[0][2] * matrix[1][1] * matrix[2][0])
    return a - b


# Regra de Sarrus
def det22(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# determinante matrix NxN
def det_nxn(matrix):
    # sempre vou escolher a primeira coluna
    '''
    first_column = [0] * len(matrix[0])
    # copiando a primeira coluna da matriz
    for x in range(0, len(first_column)):
        first_column[x] = matrix[x][0]
    '''
    first_column = matrix[0][0:len(matrix[0])]
    for x in range(0, len(first_column)):
        continue
    return 0


idx = 0
matrix_2x2 = [
    [[1, 10], [5, -1]]
]

matrix_3x3 = [
    [
        [-1, 2, 1]
        , [-4, 5, 1]
        , [0, -2, -1]
    ]
    , [
        [3, 1, 7]
        , [-1, 2, 1]
        , [0, -2, -1]
    ]
    , [
        [3, 1, 7]
        , [-1, 2, 1]
        , [-4, 5, 1]
    ]
    , [
        [0, 2, 1]
        , [3, 5, 1]
        , [1, -2, -1]
    ]
    , [
        [0, -1, 1]
        , [3, -4, 1]
        , [1, 0, -1]
    ]
    , [
        [0, -1, 1]
        , [3, -4, 1]
        , [1, 0, -1]
    ]
    , [
        [0, -1, 2]
        , [3, -4, 5]
        , [1, 0, -2]
    ]
]

matrix_nxn = [
    [
        [-2, 3, 1, 7]
        , [0, -1, 2, 1]
        , [3, -4, 5, 1]
        , [1, 0, -2, 1]
    ]
]
print(det22(matrix_2x2[idx]))
print(det33(matrix_3x3[3]))
print(det_nxn(matrix_nxn[0]))

if __name__ == '__main__':
    pass
