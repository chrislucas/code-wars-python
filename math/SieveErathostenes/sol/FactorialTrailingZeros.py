# https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/python
# https://brilliant.org/wiki/trailing-number-of-zeros/
# DONE
def fn(n):
    acc = 0
    i = 5
    while n//i >= 1:
        acc += n//i
        i *= 5
    return acc


print(fn(12))


if __name__ == "__main__":
    pass