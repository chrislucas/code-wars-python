'''
http://www.codewars.com/kata/projectile-motion/train/python
'''

from math import sin, cos, pi, sqrt


def toRadians(angle):
    return angle * pi / 180.0


def isWholeNumber(number):
    return round(number * 10) % 10 == 0


def formatting(number):
    return "%.1f" % number if isWholeNumber(number) else "%.3f" % number


class Projectile:

    def __init__(self, start_height, start_vel, angle):
        self.start_height = start_height
        self.start_vel = start_vel
        self.angle = angle

    def get_height(self, t):
        a = -16 * t ** 2
        b = (2 * cos(toRadians(self.angle)) * t)
        return a + b + self.start_height

    # vertical
    def height_eq(self):
        return "h(t) = -16.0t^2 + %st + %s" \
               % (formatting(2 * sin(toRadians(self.angle))), formatting(self.start_height))

    # horizontal
    def horiz_eq(self):
        return "x(t) = %st" \
               % (formatting(2 * cos(toRadians(self.angle))))

    def height(self, t):
        return "%s" % formatting(self.get_height(t))

    def horiz(self, t):
        return "%s" \
               % (formatting(2 * cos(toRadians(self.angle)) * t))

    def landing(self):
        comp_x = self.start_vel * cos(toRadians(self.angle))
        comp_y = self.start_vel * sin(toRadians(self.angle))
        g = -9.80
        t1 = (-comp_y + comp_y) / g
        t2 = (-comp_y - comp_y) / g
        t = t1 if t1 > 0 else t2
        x = comp_x * t
        return [x, 0, t]


#p = Projectile(5, 2, 45)
p = Projectile(5, 50, 40)
print(p.height_eq())
print(p.horiz_eq())
print(p.height(0.2))
print(p.horiz(0.2))
print(p.landing())

if __name__ == '__main__':
    pass
