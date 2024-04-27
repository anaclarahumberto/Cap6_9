

try:
   "i"/0

except ZeroDivisionError:
    raise ValueError("Divisão por zero não é permitida.")

except Exception as e:
    print("Erro:", e)
