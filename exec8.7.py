from typing import List

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"O seu nome é {self.nome} e você tem {self.idade} anos.")

class Funcionario(Pessoa):
    def __init__ (self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Salário: R${self.salario}")

pessoas: List[Pessoa] = []

pessoas.append(Pessoa("Beatriz", 22))
pessoas.append(Pessoa("João", 19))
pessoas.append(Funcionario("Pedro", 20, 10200))
pessoas.append(Funcionario("Ana", 18, 7000))

for p in pessoas:
    p.mostrar_dados()
    print("---------------------------------------------------")
