'''
https://www.codewars.com/kata/bernoulli-numbers-1/train/python
'''

from fractions import Fraction


def fast_exp(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e < 0:
        b, e = 1 / b, -e
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc *= b
        b *= b
        e >>= 1
    return acc


'''
https://pt.wikipedia.org/wiki/N%C3%BAmeros_de_Bernoulli
'''


print(Fraction(1, 2))

if __name__ == '__main__':
    pass
