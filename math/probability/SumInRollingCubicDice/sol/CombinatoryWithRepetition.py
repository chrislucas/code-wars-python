'''
https://www.geeksforgeeks.org/combinations-with-repetitions/
'''

'''
s - start idx
e - end idx
c - current idx
p - size of set
'''


def _combination(arr, chosen, s, e, c, p):
    if c == p:
        for i in range(0, p):
            print("%d " % (arr[chosen[i]]), end='')
        print("")
        return
    for i in range(s, e):
        chosen[c] = i
        _combination(arr, chosen, i, e, c + 1, p)


def combination(arr, p):
    chosen = [0] * p
    _len = len(arr)
    _combination(arr, chosen, 0, _len, 0, p)


def init(arr):
    _len = len(arr)
    for i in range(2, _len):
        combination(arr, i)
    return


#init([1, 2, 3, 4, 5, 6])
combination([1, 2, 3, 4, 5, 6], 3)

if __name__ == '__main__':
    pass
