'''
https://www.codewars.com/kata/magnet-particules-in-boxes
Exercicio resolvido com o mesmo codigo so que em java pois
em python a funcao func_v falha em converter long int para float
'''


def doubles(maxk, maxn):
    # your code
    return total_force(maxk, maxn)


def func_v(k, n):
    return 1.0 / (k * pow((n + 1), (2 * k)))


def total_force(k, n):
    acc = 0
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            acc += func_v(i, j)
    return acc


#print("{:0.17f}".format(doubles(1, 3)))
#print("{:0.17f}".format(doubles(10, 100)))
#print("{:0.17f}".format(doubles(1, 10)))
#print("{:0.17f}".format(doubles(10, 1000)))
#print("{:0.17f}".format(doubles(10, 10000)))
#print("{:0.17f}".format(doubles(20, 10000)))
print("{:0.17f}".format(doubles(90, 10000)))

if __name__ == '__main__':
    pass
