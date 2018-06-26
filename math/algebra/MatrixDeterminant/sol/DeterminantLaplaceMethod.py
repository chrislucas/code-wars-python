from copy import deepcopy


# determinante matrix NxN
def laplace_method_cofactor(matrix):
    mat = deepcopy(matrix)
    if len(mat) == 1:
        return mat[0][0]
    else:
        acc = 0
        for k in range(0, len(mat)):
            val = laplace_method_cofactor(reduce_sub_matrix(mat, k))
            # mat[line][k] = multiplicando pelos elemento da primeria linha por padrao
            acc += mat[0][k] * val if (k & 1) == 0 else -(mat[0][k] * val) # acc += mat[0][k] * (-1) ** (2+k) * val
    return acc


def reduce_sub_matrix(matrix, i):
    mat = deepcopy(matrix)
    del mat[0]  # remove a primeira linha
    for j in range(0, len(mat)):
        del mat[j][i]  # remove a i-esima coluna
    return mat


matrix = [
    [
        [1, -2]
        , [1, 2]
    ]
    , [
        [1, 2, 3]
        , [1, -2, 3]
        , [1, 2, -3]
    ]
    , [
        [1, 2, 3, 5]
        , [1, -2, 3, 6]
        , [1, 2, -3, 7]
        , [1, 2, -3, -8]
    ]
]

print(laplace_method_cofactor(matrix[2]))

if __name__ == '__main__':
    pass
