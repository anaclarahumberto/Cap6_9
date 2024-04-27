try:
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except IOError as e:
    print(f"Ocorreu um erro de I/O: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
