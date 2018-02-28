'''
https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem

Pesquisar
slope of the line of regression

https://www.thoughtco.com/slope-of-regression-line-3126232
https://en.wikipedia.org/wiki/Simple_linear_regression

Como calcular o coeficiente de correlacao
https://www.thoughtco.com/how-to-calculate-the-correlation-coefficient-3126228


https://en.wikipedia.org/wiki/Correlation_coefficient
Correlation coefficient
'O coeficiente de correlacao nos diz o quao linear estao os pontos
num gráfico de dispersão'

Interpretação do coeficiente de correlação
http://leg.ufpr.br/~silvia/CE003/node74.html

r = correlation coefficient

Pontos importantes sobre 'r'

-> o valor de r está no intervalo -1 <= r <= 1

-> quando r = 0 indica que nao a correlacao linear entre as variaveis
-> quando r esta proximo de 1 implica que ha uma relacao linear positiva
entre as variaveis, a medida que x aumenta y tambem aumenta
-> quando r esta proximo de -1 implica que ha uma relacao linear negativa
entre as variaveis, a medida que x diminui y tambem diminui

Formula Slope Of Regression Line
https://www.chegg.com/homework-help/definitions/slope-of-regression-line-31

'''

'''
https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem
DONE
'''

from math import sqrt


def sample_standard_deviation(_list, _mean):
    acc = 0
    for xi in _list:
        acc += (xi - _mean) * (xi - _mean)
    return sqrt(acc / (len(_list) - 1))


physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


def correlation_coefficient(_x, _y, stddev_x, stddev_y, mean_x, mean_y):
    acc, limit = 0, len(_x)
    for idx in range(0, limit):
        acc += (_x[idx] - mean_x) * (_y[idx] - mean_y)
    p = acc / (stddev_x * stddev_y)
    return p / (limit - 1)


def solver_v1():
    limit = len(physics)
    _mean_phy = sum(physics) / limit
    _mean_his = sum(history) / limit
    stddev_phy = sample_standard_deviation(physics, _mean_phy)
    stddev_his = sample_standard_deviation(history, _mean_his)
    r = correlation_coefficient(physics, history, stddev_phy, stddev_his, _mean_phy, _mean_his)
    return round(r * (stddev_his/stddev_phy), 3)


def solver_v2():
    limit = len(physics)
    _mean_phy = sum(physics) / limit
    _mean_his = sum(history) / limit
    acc_a = 0
    for i in range(0, limit):
        acc_a += (physics[i] - _mean_phy) * (history[i] - _mean_his)
    acc_b = 0
    for i in physics:
        acc_b += (i - _mean_phy) * (i - _mean_phy)

    return round((acc_a / acc_b), 3)


print(solver_v1())
print(solver_v2())

if __name__ == '__main__':
    pass
