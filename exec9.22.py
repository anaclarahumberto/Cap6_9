def calcular_media(lista):
    if not lista:
        raise ValueError("A lista está vazia")
    return sum(lista) / len(lista)

try:
    lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]
    media = calcular_media(lista)
    print("Média:", media)
except ValueError as e:
    print("Erro:", e)
