import shutil
import os

def criar_diretorio(diretorio):
    try:
        os.makedirs(diretorio)
        print(f"O diretório '{diretorio}' foi criado com sucesso!")
    except FileExistsError:
        print(f"O diretório '{diretorio}' já existe.")
    except PermissionError:
        print(f"Sem permissão para criar o diretório '{diretorio}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o diretório '{diretorio}': {e}")

def excluir_diretorio(diretorio):
    if os.path.exists(diretorio):
        try:
            shutil.rmtree(diretorio)
            print(f"O diretório '{diretorio}' foi excluído com sucesso!")
        except PermissionError:
            print(f"Sem permissão para excluir o diretório '{diretorio}'.")
        except Exception as e:
            print(f"Ocorreu um erro ao excluir o diretório '{diretorio}': {e}")
    else:
        print(f"O diretório '{diretorio}' não foi encontrado.")

# Exemplo de uso:
diretorio = "/caminho/para/o/diretorio"
criar_diretorio(diretorio)
excluir_diretorio(diretorio)
