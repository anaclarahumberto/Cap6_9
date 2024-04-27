import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        print(f"A área: {math.pi * self.raio ** 2}")

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura

    def volume(self):
        print(f"Volume: {math.pi * self.raio ** 2 * self.altura}")


cilindro1 =  Cilindro(5,8)

cilindro1.area()
cilindro1.volume()
