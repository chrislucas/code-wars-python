'''
https://en.wikipedia.org/wiki/Hamming_distance
'''

'''
Hamming distance pode nos dizer quantos bits precisam ser
trocados para transformar uma representacao binaria de a
em uma representacao binaria de b

Hamming weight e o numero de bits 1 num dado numero 'N'

'''


def count_flip_bits(a, b):
    a ^= b  # operador xor 'liga os bits' justamente na posicoes onde eles sao diferentes
    acc = 0
    while a > 0:
        a &= (a - 1)  # a & (a - 1) 'desliga' o bit menos significativo
        acc += 1
    return acc


print(count_flip_bits(15, 16))
print(count_flip_bits(7, 3))

if __name__ == '__main__':
    pass
