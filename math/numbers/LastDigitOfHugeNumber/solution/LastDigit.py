'''
http://www.codewars.com/kata/last-digit-of-a-huge-number/train/python
http://www.codewars.com/kata/last-digit-of-a-huge-number/train/python
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


def last_digit(_list):
    if len(_list) == 0:
        return 1
    elif len(_list) == 1:
        return _list[0] % 10
    else:
        _limit = len(_list) - 1
        rs = fast_modular_exp(_list[_limit - 1], _list[_limit], 10)
        for i in range(_limit-2, -1, -1):
            rs = fast_modular_exp(_list[i], rs, 10)
    return rs


def run():
    test_data = [
        #([], 1),
        #([0, 0], 1),
        #([0, 0, 0], 0),
        #([1, 2], 1),
        #([3, 4, 5], 1),
        #([4, 3, 6], 4),
        ([7, 6, 21], 1),
        ([12, 30, 21], 6),
        ([2, 2, 2, 0], 4),
        ([937640, 767456, 981242], 0),
        ([123232, 694022, 140249], 6),
        ([499942, 898102, 846073], 6)
    ]
    for test_input, test_output in test_data:
        rs = last_digit(test_input)
        print("%s %d" % ("True" if rs == test_output else "False", rs))


run()

#print(fast_modular_exp(11, 13, 19))
#print(fast_modular_exp(230, 13, 257))
#print(fast_modular_exp(2547, 13, 257))

if __name__ == '__main__':
    pass
