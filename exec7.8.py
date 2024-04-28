import os
import shutil

diretorio_temp = './temp'

# Verifica se o diretório existe antes de excluí-lo
if os.path.exists(diretorio_temp):
    # Verifica se é um diretório para evitar exclusões acidentais
    if os.path.isdir(diretorio_temp):
        # Exclui o diretório e todo o seu conteúdo de forma recursiva
        shutil.rmtree(diretorio_temp)
        print(f'O diretório {diretorio_temp} e todo o seu conteúdo foram excluídos com sucesso.')
    else:
        print(f'O caminho {diretorio_temp} não é um diretório.')
else:
    print(f'O diretório {diretorio_temp} não existe.')
