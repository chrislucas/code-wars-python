'''
http://www.codewars.com/kata/angle-between-two-planes/train/python

https://math.tutorvista.com/geometry/angle-between-two-planes.html
http://www.mat.ufmg.br/gaal/aulas_online/at4_11.html

Equacao de plano com 3 pontos
https://study.com/academy/lesson/finding-the-equation-of-a-plane-from-three-points.html
ax + by + cz = d

'''

from math import acos, pi, sqrt


def getVector(plane):
    p1, p2, p3 = plane[0], plane[1], plane[2]
    # x2 - x1, y2 - y1, z2 - z1
    ab = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
    # x3 - x1, y3 - y1, z3 - z1
    ac = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
    # cross product
    abc = [ab[1]*ac[2]-ab[2]*ac[1], ab[2]*ac[0]-ab[0]*ac[2], ab[0]*ac[1]-ab[1]*ac[0]]
    return abc


def norm(vect):
    return sqrt(vect[0] * vect[0] + vect[1] * vect[1] + vect[2] * vect[2])

def dotProduct(vectA, vectB):
    return vectA[0] * vectB[0] + vectA[1] * vectB[1] + vectA[2] * vectB[2]


def angle_planes(planes):
    vectA = getVector(planes[0:3])
    vectB = getVector(planes[3:6])
    # norma
    nA = norm(vectA)
    nB = norm(vectB)
    # produto interno
    dot_p = dotProduct(vectA, vectB)
    return round(acos((dot_p / (nA * nB))), 2)


p = angle_planes(([(2, 1, 2), (1, 2, 2), (2, 2, 0), (2, 0, 0), (2, 0, 2), (0, 2, 2)]))
print(p) #"{0:.2f}".format(p)
p = angle_planes(([(-17, -31, -36), (-48, 43, 0), (49, 13, 10), (45, 38, 1), (21, -36, 18), (35, 10, 11)]))
print(p) #"{0:.2f}".format(p)


if __name__ == '__main__':
    pass
