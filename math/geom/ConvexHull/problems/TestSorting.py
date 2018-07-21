class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __lt__(self, other):
        return compare(self, other)

    def __str__(self):
        return "%d, %d" % (self.x, self.y)


def compare(p, q):
    return p.y - q.y < 0


def test():
    points = []
    points.append(Point2D(0, 3))
    points.append(Point2D(1, 1))
    points.append(Point2D(2, 2))
    points.append(Point2D(4, 4))
    points.append(Point2D(0, 0))
    points.append(Point2D(1, 2))
    points.append(Point2D(3, 1))
    points.append(Point2D(3, 3))
    #points = sorted(points)
    points.sort()

    for p in points:
        print(p)


test()

if __name__ == '__main__':
    pass
