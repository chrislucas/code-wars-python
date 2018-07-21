'''
https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
http://portingguide.readthedocs.io/en/latest/comparisons.html
'''

from functools import cmp_to_key


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # <
    def __lt__(self, other):
        return compare(self, other) < 0

    def __str__(self):
        return "%d, %d" % (self.x, self.y)


def orientation(p, q, r):
    """
        0 colinear
        > 0 clockwise
        < 0 counterclockwise
    """
    return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)


def square_distance(p, q):
    diff_x = q.x - p.x
    diff_y = q.y - p.y
    return (diff_x * diff_x) + (diff_y * diff_y)


'''
Ponto2D p0, p e q
p0 é um ponto fixo de referencia
'''

points = []


def compare(p, q):
    p0 = points[0]
    o = orientation(p0, p, q)
    '''
        se os pontos forem colineares verique qual dos 2 pontos
        esta mais perto de p0
    '''
    if o == 0:
        a = square_distance(p0, p)
        b = square_distance(p0, q)
        return -1 if b >= a else 1
    '''
        senao ordene pelos pontos que estao na orientacao anti-horario em torno do ponto p0
    '''
    return -1 if o < 0 else 1


def swap(_list, i, j):
    aux = _list[i]
    _list[i] = _list[j]
    _list[j] = aux


def is_empty(_stack):
    return len(_stack) == 0


def top(_stack):
    if is_empty(_stack):
        return None
    return _stack[len(_stack) - 1]


def next_top(_stack):
    _len = len(_stack)
    if _len > 1:
        _top = top(_stack)
        _stack.pop(_len - 1)
        _next_top = top(_stack)
        _stack.append(_top)
        return _next_top
    return None


def convex_hull(points):
    size, min_idx, min_y = len(points), 0, points[0].y
    for i in range(1, size):
        test = points[i].y < min_y or \
               (points[i].y == min_y and points[i].x < points[min_idx].x)
        if test:
            min_idx, min_y = i, points[i].y

    if min_idx != 0:
        swap(points, 0, min_idx)

    p0 = points[0]

    points[1:] = sorted(points[1:], key=cmp_to_key(compare))
    #points[1:] = sorted(points[1:])
    acc = 1
    i = 1
    while i < size:
        '''
            verificar se p0 e 2 pontos consecutivos sao colineares
            se forem passe para o par seguinte
        '''
        if i < (size - 1):
            o = orientation(p0, points[i], points[i + 1])
            while i < (size - 1) and o == 0:
                i += 1
                o = orientation(p0, points[i], points[i + 1])
        points[acc] = points[i]
        acc += 1
        i += 1

    if acc > 2:
        _stack = [points[0], points[1], points[2]]
        i = 3
        while i < acc:
            _next_top = next_top(_stack)
            _top = top(_stack)
            o = orientation(_next_top, _top, points[i])
            '''
            se a orientacao dos 3 pontos nao for anti horario
            remova o ultimo ponto da pilha e
            '''
            while len(_stack) > 2 and o > -1:
                _stack.pop()
                _next_top = next_top(_stack)
                _top = top(_stack)
                o = orientation(_next_top, _top, points[i])
            _stack.append(points[i])
            i += 1
        return _stack
    return []


def test_convex_hull():
    points.append(Point2D(0, 3))
    points.append(Point2D(1, 1))
    points.append(Point2D(2, 2))
    points.append(Point2D(4, 4))
    points.append(Point2D(0, 0))
    points.append(Point2D(1, 2))
    points.append(Point2D(3, 1))
    points.append(Point2D(3, 3))
    '''
    '''
    '''
        points = []
        for i in range(0, 100):
            points.append(Point2D(i // 10, i % 10))
    '''

    _stack_points = convex_hull(points)
    for p in _stack_points:
        print("P(%d,%d)", p.get_x(), p.get_y())


test_convex_hull()

if __name__ == '__main__':
    pass
