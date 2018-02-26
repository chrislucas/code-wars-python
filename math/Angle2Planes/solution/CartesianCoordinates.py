'''
http://www.codewars.com/kata/cartesian-coordinates-from-degree-angle/train/python
https://www.engineeringtoolbox.com/converting-cartesian-polar-coordinates-d_1347.html
http://wwwp.fc.unesp.br/~mauri/Down/Polares.pdf
'''

from math import cos, sin, pi


def coordinates(degrees, radius):
    return round(radius * cos(degrees * pi / 180), 10), round(radius * sin(degrees * pi / 180), 10)


print(coordinates(90, 1))
print(coordinates(45, 1))

if __name__ == '__main__':
    pass
