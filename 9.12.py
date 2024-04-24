class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        super().__init__(f"Saldo insuficiente para sacar {valor_saque}. Saldo atual: {saldo_atual}")

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque de", valor, "realizado com sucesso.")
        else:
            raise SaldoInsuficienteError(self.saldo, valor)


minha_conta = ContaBancaria(saldo=100)

try:
    minha_conta.sacar(150)
except SaldoInsuficienteError as e:
    print(e)
