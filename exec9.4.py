#O bloco try/except é composto por duas partes principais: o bloco try, que contém o código a ser executado, e o bloco except, que contém o tratamento de possíveis exceções.


numero_str = "abc"

try:
    numero_int = int(numero_str)
    print("Número inteiro:", numero_int)
except ValueError:
    print("Erro: A string não pode ser convertida em um número inteiro.")
