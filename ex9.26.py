import MeuModulo

try:
    # Chamando a função dividir do módulo
    resultado = MeuModulo.dividir(10, "A")
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    print("Erro:", e)


