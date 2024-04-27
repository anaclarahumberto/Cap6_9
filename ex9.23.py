try:
    with open("arquivo.txt", "r") as arquivo:
        numeros = [int(x) for x in arquivo.read().split()]
        soma = sum(numeros)
        print("Soma dos números:", soma)
except FileNotFoundError:
    print("Arquivo não encontrado")
except ValueError:
    print("Conteúdo inválido no arquivo")
