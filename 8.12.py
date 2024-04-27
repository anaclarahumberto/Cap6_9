class Veiculo:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor

    def exibir_velocidade(self):
        print(f"Velocidade do veículo: {self.velocidade} km/h")

class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca

carro = Carro(marca="Toyota")

print(f"Marca do carro: {carro.marca}")
carro.acelerar(50)
carro.exibir_velocidade()
carro.frear(20)
carro.exibir_velocidade()
