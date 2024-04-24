#As exceções em Python são erros que ocorrem durante a execução de um programa. Esses erros interrompem o fluxo normal de execução e podem ser causados #por diferentes fatores, como entradas inválidas do usuário, falhas na conexão de rede, erros de digitação, entre outros.

try:
   x = 1 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")