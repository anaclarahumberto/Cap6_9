class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def mostrar_dados(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Preço: R$ {self.preco}")
        print(f"Quantidade em estoque: {self.quantidade_estoque}")

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, quantidade_estoque, imposto):
        super().__init__(nome, preco, quantidade_estoque)
        self.imposto = imposto

    def preco_final(self):
        preco_com_imposto = self.preco * (1 + self.imposto / 100)
        print(f"Preço final com imposto: R$ {preco_com_imposto}")

produto_importado = ProdutoImportado(nome="Notebook", preco=2500, quantidade_estoque=10, imposto=15)
produto_importado.mostrar_dados()
produto_importado.preco_final()
