nome_arquivo = input("Digite o nome do arquivo: ")
with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines() 
    num_linhas = len(linhas)
    print(f"O arquivo '{nome_arquivo}' possui {num_linhas} linhas.")
