class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_dados(self):
        print(f"{self.numerador}/{self.denominador}")

    def multiplicar(self, outra_fracao):
        novo_numerador = self.numerador * outra_fracao.numerador
        novo_denominador = self.denominador * outra_fracao.denominador
        return Fracao(novo_numerador, novo_denominador)

fracao1 = Fracao(numerador=3, denominador=4)
fracao2 = Fracao(numerador=5, denominador=6)

fracao1.mostrar_dados()
fracao2.mostrar_dados()

resultado = fracao1.multiplicar(fracao2)
resultado.mostrar_dados()
