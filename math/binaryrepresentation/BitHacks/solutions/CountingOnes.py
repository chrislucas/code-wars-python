'''
Tambem conhecido como Hamming weight a funcao abaixo conta
quantos bits 1 tem a representacao binarioa de 'N'

https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n/
'''


def hamming_weight(n):
    acc = 0
    while n > 0:
        n &= (n - 1)
        acc += 1
    return acc


def counting_ones_interval(n):
    return


if __name__ == '__main__':
    pass
