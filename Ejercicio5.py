import math
class figura:
    def calcular_el_area(self):
        pass

class circulo(figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular__area(self):
        return math.pi * (self.radio ** 2)

class rectangulo(figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

c = circulo(5)
r = rectangulo(4, 6)
print(c.calcular__area())  
print(r.calcular_el_area())  