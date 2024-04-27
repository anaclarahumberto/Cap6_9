import math

while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            raise ValueError("O número deve ser positivo.")
        else:
            raiz_quadrada = math.sqrt(numero)
            print(f"A raiz quadrada de {numero} é: {raiz_quadrada:.2f}")
            break
    except ValueError as ve:
        print("Erro:", ve)
