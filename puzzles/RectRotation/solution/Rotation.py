'''
https://www.codewars.com/kata/simple-fun-number-27-rectangle-rotation/train/python
'''

from math import cos, sin, pi


def to_radian(angle):
    return angle * pi / 180


'''
normal 
[ [cos(theta) -sin(theta)], [sin(theta) cos(theta)]]
# anti horario
[ [cos(theta) sin(theta)], [-sin(theta) cos(theta)]]
'''


def rotation_pointd_2d(originX, originY, px, py, angle):
    theta = to_radian(angle)
    ct, st = cos(theta), sin(theta)
    '''
    [(px - originX) * ct + (py - originY) * st + originX, (-px - originX) * st + (py - originY) * ct + originY]
    '''
    return [(px - originX) * ct - (py - originY) * st + originX, (px - originX) * st + (py - originY) * ct + originY]


def rotation_2d_matrix_homogeneuous(origin_x, origin_y, px, py, angle):
    # matrix homogenea de rotacao
    # hm = [[ct,-st,-originX*ct+originY*st],[st,ct,-originX*st-originY*ct],[0,0,1]]
    # ponto em uma matriz homogenea
    # hp = [px, py, 1]
    # counter clockwise
    # [px * ct + py * st, -px * st + py * ct]
    # normal
    # [px * ct - py * st, px * st + py * ct]
    pass


def test_rotation():
    for angle in range(0, 361):
        p = rotation_pointd_2d(2.03, 1.03, 1, 1, angle)
        print("%d: %f %f" % (angle, p[0], p[1]))


test_rotation()

if __name__ == '__main__':
    pass
