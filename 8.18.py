class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} emite um som genérico.")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} faz 'au au'.")

cachorro = Cachorro(nome="Rex")

cachorro.emitir_som()
