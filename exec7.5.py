import os

nome_arquivo = input("Digite o nome do arquivo que deseja excluir: ")

if os.path.exists(nome_arquivo):
    os.remove(nome_arquivo)
    print(f"O arquivo '{nome_arquivo}' foi excluído com sucesso.")
