'''
https://www.codewars.com/kata/total-primes/python
DONE
'''

from math import sqrt


def erasthotenes():
    n = 10000000
    flags = [True] * (n + 1)
    flags[0], flags[1] = False, False
    for i in range(2, int(sqrt(n) + 1)):
        if flags[i]:
            j = i
            while j * i <= n:
                flags[i * j] = False
                j += 1
    return flags


flags = erasthotenes()


def get_total_primes(a, b):
    # Happy coding!
    acc = 0
    for idx in range(a, b):
        flag = True
        if flags[idx]:
            ci = idx
            while ci >= 1:
                if flags[ci % 10]:
                    ci //= 10
                else:
                    flag = False
                    break
            if flag:
                acc += 1
    return acc


print(get_total_primes(50, 257))
print(get_total_primes(500, 600))
print(get_total_primes(523, 523))
print(get_total_primes(523, 556))
print(get_total_primes(0, 1))
print(get_total_primes(0, 2))
print(get_total_primes(10, 100))
print(get_total_primes(1, 10))
print(get_total_primes(523, 558))

if __name__ == '__main__':
    pass
