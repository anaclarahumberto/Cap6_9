class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def obter_area(self):
        area = self.largura * self.altura
        return area

retangulo = Retangulo(5, 10)

area_do_retangulo = retangulo.obter_area()
print(f"A área do retângulo é: {area_do_retangulo}.")
