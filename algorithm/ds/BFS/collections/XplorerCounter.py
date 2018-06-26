'''
https://docs.python.org/2/library/collections.html#collections.Counter

Uma subclasse de dict para contar objetos que podemos gerar um numero hash.

Uma colecao nao ordenada que armazena os dados na forma de Mapa <chave, valor>. Segundo a documentacao
a classe Counter se Aseemelha a estruturas como Multisets ou Bags que existem em outras linguagens

'''
from collections import Counter

_counter_map = Counter({'a': 2, 'b': 3, 'c': 25, 'd': 33})

'''
Os N primeiros mais comuns
'''
print(_counter_map.most_common(3))

_counter_list = Counter([1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9, 9, 9, 10])

print(_counter_list.most_common(3))


def set_intersection(a, b):
    return a & b


def set_counter_addition(a, b):
    return a + b


def set_counter_union(a, b):
    return a | b


_set_intersection = set_intersection(Counter([1, 2, 3, 3]), Counter([1, 2, 3, 3, 4]))
_set_addition = set_counter_addition(Counter([1, 2, 3, 3]), Counter([1, 2, 3, 3, 4]))
_set_union = set_counter_union(Counter([1, 2, 3, 3, 3, 7, 7]), Counter([1, 2, 3, 3, 3, 3,  4, 5, 7, 8]))

print(_set_intersection)
print(_set_addition)
print(_set_union)

if __name__ == '__main__':
    pass
