def get_pos_rms(n):
    from math import log2
    return int(log2(n - (n & (n - 1))))


def get_pos_rms2(n):
    n = n - (n & (n - 1))
    acc = 0
    while n & 1 == 0:
        acc += 1
        n >>= 1
    return acc


print("%d %d" % (get_pos_rms(10), get_pos_rms2(10)))
print("%d %d" % (get_pos_rms(12), get_pos_rms2(12)))
print("%d %d" % (get_pos_rms(16), get_pos_rms2(16)))
print("%d %d" % (get_pos_rms(3), get_pos_rms2(3)))
print("%d %d" % (get_pos_rms(128), get_pos_rms2(128)))


if __name__ == '__main__':
    pass
