'''
https://www.geeksforgeeks.org/gaussian-elimination/
https://www.ime.unicamp.br/~marcia/AlgebraLinear/Arquivos%20PDF/algo_eliminacao.pdf
https://www.youtube.com/watch?v=QFGo3psJltw
http://prorum.com/index.php/3218/determinante-eliminacao-gaussiana-laplace-algoritmo-eficiente
'''

'''
https://pt.wikipedia.org/wiki/Matriz_estritamente_diagonal_dominante
'''


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


matrix = [
    [[5, 1, 2], [2, 6, 3], [3, 4, 7]]
]

print(is_strict_diagonal_dominant(matrix[0]))
