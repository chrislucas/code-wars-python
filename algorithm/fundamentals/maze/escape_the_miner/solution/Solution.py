'''
http://www.codewars.com/kata/escape-the-mines/train/python
DONE
'''

_maps = [
    [
        [True, False], [True, True]
    ]
    , [
        [True]
    ]
    ,
    [
        [True, False], [True, True]
    ]
    , [
        [True], [True], [True], [True]
    ]
    ,
    [
        [True, True, True, True, True],
        [True, False, True, False, True],
        [False, True, True, True, False],
        [True, False, False, True, True],
        [True, True, True, True, False]
    ]
    , [
        [True], [True], [True], [True]
    ]
]

miner = [
    {'x': 0, 'y': 0}
    , {'x': 0, 'y': 0}
    , {'x': 0, 'y': 0}
    , {'x': 0, 'y': 0}
    , {'x': 0, 'y': 4}
    , {'x': 3, 'y': 0}
]
_exit = [
    {'x': 1, 'y': 1}
    , {'x': 0, 'y': 0}
    , {'x': 1, 'y': 0}
    , {'x': 3, 'y': 0}
    , {'x': 3, 'y': 0}
    , {'x': 0, 'y': 0}
]


def goal(current_local, g_local):
    return current_local['x'] == g_local['x'] and current_local['y'] == g_local['y']


'''
    A matriz que representa o labirinto desse exercicio e diferente da maioria
    dos exercicios de percurso num labirinto, ela esta rotacionada em 90 graus no sentido horario
    , ou seja a primeira linha da matriz representa o lado direito do labirinto
'''
steps = ['up', 'down', 'left', 'right']


def solve(_map, miner, _exit):
    # your code here
    valid_path = [miner]
    path = []

    dim_x = len(_map)
    dim_y = len(_map[0])

    # memorizando o caminho que ja foi feito
    _memo_map = [[False] * dim_y for i in range(0, dim_x)]

    # esquerda, direita, cima, baixo
    possible_movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # BFS no mapa para achar um caminho de saida do labirinto
    idx = 0
    while len(valid_path) > 0:
        current_state = valid_path[0]
        valid_path.pop(0)
        if not goal(current_state, _exit):
            # verificar possiveis caminhos a partir de um ponto no labitindo
            _memo_map[current_state['x']][current_state['y']] = True
            flag = False
            for i in range(0, len(possible_movements)):
                xx = current_state['x'] + possible_movements[i][0]
                yy = current_state['y'] + possible_movements[i][1]
                if (0 <= xx < dim_x) and (0 <= yy < dim_y) and _map[xx][yy] and not _memo_map[xx][yy]:

                    local = {'x': xx, 'y': yy}
                    li = valid_path
                    valid_path = [local] + li

                    # adicionando o local alcancado, o local de onde eu vim e a direcao
                    data = (local, current_state, steps[i])
                    if data not in path:
                        path.append(data)
                    flag = True

            # se a partir de um determinado local na matriz chegamos a um caminho sem saida
            if not flag:
                for i in range(0, len(path)):
                    child = path[i][0]
                    parent = path[i][1]
                    if current_state['x'] == child['x'] and current_state['y'] == child['y']:
                        # vamos adicionar informar que por esse caminho nao podemos ir
                        _map[child['x']][child['y']] = False
                        # voltamos na memoria e marcamos o ultimo passo alcancado como se nao tivessemos pasado por ele
                        # _memo_map[parent['x']][parent['y']] = False
                        # removemos o caminho inviavel da lista
                        path.pop(i)
                        # adicionamos o ultimo passo na lista para verificacao
                        # li = valid_path
                        # valid_path = [parent] + li
                        break
        else:
            for vp in valid_path:
                for j in range(0, len(path)):
                    if vp == path[j][0]:
                        path.pop(j)
                        break
            valid_path = []

    return [path[x][2] for x in range(0, len(path))]


idx = 2
path = solve(_maps[idx], miner[idx], _exit[idx])

for p in path:
    print(p)

if __name__ == '__main__':
    pass
