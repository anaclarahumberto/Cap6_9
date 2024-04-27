while True:
    try:
        nome_arquivo = input("Digite o nome do arquivo: ")
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        break
    except FileNotFoundError:
        print("Arquivo não encontrado")
