def composicao(f, g):
    def funcao_composta(x):
        return f(g(x))
    return funcao_composta

def dobro(x):
    return 2 * x

def quadrado(x):
    return x ** 2

funcao_resultante = composicao(dobro, quadrado)

resultado = funcao_resultante(3)
print(f"O resultado da função composta em x = 3 é {resultado}")
