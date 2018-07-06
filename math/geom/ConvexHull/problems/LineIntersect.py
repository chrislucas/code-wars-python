'''
https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
'''


class Point2D:
    def __init__(self, x, t):
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


line1 = Line2D(Point2D(1, 1), Point2D)