'''
https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python
'''


def determinant(matrix):
    return laplace_nxn(matrix, len(matrix[0]))


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
    [[1, 3], [2, 5]]
    , [[1]]
    , [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
    , [[3, -8, -7], [4, 9, 10], [7, 9, 5]]
    , [[-5, -5, 2, -2, -9, 7, -7, -6]
        , [-2, -8, -8, 4, 10, -7, -7, 5]
        , [-8, 10, 3, 9, -8, -5, 4, -7]
        , [3, 2, -2, 2, -5, 9, 7, 2]
        , [4, 1, 2, 0, -7, 1, -9, -6]
        , [-2, 9, 8, -6, 0, 10, 3, 2]
        , [1, 6, 4, 4, 6, 9, 7, -8]
        , [8, 4, 3, -9, 1, 1, 2, -2]]
    , [[6, 5, 0, 4], [-9, 0, 1, 2], [8, 3, -1, 9], [4, -3, 8, 5]]
    , [[-9, -2, 0, 9, 9, 0, 1]
        , [-7, 5, -9, 6, -1, 5, -9]
        , [6, -8, -6, -8, 5, 4, -7]
        , [3, -10, -9, 9, 2, 7, 3]
        , [-2, 0, 7, -4, -2, 9, 7]
        , [-9, -7, -2, 6, -4, -2, -9]
        , [9, 9, -7, 6, -8, 6, -10]]
    , [[10, -5], [9, 4]]
    , [[7, -10, -1, 2], [1, -3, 5, -3], [-1, 10, 7, -10], [-4, 7, 6, -3]]
]

print(determinant(matrix[8]))


if __name__ == '__main__':
    pass
