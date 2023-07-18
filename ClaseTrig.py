### Laboratorio 1
## Repaso de Programacion Orientada a Objetos
## Autor: Jorge Villalobos


import math



class Trig:
    Pi = math.pi
    def __init__(self,operacion):
        self.operacion = operacion

    ##funcion para calcular el seno de PI
    def senx(self):
        return math.sin(self.Pi)
    
   ##funcion para calcular el coseno de PI
    def cosx(self):
        return math.cos(self.Pi)

    ##funcion para calcular la tangente de PI
    def tanx(self):
        return math.tan(self.Pi)



    
