'''
http://www.codewars.com/kata/last-digit-of-a-large-number/train/python
DONE
'''


def modular_mult(a, b, m):
    return ((a % m) * (b % m)) % m


def fast_modular_exp(b, e, m):
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e < 0:
        b, e = 1 / b, -e
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc = modular_mult(acc, b, m)
        b = modular_mult(b, b, m)
        e >>= 1
    return acc


def last_digit(n1, n2):
    return fast_modular_exp(n1, n2, 10)


def run():
    print(last_digit(4, 1))
    print(last_digit(4, 2))
    print(last_digit(9, 7))
    print(last_digit(10, 10 ** 10))
    print(last_digit(2 ** 200, 2 ** 300))
    print(last_digit(3715290469715693021198967285016729344580685479654510946723,
                     68819615221552997273737174557165657483427362207517952651))


run()

if __name__ == '__main__':
    pass
