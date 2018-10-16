# https://en.wikipedia.org/wiki/Gaussian_elimination#Computing_determinants
# http://prorum.com/?qa=3218/determinante-eliminacao-gaussiana-laplace-algoritmo-eficiente
class Determinant:

    def __init__(self):
        pass

    @staticmethod
    def is_strict_diagonal_dominant(matrix):
        lin = len(matrix)
        col = len(matrix[0])
        if lin != col:
            return False
        else:
            for i in range(0, lin):
                acc = 0
                for j in range(0, col):
                    if i != j:
                        acc += matrix[i][j]

                if matrix[i][i] < acc:
                    return False
        return True

    def det_n_pivot(self, mat):
        det = 1
        limit_cols = len(mat[0])
        limit_line = len(mat)
        for i in range(0, limit_line):
            for j in range(i + 1, limit_line):
                # calcular qual o fator que vamos usar para multiplicar a linha abaixo do pivo
                f = mat[j][i] / mat[i][i] if mat[i][i] != 0 else 0
                for k in range(i + 1, limit_cols):
                    mat[j][k] = mat[j][k] - mat[i][k] * f
                # zerando os elementos abaixo da diagonal principal
                mat[j][i] = 0
            det *= mat[i][i]
        return det

    @staticmethod
    def _swap_rows(mat, i, j):
        for k in range(0, len(mat[0])):
            temp = mat[i][k]
            mat[i][k] = mat[j][k]
            mat[j][k] = temp

    def det_pivot(self, mat):
        det = 1
        limit_cols = len(mat[0])
        limit_line = len(mat)
        for i in range(0, limit_line):
            g_idx = i
            for j in range(i + 1, limit_line):
                if abs(mat[j][i]) > abs(mat[g_idx][i]):
                    g_idx = j
            if g_idx != i:
                self._swap_rows(mat, i, g_idx)
                det = -det
            for j in range(i + 1, limit_line):
                # calcular qual o fator que vamos usar para multiplicar a linha abaixo do pivo
                f = mat[j][i] / mat[i][i] if mat[i][i] != 0 else 0
                for k in range(i + 1, limit_cols):
                    mat[j][k] = mat[j][k] - mat[i][k] * f
                # zerando os elementos abaixo do pivo
                mat[j][i] = mat[j][i] - mat[i][i] * f
            # multiplicar o determinante pelos elementos da diagonal principal
            det *= mat[i][i]
        return det


from copy import deepcopy


def test():
    det = Determinant()
    mat = [
        [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]]
        , [[3.0, 2.0, -4.0], [2.0, 3.0, 3.0], [5.0, -3, 1.0]]
        , [[2, 1, -3, -1], [-1, 3, 2, 12], [3, 1, -3, 0]]
        , [[2, 1, 5], [-1, 1, 2]]
        , [[1, 1, 6], [-3, 1, 2]]
        , [[2, 1, -2, 3], [1, -1, -1, 0], [1, 1, 3, 12]]
        , [[1, 1, 3], [2, 2, 6]]
    ]

    print(det.det_pivot(deepcopy(mat[1])))
    print(det.det_n_pivot(deepcopy(mat[1])))


if __name__ == '__main__':
    test()
