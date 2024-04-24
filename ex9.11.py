#Criar exceções personalizadas em Python pode ajudar a lidar com erros específicos no programa e exibir mensagens de erro mais informativas para o usuário. 

class ValorInvalido(Exception):
    def __init__(self, parametro, valor):
        self.parametro = parametro
        self.valor = valor
        self.mensagem = f"O valor '{valor}' é inválido para o parâmetro '{parametro}'"
        super().__init__(self.mensagem)