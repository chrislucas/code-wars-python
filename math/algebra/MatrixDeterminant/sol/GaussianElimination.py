'''
https://www.geeksforgeeks.org/gaussian-elimination/
https://www.ime.unicamp.br/~marcia/AlgebraLinear/Arquivos%20PDF/algo_eliminacao.pdf
https://www.youtube.com/watch?v=QFGo3psJltw
http://prorum.com/index.php/3218/determinante-eliminacao-gaussiana-laplace-algoritmo-eficiente
'''

'''
https://pt.wikipedia.org/wiki/Matriz_estritamente_diagonal_dominante
'''



class GaussianElimination:

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

    def apply(self, mat):
        ans = self._forward_elimination(mat)
        # se a matriz for singular/nao invertivel (aii == 0)
        if ans != -1:
            '''
                Se o lado direito da equacao tem o valor 0, esse sistema
                tem infinitas solucoes, do contrario nao tem nenhuma
            '''
            if mat[ans][len(mat[0])-1] == 0:
                return []
            else:
                return None
        return self._back_substitution(mat)

    '''
        Aplicar o metodo de eliminacao: Consiste em zerar todos
        os elementos abaixo da diagonal principal
    '''

    def _forward_elimination(self, mat):
        # o limite eh a penultima coluna da matriz, pois a ultima eh o valor do lado direito da equacao
        limit = len(mat[0]) - 1
        # iteracao linha por linha da matriz
        for i in range(0, limit):
            # o maior elemento da coluna vai ser o i-esimo valor na diagonal principal
            ith_max, val_max = i, mat[i][i]
            # procurar o maior elemento da i-esima coluna
            for k in range(i + 1, limit):
                if abs(mat[k][i]) > val_max:
                    ith_max, val_max = k, mat[k][i]
            '''
                se o elemento pivo da i-esima coluna eh igual a zero
                a matriz eh singular
            '''
            if mat[i][ith_max] == 0:
                return i
            '''
                se o maior valor da i-esima coluna nao estiver na diagonal principal
                troque as linhas
            '''
            if ith_max != i:
                self._swap_rows(mat, i, ith_max)
            '''
                Procurar os (N-i) fatores 'f' que irao zerar todos os elementos
                abaixo do elemento pivo escolhido na i-esima coluna
            '''
            for k in range(i + 1, limit):
                # k = ao primeiro valor abaixo do pivo
                # para zerar os elementos da coluna abaixo do elemento pivo
                # dividimos o elemento que queremos zerar pelo pivo e assim descobrimos
                # qual o fator de multiplicacao que usaremos para zerar os elementos abaixo do pivo
                f = mat[k][i] / mat[i][i]
                # loop para alterar os elementos das linhas abaixo da linha do pivo, inclusive o ultimo
                # valor que corresponde o valor do lado direito da equacao linear
                for l in range(i + 1, limit + 1):
                    # multiplicar os numeros da linha do pivo pelo fator
                    # alterar as linhas abaixo da linha do elemento pivo
                    mat[k][l] = mat[k][l] - mat[i][l] * f
                # zerar o elemento abaixo do pivo (diagonal principal)
                mat[k][i] = 0
                # mat[k][i] = mat[k][i] - f * mat[i][i]
        return -1

    @staticmethod
    def _swap_rows(mat, i, j):
        for k in range(0, len(mat[0])):
            temp = mat[i][k]
            mat[i][k] = mat[j][k]
            mat[j][k] = temp

    '''
        Com a matriz escalonada reduzida em maos, resolva as equacoes
        da ultima ate a primeira para descobrir os valores dos coeficientes
        e ir substituindo nas equacoes anteriores
    '''

    @staticmethod
    def _back_substitution(reduced_echelon_form):
        limit = len(reduced_echelon_form[0]) - 1
        ans = [0] * limit
        for i in range(limit - 1, -1, -1):
            # lado direito da equacao linear
            ans[i] = reduced_echelon_form[i][limit]
            for j in range(i + 1, limit):
                # a incognita da equacao * seu coeficiente - o lado direito da equacao = valor na incognita da equacao anterior
                # que esta na linha anterior da matriz escalonada reduzida
                ans[i] = ans[i] - reduced_echelon_form[i][j] * ans[j]
            # para descobrir o valor da incognita da i-esima equacao
            # dividimos o coeficiente ao lado da incognita pelo valor do lado direito da equacao
            # Observar que as equacoes antes da ultima passam por um processo de subtracoes e substituicoes de incognitas
            # ate a ultima
            ans[i] /= reduced_echelon_form[i][i]
        return ans


def test_strict_diagonal_dominant():
    matrix = [[[5, 1, 2], [2, 6, 3], [3, 4, 7]]]
    print(GaussianElimination.is_strict_diagonal_dominant(matrix[0]))

# https://www.mathsisfun.com/algebra/systems-linear-equations.html
def test_gaussian_elimination():
    ge = GaussianElimination()
    mat = [
        [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]]
        , [[2, 1, -3, -1], [-1, 3, 2, 12], [3, 1, -3, 0]]
        , [[2, 1, 5], [-1, 1, 2]]
        , [[1, 1, 6], [-3, 1, 2]]
        , [[2, 1, -2, 3], [1, -1, -1, 0], [1, 1, 3, 12]]
        , [[1, 1, 3], [2, 2, 6]]
    ]
    ans = ge.apply(mat[0])
    if ans is None:
        print("Sistemas com infinitas solucoes")
    elif len(ans) == 0:
        print("Sistema Linear inconsistente")
    else:
        print(ans)


if __name__ == '__main__':
    test_gaussian_elimination()
