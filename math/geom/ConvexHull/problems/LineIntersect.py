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


'''
0 colinear
> 0 clockwise 
< 0 counterclockwise 
'''


def orientation(p, q, r):
    return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)


def is_intersect(line_a, line_b):
    a = orientation(line_a.p, line_a.q, line_b.p)
    b = orientation(line_a.p, line_a.q, line_b.q)
    c = orientation(line_b.p, line_b.q, line_a.p)
    d = orientation(line_b.p, line_b.q, line_a.q)

    '''
    caso geral onde a orientacao de todos os pontos sao diferentes
    '''
    if a != b and c != d:
        return True

    '''
    caso especial onde todos os pontos sao colineares
    '''

    return False


line1 = Line2D(Point2D(1, 1), Point2D(13, 14))
line2 = Line2D.constructor(2, 3, 10, 15)

print(line1)
print(line2)

# colinear
print(orientation(Point2D(0, 0), Point2D(4, 4), Point2D(1, 1)))
# counterclockwise
print(orientation(Point2D(0, 0), Point2D(4, 4), Point2D(1, 5)))

if __name__ == '__main__':
    pass
