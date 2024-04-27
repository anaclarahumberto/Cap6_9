class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")

class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros):
        super().__init__()
        self.taxa_juros = taxa_juros

    def rendimento(self):
        rendimento_mensal = self.saldo * (self.taxa_juros / 100)
        print(f"Rendimento mensal com taxa de juros de {self.taxa_juros}%: R$ {rendimento_mensal:.2f}")

conta_poupanca = ContaPoupanca(taxa_juros=0.5)
conta_poupanca.depositar(1000)
conta_poupanca.rendimento()
