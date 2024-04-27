try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    
    resultado = numerador / denominador

except ValueError as ve:
    raise TypeError("Os valores digitados devem ser números inteiros") from ve

except ZeroDivisionError as zde:
    raise ValueError("Divisão por zero não é permitida") from zde

except Exception as e:
    print("Erro:", e)
