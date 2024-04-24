nome_arquivo = input("Digite o nome do arquivo: ")
if os.path.exists(nome_arquivo):
    nome, extensao = os.path.splitext(nome_arquivo)
    novo_nome = f"{nome}_renomeado{extensao}"
    
os.rename(nome_arquivo, novo_nome)
        print(f"Arquivo renomeado com sucesso para '{novo_nome}'.")
