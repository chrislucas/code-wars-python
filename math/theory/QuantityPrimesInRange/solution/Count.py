from math import sqrt


def eratosthenes(n):
    flags = [True] * (n+1)
    flags[0], flags[1] = False, False
    for i in range(2, int(sqrt(n)+1)):
        if flags[i]:
            j = i
            while i*j <= n:
                flags[i * j] = False
                j += 1
    primes = []
    for i in range(0, len(flags)):
        if flags[i]:
            primes.append(i)

    return primes


def summation(n):
    flags = [True] * (n+1)
    flags[0], flags[1] = False, False
    for i in range(2, int(sqrt(n)+1)):
        if flags[i]:
            j = i
            while i*j <= n:
                flags[i * j] = False
                j += 1

    _summation = [0] * (n+1)
    for i in range(2, len(flags)):
        _summation[i] = _summation[i-1]
        if flags[i]:
            _summation[i] += 1

    return _summation

'''
print(len(eratosthenes(10)))
print(len(eratosthenes(100)))
print(len(eratosthenes(1000)))
print(len(eratosthenes(10000)))
print(len(eratosthenes(100000)))
print(len(eratosthenes(1000000)))
print(len(eratosthenes(10000000)))
print(len(eratosthenes(100000000)))
'''
_range = summation(100)
print(_range)
print("%d" % abs(_range[5] - _range[100]))
print("%d" % abs(_range[1] - _range[10]))
print("%d" % abs(_range[5] - _range[10]))


if __name__ == '__main__':
    pass
