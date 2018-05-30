'''
http://www.techiedelight.com/count-set-bits-using-lookup-table/
https://www.geeksforgeeks.org/count-set-bits-integer-using-lookup-table/

Temuma lookup table de 64 bits
http://chessprogramming.wikispaces.com/Population+Count
'''

# 256
size_of_lookup_table = 0xff + 1


def get_lookup_table():
    lookup_table = [0] * size_of_lookup_table
    for i in range(0, len(lookup_table)):
        lookup_table[i] = (i & 1) + lookup_table[i // 2]
    return lookup_table


def count_bits(n):
    lookup_table = get_lookup_table()
    acc = 0
    i = 1
    while i <= n:
        acc += lookup_table[n & 0xff]
        # quebra o n nos 8 bits da direta para esquerda
        n >>= 8
    return acc


def count_bits_2(n):
    lookup_table = get_lookup_table()
    acc = 0
    if n < 0:
        n = (1 << 32) - 1
    # com o loop abaixonao precisamos nos preocurar com o tamanho do numero
    while n > 0:
        acc += lookup_table[n & 0xff]
        n >>= 8
    '''
        acc += lookup_table[(n >> 0) & 0xff]    # considerando os primeiros 8 bits da esquerda para direita
        acc += lookup_table[(n >> 8) & 0xff]    # remove 8 bits da direita de 'n' e verifica na tabela quantos bits 2 tem nesse numero
        acc += lookup_table[(n >> 16) & 0xff]   # remove 8 bits dos 
        acc += lookup_table[(n >> 24) & 0xff]
    '''
    return acc


# print(get_lookup_table())
# print([count_bits(x) for x in range(0, size_of_lookup_table)])


print(count_bits_2((1 << 32) - 1))
print(count_bits_2((1 << 32)))
print(count_bits_2(127127127127127))
print(count_bits_2(127127127127127127))
print(count_bits_2(127127127127127127127127127127))
print(count_bits_2(127127127127127127127127127127127))
print(count_bits_2(127127127127127127127127127127127127))
print(count_bits_2((1 << 70) - 1))
print(count_bits_2((1 << 80) - 1))

if __name__ == '__main__':
    pass
