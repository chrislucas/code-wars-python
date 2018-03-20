'''
https://www.codewars.com/kata/greatest-common-divisor/train/python
DONE
'''


def mygcd2(x, y):
    while x % y >= 1:
        mod = x % y
        x = y
        y = mod
    return y


def mygcd(x, y):
    return y if x % y == 0 else mygcd(y, x % y)


print(mygcd(30, 12))
print(mygcd(8, 9))

if __name__ == '__main__':
    pass
