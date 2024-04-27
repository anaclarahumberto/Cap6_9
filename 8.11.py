class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        self.salario += porcentagem * self.salario

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Salário: {self.salario}")

pessoa = Funcionario("Rafael", 18, 100000)
pessoa.aumentar_salario(0.1)
pessoa.mostrar_dados()


