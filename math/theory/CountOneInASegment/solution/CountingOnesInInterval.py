'''
dado um numero 'N' retorne um array de atamanho 'N'
onde o indice 'i' armazena a quantidade de 1 na repsentacao binaria
do i-esimoo numero
'''


def solver(n):
    _list = [0] * (n+1)
    _list[0] = 0
    _list[1] = 1
    for x in range(2, len(_list)):
        _list[x] = _list[x & (x-1)] + 1
    return _list


print(solver(100))