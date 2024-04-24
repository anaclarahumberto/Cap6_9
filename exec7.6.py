import os

nome_arquivo_original = input("Digite o nome do arquivo: ")
nome, extensao = os.path.splitext(nome_arquivo_original)
nome_arquivo_copia = f"{nome}.copy{extensao}"  # Adicionando a extensão ao nome da cópia

with open(nome_arquivo_original, 'r') as arquivo_origem:
    conteudo = arquivo_origem.read()

with open(nome_arquivo_copia, 'w') as arquivo_copia:
    arquivo_copia.write(conteudo)

with open(nome_arquivo_copia, 'r') as arquivo_copia:
    print("Conteúdo do arquivo copiado:")
    print(arquivo_copia.read())
    print(f"Arquivo copiado para '{nome_arquivo_copia}'.")
