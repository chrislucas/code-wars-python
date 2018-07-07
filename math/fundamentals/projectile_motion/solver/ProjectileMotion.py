'''
http://www.codewars.com/kata/projectile-motion/train/python
'''

from math import sin, cos, pi, sqrt, ceil


def toRadians(angle):
    return angle * pi / 180


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
        b = (self.start_vel * sin(toRadians(self.angle)) * t + self.start_height)
        return a + b

    # vertical
    def height_eq(self):
        return "h(t) = -16.0t^2 + %st%s" \
               % (formatting(self.start_vel * sin(toRadians(self.angle)))
                  , "" if self.start_height == 0 else " + " + formatting(self.start_height))

    # horizontal
    def horiz_eq(self):
        return "x(t) = %st" \
               % (formatting(self.start_vel * cos(toRadians(self.angle))))

    def height(self, t):
        f = float(formatting(self.get_height(t)))
        return int(f) if isWholeNumber(f) else f

    def horiz(self, t):
        f = float((formatting(self.start_vel * cos(toRadians(self.angle)) * t)))
        return int(f) if isWholeNumber(f) else f

    def timeOfFlight(self):
        # m/s
        return (2 * self.start_vel * sin(toRadians(self.angle))) / 9.8

    def maxHeight(self):
        return ((self.start_vel ** 2) * sin(toRadians(self.angle)) ** 2) / (2 * 9.8)

    def horizontalRange(self):
        return ((self.start_vel ** 2) * (sin(toRadians(self.angle) * 2))) / 9.8

    # http://www.softschools.com/formulas/physics/projectile_motion_formulas/58/
    def landing(self):
        vx0 = self.start_vel * cos(toRadians(self.angle))  # round(self.start_vel * cos(toRadians(self.angle)), 3)
        vy0 = self.start_vel * sin(toRadians(self.angle))  # round(self.start_vel * sin(toRadians(self.angle)), 3)
        # -0.5 * 9.80 * 2
        # gravidade
        g = 9.8
        # m/s to feet/s 1m/s = 3.2808399 ft/s #3.280839895
        #ga = -g
        ga = -g * 3.28 #round(-g * 3.2808399, 3)
        '''
        # x = y0 + v0 * t + 0.5 * a * (t ^ 2)
        y0 = altura
        vy0t = v0 * sin(theta)
        Equacao quadradica
         v0 + 0.5 * a * (t ^ 2) + x0 = 0
        -v0 sin(theta) + sqrt( v0^2 * sin^2(theta) - 4 * 0.5 * (-g) * h)
        '''
        # y0 = sin(toRadians(self.angle)) #round(sin(toRadians(self.angle)), 3)
        # (self.start_vel*self.start_vel) *
        '''
        2 solucoes
        sqrt((self.start_vel*self.start_vel) * (y0*y0) - 4 * 0.5 * a * self.start_height)
        sqrt((vy0*vy0) - 4 * 0.5 * a * self.start_height) 
        '''
        b = vy0
        a = 0.5 * ga
        c = self.start_height
        delta = sqrt(b * b - 4 * a * c)
        t1 = (-vy0 + delta) / ga
        t2 = (-vy0 - delta) / ga
        t = t1 if t1 > 0 else t2
        x = vx0 * t  # round(vx0 * t, 3)
        return [float(formatting(x)), 0, float(formatting(t))]


def test_1():
    p = Projectile(5, 2, 45)
    print(p.height_eq())
    print(p.horiz_eq())
    print(p.height(0.2))
    print(p.horiz(0.2))
    print(p.landing())


def test_2():
    p = Projectile(0, 5, 45)
    print(p.height_eq())
    print(p.horiz_eq())
    print(p.height(0.2))
    print(p.horiz(0.2))
    print(p.landing())


def test_3():
    p = Projectile(15, 12, 80)
    print(p.height_eq())
    print(p.horiz_eq())
    print(p.height(0))
    print(p.horiz(0))
    print(p.height(1))
    print(p.horiz(1))
    print(p.landing())


def test_4():
    p = Projectile(125, 65, 37)
    print(p.landing())
    print(p.timeOfFlight())
    print(p.maxHeight())


def test_5():
    p = Projectile(0, 20, 60)
    print(p.landing())


test_1()
test_2()
test_3()
# test_5()

if __name__ == '__main__':
    pass
