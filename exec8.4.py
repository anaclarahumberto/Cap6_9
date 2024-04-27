class Carro:
    def __init__(self, velocidade):
       self.velocidade = velocidade
       

    def acelerar(self, segundos):
       aceleracao = 10
       self.velocidade += aceleracao * segundos
       return self.velocidade

    def frear(self, segundos):
        desaceleracao = 6  # m/s^2
        self.velocidade -= desaceleracao * segundos
        if self.velocidade < 0:
            self.velocidade = 0
            return self.velocidade
        
carro1 = Carro(30)

print("Velocidade inicial:", carro1.velocidade)
carro1.acelerar(6)  # Acelerando por 6 segundos
print("Velocidade após acelerar:", carro1.velocidade)
carro1.frear(4)     # Freando por 4 segundos
print("Velocidade após frear:", carro1.velocidade)
