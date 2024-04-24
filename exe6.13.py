lista = [1,2,3,4,5,6,7,8]

def impar(numero):
    return numero % 2 != 0

def filtrar_lista(lista, funcao):
    return [elemento for elemento in lista if funcao(elemento)]

resultado = filtrar_lista(lista, impar)
print(resultado) 
