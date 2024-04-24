#é possível utilizar o bloco finally em conjunto com o bloco try/except para garantir a
#execução de um determinado trecho de código, independentemente de ocorrer uma exceção ou não.
try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
finally:
    arquivo.close()

#O bloco finally garante que o arquivo seja fechado após a sua utilização, independentemente de ocorrer ou não uma exceção.