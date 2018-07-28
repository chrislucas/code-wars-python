# NESTED LIST
# https://snakify.org/en/lessons/two_dimensional_lists_arrays/

def test_list_1(_len):
    # uma lista com (_len) espacos
    table = [0] * _len
    for i in range(0, _len):
        # no i-esimo espaco adicione uma lista vazia
        table[i] = [0] * _len
        #
        table[i] = [x for x in range(i, 25)]
    return table


def test_list_2(_len):
    # neste caso [] * N retorna a referencia para uma lista de tamanho N
    # [[]] * N retorna uma referencia para N listas de tamanho zero
    table = [[]] * _len
    for i in range(0, _len):
        table[i].append([x for x in range(i, 25)])
    return table


def test_list_3(_len):
    # usando generator
    table = [[0] * _len for i in range(_len)]
    for i in range(0, _len):
        table[i] = [i for i in range(i, 25)]
    return table


for _list in test_list_1(10):
    print(_list)

if __name__ == '__main__':
    pass
