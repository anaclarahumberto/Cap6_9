class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        pi = 3.14
        cal_area = pi* (self.raio**2)
        return cal_area
    

circulo = Circulo(5)

print (f"Área:{circulo.area()}")