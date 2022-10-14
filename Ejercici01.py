import math

class Punto:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x,self.y)

        if self.x > 0 and self.y > 0:
            print("{} se encuentra en el primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} se encuentra en el segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} se encuentra en el tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} se encuentra en el cuarto cuadrante".format(self))
        else:
            print("{} se encuentra en el origen".format(self))

def vector(self,v):
    print("El vector entre los puntos {} y {} es ({},{})".format(self,v,v.x - self.x, v.y-self.y))
def distancia (self, d):
    distan = math.sqrt((d.x- self.x)**2+ (d.y-self.y)**2)
    print("La distancia entre los puntos {} y {} es({})".format(self,d,distan))


class Rectangulo:
    

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)
A.cuadrante()
B.cuadrante()
C.cuadrante()