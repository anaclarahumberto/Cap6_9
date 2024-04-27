class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


pessoa1 = Pessoa("Elouise", 24)
pessoa2 = Pessoa("Anthony", 35)


pessoa1.mostrar_dados()
print()
pessoa2.mostrar_dados()
