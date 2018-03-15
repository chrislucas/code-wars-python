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


if __name__ == '__main__':
    pass