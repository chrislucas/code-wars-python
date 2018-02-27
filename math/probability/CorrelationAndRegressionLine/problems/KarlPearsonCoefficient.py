'''
https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem

https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson
http://www.learningaboutelectronics.com/Articles/Slope-and-y-intercept-of-a-regression-line-calculator.php


Calculadora online
https://ncalculators.com/statistics/correlation-coefficient-calculator.htm

DONE
'''

from math import sqrt

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


def stddev(_list, _mean):
    acc = 0
    for x in _list:
        acc += (x - _mean) * (x - _mean)
    return sqrt(acc / (len(_list) - 1))


def pearson_correlation(_x, _y, _mean_x, _mean_y, stddev_x, stddev_y):
    acc, limit = 0, len(_x)
    for idx in range(0, limit):
        acc += (_x[idx] - _mean_x) * (_y[idx] - _mean_y)
    return acc / ((limit - 1) * stddev_x * stddev_y)


def solver_v1():
    _limit = len(physics)
    _mean_phy = sum(physics) / _limit
    _mean_his = sum(history) / _limit
    stddev_phy = stddev(physics, _mean_phy)
    stddev_his = stddev(history, _mean_his)
    return round(pearson_correlation(physics, history, _mean_phy, _mean_his, stddev_phy, stddev_his), 3)


print(solver_v1())

if __name__ == '__main__':
    pass
