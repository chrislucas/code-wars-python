'''
http://www.codewars.com/kata/compute-a-convex-hull
DONE
'''

from functools import cmp_to_key

p0 = [0] * 2


def orientation(p, q, r):
    px, py = p[0], p[1]
    qx, qy = q[0], q[1]
    rx, ry = r[0], r[1]
    return (qy - py) * (rx - qx) - (qx - px) * (ry - qy)


def square_distance(p, q):
    px, py = p[0], p[1]
    qx, qy = q[0], q[1]
    return (px - qx) * (px - qx) + (py - qy) * (py - qy)


def compare(p, q):
    o = orientation(p0, p, q)
    if o == 0:
        a = square_distance(p0, p)
        b = square_distance(p0, q)
        return -1 if b >= a else 1
    return -1 if o < 0 else 1


def swap(points, i, j):
    aux = points[i]
    points[i] = points[j]
    points[j] = aux


def next_top(stack):
    _top = stack.pop()
    _ntop = stack.pop()
    stack.append(_ntop)
    stack.append(_top)
    return _ntop


def top(stack):
    top = stack.pop()
    stack.append(top)
    return top


def hull_method(points):
    size = len(points)
    min_y, min_idx = points[0][1], 0
    for idx in range(1, size):
        p = points[idx]
        x, y = p[0], p[1]
        if y < min_y or (y == min_y and x < points[min_idx][0]):
            min_y = y
            min_idx = idx

    swap(points, 0, min_idx)
    p0[0], p0[1] = points[0][0], points[0][1]
    points[1:] = sorted(points[1:], key=cmp_to_key(compare))
    acc, idx = 1, 1
    while idx < size:
        while idx < (size - 1) and orientation(p0, points[idx], points[idx + 1]) == 0:
            idx += 1
        points[acc] = points[idx]
        acc += 1
        idx += 1

    if acc > 2:
        hull = [points[0], points[1], points[2]]
        idx = 3
        while idx < acc:
            while len(hull) > 2 and orientation(next_top(hull), top(hull), points[idx]) > -1:
                hull.pop()
            hull.append(points[idx])
            idx += 1
        return hull
    return []


def test():
    matrix_points = [
        [[0, 3], [1, 1], [2, 2], [4, 4], [0, 0], [1, 2], [3, 1], [3, 3]]
        , [[0, 5], [0, 0], [5, 3]]
        , [[0, 0], [5, 3], [0, 5]]
        , [[0, 0], [5, 3], [0, 5], [2, 3]]
        , [[0, 0], [5, 3], [0, 5], [0, 3]]
        , [[0, 0], [5, 3], [0, 5], [5, 3]]
        , [[0, 0], [5, 3], [0, 5], [0, 3], [2, 3], [5, 3]]
    ]

    _list = sorted(hull_method(matrix_points[6]))
    if len(_list) > 1:
        for p in _list:
            print("P(%d, %d)" % (p[0], p[1]))


test()

if __name__ == '__main__':
    pass
