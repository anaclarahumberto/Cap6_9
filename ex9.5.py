try: 
    resultado = 10/0
except Exception:
    print("Ocorreu uma exceção!")


# se um bloco except Exception for o primeiro tratador
#de um bloco try, qualquer exceção que ocorra neste bloco try será sempre tratada por ele