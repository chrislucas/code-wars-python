'''
https://pt.wikipedia.org/wiki/Teorema_de_Laplace
http://calculous.com.br/?pid=88888888
'''


def laplace_2x2(matrix_2x2):
    return matrix_2x2[0][0] * matrix_2x2[1][1] - matrix_2x2[0][1] * matrix_2x2[1][0]


def laplace_3x3(matrix_3x3):
    _line_chosen = 0
    line = matrix_3x3[_line_chosen][0:len(matrix_3x3)]
    _lim = len(line)
    acc = 0
    for i in range(0, _lim):
        # usar list comprehesion -
        # https://stackoverflow.com/questions/9459337/assign-value-to-an-individual-cell-in-a-two-dimensional-python-array
        sub_matrix = [[None] * 2 for i in range(0, 2)]
        l = 0
        for j in range(0, _lim):
            # ignorar a linha escolhida na matriz original para ser eliminada
            if j == _line_chosen:
                continue
            c = 0
            for k in range(0, _lim):
                # como a matriz eh quadrada, i tbm pode representar a coluna
                # quando estivermos na i-esima linha, tbm ignoradamos o elemento da i-esima coluna
                if k == i:
                    continue
                sub_matrix[l][c] = matrix_3x3[j][k]
                c += 1
            l += 1
        det = laplace_2x2(sub_matrix)
        acc += line[i] * det if (i & 1 == 0) else -(line[i] * det)
    return acc


#
def laplace_nxn(_matrix, order, _line_chosen=0):
    if order < 1:
        return 0
    if order == 1:
        return _matrix[0][0]
    elif order == 2:
        return laplace_2x2(_matrix)
    elif order == 3:
        return laplace_3x3(_matrix)
    else:
        acc = 0
        for i in range(0, order):
            lin = 0
            sub_matrix = [[None] * (order - 1) for i in range(0, (order - 1))]
            for j in range(0, order):
                if j == _line_chosen:
                    continue
                col = 0
                for k in range(0, order):
                    if k == i:
                        continue
                    sub_matrix[lin][col] = _matrix[j][k]
                    col += 1
                lin += 1
            det = laplace_nxn(sub_matrix, order - 1, _line_chosen)
            acc += _matrix[_line_chosen][i] * det if (i & 1) == 0 else -(_matrix[_line_chosen][i] * det)
        return acc


matrix = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    , [[0, -1, 2], [3, -4, 5], [1, 0, -2]]
    , [[-2, 3, 1, 7], [0, -1, 2, 1], [3, -4, 5, 1], [1, 0, -2, 1]]
    , [[-2, 3, 1, 7], [0, -1, 2, 1], [3, -4, 5, 1], [1, 0, -2, -1]]
    , [
        [-2, 3, 1, 7, 1]
        , [0, -1, 2, 1, 1]
        , [3, -4, 5, 1, 1]
        , [1, 0, -2, -1, 1]
        , [1, 0, -2, -1, 1]
    ]
    , [
        [-2, 3, 1, 7, 1]
        , [0, -1, 2, 1, 1]
        , [3, -4, 5, 1, 1]
        , [1, 0, -2, -1, 1]
        , [-20, 3, 1, 7, 10]
    ]
    , [[1, 3], [2, 5]]
    , [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
    , [
          [20, 5, 3, 1, 2, 3]
        , [1, 2, -1, 1, 3, 7]
        , [1, 3, 4, 7, 5, 6]
        , [1, -2, -1, 1, 3, 70]
        , [2, 5, 3, 1, 2, 3]
        , [1, 3, 5, 6, 7, 8]
    ]
]

# print(laplace_3x3(matrix[1]))
# print(laplace_nxn(matrix[2], len(matrix[2][0]), 0))
# print(laplace_nxn(matrix[3], len(matrix[3][0]), 0))
# print(laplace_nxn(matrix[1], len(matrix[1][0]), 0))
# print(laplace_nxn(matrix[4], len(matrix[4][0]), 0))
# print(laplace_nxn(matrix[5], len(matrix[5][0]), 0))
# print(laplace_nxn(matrix[6], len(matrix[6][0]), 0))
# print(laplace_nxn(matrix[7], len(matrix[7][0]), 0))
print(laplace_nxn(matrix[8], len(matrix[8][0]), 0))

if __name__ == '__main__':
    pass
