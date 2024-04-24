import random

def gerar_numero_aleatorio():
    return random.randint(1, 10)

numero_aleatorio = gerar_numero_aleatorio()
print("Número aleatório entre 1 e 10:", numero_aleatorio)
