import os

diretorio_temp = './temp'
os.makedirs(diretorio_temp, exist_ok=True)

# Cria o arquivo "temp.txt" dentro do diretório "temp"
caminho_arquivo = os.path.join(diretorio_temp, 'temp.txt')
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Conteúdo do arquivo temp.txt\n')
