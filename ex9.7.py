#O bloco finally é executado sempre que um bloco try é executado, independentemente de ocorrer ou não uma exceção. Isso significa que o bloco finally é executado mesmo que uma exceção tenha sido lançada e não tenha sido capturada por um bloco except.

try: 
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
finally:
    arquivo.close()