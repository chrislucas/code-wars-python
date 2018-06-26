'''
https://docs.python.org/2/library/collections.html
'''

from collections import defaultdict


def test_init_dict_from_list():
    list_months = [
        ('jan', 1), ('fev', 1), ('mar', 1), ('abr', 1)
        , ('mai', 1), ('jun', 1), ('jul', 1), ('ago', 1)
        , ('set', 1), ('out', 1), ('nov', 1), ('dez', 1)
    ]
    dict_month = defaultdict(list)
    for k, v in list_months:
        dict_month[k].append(v)
    '''
        Uma diferenca interessante entre defaultdict e dict
        eh que nao precisamos nos preocupar se uma chave existe
        numa estrutura criada com ele, no caso do objeto dict, se
        tentarmos acessar um elemento de uma chave inexistente
        o programa lancara uma excecao
    '''
    print(dict_month['teste'])
    _dict = {}
    _dict['teste'] = 1
    if 'teste' in _dict:
        print(_dict['teste'])
    return


def test_init_dict_from_list_2():
    _list = [ ('a', 1), ('b', 2), ('b', 3), ('c', 3)]
    _dict = defaultdict(list)
    for k, v in _list:
        _dict[k].append(v)

    return

test_init_dict_from_list()

if __name__ == '__main__':
    pass
