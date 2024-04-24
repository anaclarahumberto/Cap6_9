class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito de", valor, "realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print("Saque de", valor, "realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def exibir_saldo(self):
        print("Saldo atual:", self.saldo)


minha_conta = ContaBancaria()


minha_conta.depositar(100)
minha_conta.exibir_saldo()

minha_conta.sacar(50)
minha_conta.exibir_saldo()

minha_conta.sacar(70) 
minha_conta.exibir_saldo()
