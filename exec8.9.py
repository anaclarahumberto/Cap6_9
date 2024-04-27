class Retangulo:
    def __init__ (self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        area = self.altura * self.largura
        return area
    
    @property
    def largura(self):
        return self._largura
        
    @largura.setter
    def largura(self, valor):
        if (valor > 0):
            self._largura = valor
        else:
            raise LadoInvalidoError()
        
    @property
    def altura(self):
        return self._altura
        
    @altura.setter
    def altura(self, valor):
        if (valor > 0):
            self._altura = valor
        else:
            raise LadoInvalidoError()
              
                                    
class LadoInvalidoError(Exception):
    def __init__(self):
        super().__init__("O lado de um retângulo deve ser positivo")

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    @property
    def largura(self):
        return self._largura
    
    @property
    def altura(self):
        return self._altura
    
    @largura.setter
    def largura(self, valor):
        if (valor > 0):
            self._largura = valor
            self._altura = valor
        else:
            raise LadoInvalidoError()
        
    @altura.setter
    def altura(self, valor):
        if (valor > 0):
            self._altura = valor
            self._largura = valor
        else:
            raise LadoInvalidoError()
                            
try:
    r1 = Retangulo(10,2)
    print(r1.calcular_area())
    r2 = Retangulo(2,1)
    print(r2.calcular_area())
    q1 = Quadrado(10)
    q1.altura = 8
    print(q1.calcular_area())
except LadoInvalidoError as ex:
    print(ex)
print("Programa finalizado.")
