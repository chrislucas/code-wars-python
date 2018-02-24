#from functools import reduce
from math import ceil

def new_avg(arr, newavg):
    if len(arr) == 0:
        return newavg
    #summation = reduce(lambda x, y: x + y, arr)
    summation = sum(arr)
    if newavg <= summation // len(arr):
        raise ValueError
    else:
        return ceil(newavg * (len(arr) + 1 - summation))


print(new_avg([14, 30, 5, 7, 9, 11, 16], 90))
print(new_avg([14, 30, 5, 7, 9, 11, 15], 92))
print(new_avg([14, 30, 5, 7, 9, 11, 15], 2))

if __name__ == '__main__':
    pass
