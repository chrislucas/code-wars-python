'''
http://www.codewars.com/kata/the-fibfusc-function-part-1/train/python
DONE
'''


def even_f(x, y):
    return (x + y) * (x - y), y * (2 * x + 3 * y)


def odd_f(x, y):
    return -y * (2 * x + 3 * y), (x + 2 * y) * (x + 4 * y)


def test(n):
    if n == 0:
        return 1, 0
    memo = [()] * (n+1)
    memo[0] = (1, 0)
    memo[1] = (0, 1)
    for i in range(2, n + 1):
        if (i & 1) == 0:
            p = i // 2
            aux_x, aux_y = memo[p]
            memo[i] = even_f(aux_x, aux_y)
        else:
            p = (i-1) // 2
            aux_x, aux_y = memo[p]
            memo[i] = odd_f(aux_x, aux_y)
    return memo[n]


def fibfusc(n):
    return test(n)


print(fibfusc(2))
print(fibfusc(3))
print(fibfusc(4))
print(fibfusc(5))

print(even_f(-1, 3)) # 4
print(odd_f(-1, 3)) # 5
print(odd_f(0, 1))

if __name__ == '__main__':
    pass
