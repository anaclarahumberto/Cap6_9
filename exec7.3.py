nome_arquivo_origem = input("Digite o nome do arquivo de origem: ")
nome_arquivo_destino = input("Digite o nome do arquivo de destino: ")

with open(nome_arquivo_origem, 'r') as arquivo_origem:
    linhas_origem = arquivo_origem.readlines()
    linhas_invertidas = [linha.rstrip('\n')[::-1] + '\n' for linha in linhas_origem]
    
with open(nome_arquivo_destino, 'w') as arquivo_destino:
    arquivo_destino.writelines(linhas_invertidas)
    
print(f"O conteúdo do arquivo '{nome_arquivo_origem}' foi invertido e salvo em '{nome_arquivo_destino}'.")
