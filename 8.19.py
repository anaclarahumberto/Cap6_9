class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

class LivroDeBiblioteca(Livro):
    def __init__(self, titulo, autor, codigo):
        super().__init__(titulo, autor)
        self.codigo = codigo

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Código: {self.codigo}")

livro_biblioteca = LivroDeBiblioteca(titulo="Dom Quixote", autor="Miguel de Cervantes", codigo="DQ123")
livro_biblioteca.mostrar_dados()
