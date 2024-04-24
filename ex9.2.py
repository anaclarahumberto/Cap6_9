# O tratamento adequado de exceções pode melhorar a qualidade do código e torná-lo mais robusto, aumentando a confiabilidade do programaem geral.


numero = 10
divisor = 0

try:
    resultado = numero / divisor
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
