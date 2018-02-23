'''
http://mundoeducacao.bol.uol.com.br/matematica/angulo-entre-dois-vetores.htm

https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
'''

from math import sqrt, cos

class Vect2D:
    def __init__(self, px, py):
        self.px = px
        self.py = py

    def norm(self):
        return sqrt(self.px*self.px+self.py*self.px)


    def dotProduct(self, vect):
        return self.px * vect.px + self.py * vect.py


    def angle(self, vect):
        normA = self.norm()
        normB = vect.norm()
        dotP = self.dotProduct(vect)
        return normA * normB / dotP


a = Vect2D(1, 2)
b = Vect2D(15,13)
print(a.norm())
print(a.dotProduct(b))
print(a.angle(b))


if __name__ == '__main__':
    pass