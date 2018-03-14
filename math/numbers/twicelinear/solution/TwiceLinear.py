'''
https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python
'''


# 1, 2, 1, 3, 1, 4
def seq(n):
    acc = 0
    _list = []
    for x in range(1, n + 1):
        if (x & 1) == 1:
            _list.append(1)
        else:
            _list.append(x - acc)
            acc += 1
    return _list


def impl(a, b):
    return a * b + 1


def dbl_linear(n):
    call = 0
    _limit = (10 * n + 1)
    _list = [0] * _limit
    _list[0] = 1
    l = 0
    r = 1
    acc = 2
    while call <= n:
        y = impl(2, _list[call])
        z = impl(3, _list[call])
        if call & 1 == 0:
            l += 1
            r += 1
        else:
            l += acc
            r += acc + 1
            acc += 1
        _list[l] = y
        _list[r] = z
        call += 1
    return _list[n]


'''
print(dbl_linear(20))
print(dbl_linear(10))
print(dbl_linear(30))
print(dbl_linear(50))
'''
print(seq(18))

if __name__ == '__main__':
    pass
