class Triangulo:
    def __init__(self, lado1, lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        print(f"O perimetro é {self.perimetro}")

class Triangulo_Retangulo(Triangulo):
    def __init__(self, cateto_adjacente, cateto_oposto, hipotenusa):
        super().__init__(cateto_adjacente, cateto_oposto, hipotenusa)

    def area(self):
        self.area = self.lado1*self.lado2/2
        print(f"A area é {self.area}")

Triangulo1 = Triangulo_Retangulo(3,4,5)
Triangulo1.area()
