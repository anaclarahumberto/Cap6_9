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

livro_biblioteca = LivroDeBiblioteca(titulo="O verão que mundo a minha vida", autor="Jenny Han", codigo="JP189")
livro_biblioteca.mostrar_dados()
