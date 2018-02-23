'''
http://www.codewars.com/kata/angle-between-two-planes/train/python

https://math.tutorvista.com/geometry/angle-between-two-planes.html
http://www.mat.ufmg.br/gaal/aulas_online/at4_11.html
'''


def angle_planes(planes):
    accX, accY, accZ = 1, 1, 1
    for x, y, z in planes:
        print(x, y, z)



angle_planes(([(2,1,2),(1,2,2),(2,2,0), (2,0,0),(2,0,2),(0,2,2)]))

if __name__ == '__main__':
    pass