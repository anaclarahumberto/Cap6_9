nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")
with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
