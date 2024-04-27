nome_arquivo = input("Digite o nome do arquivo de texto: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
