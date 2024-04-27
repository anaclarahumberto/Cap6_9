import MeuModulo

try:
    resultado = MeuModulo.dividir(14, "A")
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    print("Erro:", e)


