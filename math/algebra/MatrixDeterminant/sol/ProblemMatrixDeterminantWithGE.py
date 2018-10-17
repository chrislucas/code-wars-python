'''
https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python
'''



def determinant(mat):
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
    return int(det)


print(determinant([[1, 3], [2, 5]]))
print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]))


print(determinant([[0, 2.6666666666666665, -4.666666666666666], [0, 0, -9.916666666666668], [0, 0, 0]]))

if __name__ == '__main__':
    pass
