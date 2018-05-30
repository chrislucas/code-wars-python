'''
https://en.wikipedia.org/wiki/Hamming_weight

Hamming weight de u numero na sua base binaria e a quantidade de bits 1 que esse numero possui
'''


def hamming_weight(n):
    acc = 0
    while n > 0:
        n &= (n - 1)
        acc += 1
    return acc


for x in range(0, 0x100):
    print("%d %d" % (x, hamming_weight(x)))

if __name__ == '__main__':
    pass
