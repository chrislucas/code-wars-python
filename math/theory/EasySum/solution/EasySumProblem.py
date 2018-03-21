'''
https://a2oj.com/p?ID=155
'''


def exp_by_squaring(base, exp):
    if base == 1:
        return 1.0

    if exp < 0:
        base = 1 / base
        exp = -exp

    acc = 1
    while exp > 1:
        if (exp & 1) == 0:
            base *= base
            exp >>= 1
        else:
            acc *= base
            base *= base
            exp = (exp - 1) >> 1

    return acc * base


def modular_multiply(a, b, m):
    return ((a % m) * (b % m)) % m


def fast_modular_exponential(base, exp, m):
    if exp == 0:
        return 1
    acc = 1
    acc = 1
    while exp > 1:
        if (exp & 1) == 0:
            base = modular_multiply(base, base, m)
            exp >>= 1
        else:
            acc = modular_multiply(acc, base, m)
            base = modular_multiply(base, base, m)
            exp = (exp - 1) >> 1

    return modular_multiply(acc, base, m)


def run():
    cases = int(input())
    while cases > 0:
        n = int(input())
        print(fast_modular_exponential(2, n + 1, 33554431)-1)
        cases -= 1


run()

if __name__ == '__main__':
    pass
