class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Cliente(Pessoa):
    def __init__(self,nome,idade,endereco):
        super().__init__(nome,idade)
        self.endereco = endereco

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Endereço: {self.endereco}")

pessoa1 = Cliente("Rafael", 19, "Uberlandia")
pessoa1.mostrar_dados()