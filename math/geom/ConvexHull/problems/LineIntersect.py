'''
https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
https://www.geeksforgeeks.org/orientation-3-ordered-points/
'''


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line2D:
    # p e q sao pontos num espaco de 2 dimensoes
    def __init__(self, p, q):
        self.p = p
        self.q = q

    @classmethod
    def constructor(cls, px, py, qx, qy):
        return cls(Point2D(px, py), Point2D(qx, qy))

    def get_p(self):
        return self.p

    def get_q(self):
        return self.q


def on_segment(p, q, r):
    '''
    Ponto p, q, r colineares
    '''
    px, py = p.get_x(), p.get_y()
    qx, qy = q.get_x(), q.get_y()
    rx, ry = r.get_x(), r.get_y()
    return max(px, rx) >= qx >= min(px, rx) and max(py, ry) >= qy >= min(py, ry)


def orientation(p, q, r):
    '''
    0 colinear
    > 0 clockwise
    < 0 counterclockwise
    '''
    return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)


def is_intersect(line_a, line_b):
    a = orientation(line_a.p, line_a.q, line_b.p)
    b = orientation(line_a.p, line_a.q, line_b.q)
    c = orientation(line_b.p, line_b.q, line_a.p)
    d = orientation(line_b.p, line_b.q, line_a.q)
    '''
        caso geral: Onde (p1, q1, p2) e (p1. q1, q2) tem orientacoes diferentes
        e (p2, q2, p1) e (p2, q2, q1) tambem tem orientacoes diferentes
    '''
    if a != b and c != d:
        return True

    '''
        caso especial onde os pontos line_a.p, line_a.q, line_b.p
        sao colineares e o ponto line_b.p esta no segmento
        line_a.p -> line_a.q
    '''
    if a == 0 and on_segment(line_a.p, line_b.p, line_a.q):
        return True

    '''
        caso especial onde os pontos line_a.p, line_a.q, line_b.q
        sao colineares e o ponto line_b.q esta no segmento
        line_a.p -> line_a.q
    '''
    if b == 0 and on_segment(line_a.p, line_b.q, line_a.q):
        return True

    '''
        caso especial onde os pontos line_b.p, line_b.q, line_a.p
        sao colineares e o ponto line_a.p esta no segmento
        line_b.p -> line_b.q
    '''
    if c == 0 and on_segment(line_b.p, line_a.p, line_b.q):
        return True

    '''
        caso especial onde os pontos line_b.p, line_b.q, line_a.p
        sao colineares e o ponto line_a.q esta no segmento
        line_b.p -> line_b.q
    '''
    if d == 0 and on_segment(line_b.p, line_a.q, line_b.q):
        return True

    return False


def test_instance_line():
    print(Line2D(Point2D(1, 1), Point2D(13, 14)))
    print(Line2D.constructor(2, 3, 10, 15))


def test_orientation():
    # colinear
    print(orientation(Point2D(0, 0), Point2D(4, 4), Point2D(1, 1)))
    # counterclockwise
    print(orientation(Point2D(0, 0), Point2D(4, 4), Point2D(1, 5)))
    # clockwise
    print(orientation(Point2D(10, 0), Point2D(1, 1), Point2D(1, 5)))
    # counterclockwise
    print(orientation(Point2D(-3, -5), Point2D(1, 1), Point2D(1, 5)))
    # clockwise
    print(orientation(Point2D(-3, -5), Point2D(1, 1), Point2D(2, -5)))
    # clockwise
    print(orientation(Point2D(-3, -5), Point2D(-1, -1), Point2D(-2, -5)))


def test_intersection():

    la = Line2D(Point2D(-5, -5), Point2D(0, 0))
    lb = Line2D(Point2D(0, 0), Point2D(10, 10))
    # la e lb sao paralelas
    print(is_intersect(la, lb))


    la = Line2D(Point2D(1, 1), Point2D(10, 1))
    lb = Line2D(Point2D(1, 2), Point2D(10, 2))
    # la e lb sao paralelas
    print(is_intersect(la, lb))

    la = Line2D(Point2D(10, 0), Point2D(0, 10))
    lb = Line2D(Point2D(0, 0), Point2D(10, 10))
    # la e lb sao paralelas
    print(is_intersect(la, lb))

    la = Line2D(Point2D(-5, -5), Point2D(0, 0))
    lb = Line2D(Point2D(1, 1), Point2D(10, 10))
    # la e lb sao paralelas
    print(is_intersect(la, lb))


    la = Line2D(Point2D(-5, -5), Point2D(0, 0))
    lb = Line2D(Point2D(-1, -1), Point2D(10, 10))
    # la e lb sao paralelas
    print(is_intersect(la, lb))


test_orientation()

if __name__ == '__main__':
    pass
