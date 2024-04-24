#Para criar uma exceção personalizada, basta criar uma nova classe que herde da classe base Exception ou de uma de suas subclasses
class ValorInvalido(Exception):
    def __init__(self, parametro, valor):
        self.parametro = parametro
        self.valor = valor
        self.mensagem = f"O valor '{valor}' é inválido para o parâmetro '{parametro}'"
        super().__init__(self.mensagem)
