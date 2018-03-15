'''
https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

y = 2 * x + 1, z = 3 * x + 1

[1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
[1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, 28, 31]
i -> idx1 idx2
0 -> 1, 2   = diff 1
1 -> 3, 5   = diff 2
2 -> 4, 6   = diff 3
3 -> 7, 10  = diff 3
4 -> 8, 12  = diff 4
5 -> 9, 13  = diff 4
6 -> 11, ?
7 -> 13, ?
'''


def utils_append(_list, n):
    if n not in _list:
        _flag = True
        for idx in range(0, len(_list)):
            if _list[idx] > n:
                _flag = False
                _copy_list = _list[idx:len(_list)]
                del _list[idx:len(_list)]
                _list.append(n)
                for x in _copy_list:
                    _list.append(x)
                break
        if _flag:
            _list.append(n)


def load(n):
    _local_list = [1, 3, 4]
    call = len(_local_list)
    ss(call, _local_list, n)
    return _local_list

_list = load(2000)


def solver(_list, n):
    call = len(_list)
    ss(call, _list, n)
    return _list[n]


def ss(call, _list, n):
    i, j = len(_list) - 2, len(_list) - 1
    while call < n:
        a, b = _list[i], _list[j]
        y = 2 * a + 1
        z = 2 * b + 1
        yy = 3 * a + 1
        zz = 3 * b + 1
        utils_append(_list, y)
        utils_append(_list, z)
        utils_append(_list, yy)
        utils_append(_list, zz)
        call += 1
        i = j + 1
        j = i + 1


def dbl_linear(n):
    if n < len(_list):
        return _list[n]
    else:
        return solver(_list, n)




print(dbl_linear(10))
print(dbl_linear(20))
print(dbl_linear(30))
print(dbl_linear(50))
print(dbl_linear(2300))
print(dbl_linear(1100))
print(dbl_linear(8038))
print(dbl_linear(229949974))


if __name__ == '__main__':
    pass
