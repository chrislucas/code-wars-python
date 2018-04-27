'''
Quantos bits sao necessarios inverter para converter 'a' em 'b'

a = 20, b = 10
10 = 001010
20 = 010100

bits trocados da direita para esquerda (1,2,3,4)

O operador xor nos ajuda a descobrir em quais bits divergem
dexiando nas posicoes de divergencia o bits '1'. Assim, basta
usar o a XOR b e contas os bits 1

'''


def count_needed_flips(a, b):
    a ^= b
    acc = 0
    while a > 0:
        a &= (a-1)
        acc += 1
    return acc


print(count_needed_flips(10, 20))
print(count_needed_flips(4, 7))
print(count_needed_flips(127, 128))

