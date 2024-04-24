class Carro:
    def __init__(self, velocidade):
       self.velocidade = velocidade
       

    def acelerar(self, segundos):
       aceleracao = 10
       self.velocidade += aceleracao * segundos
       return self.velocidade

    def frear(self, segundos):
        desaceleracao = 5  # m/s^2
        self.velocidade -= desaceleracao * segundos
        if self.velocidade < 0:
            self.velocidade = 0
            return self.velocidade
        
carro1 = Carro(20)

print("Velocidade inicial:", carro1.velocidade)
carro1.acelerar(5)  # Acelerando por 5 segundos
print("Velocidade após acelerar:", carro1.velocidade)
carro1.frear(3)     # Freando por 3 segundos
print("Velocidade após frear:", carro1.velocidade)