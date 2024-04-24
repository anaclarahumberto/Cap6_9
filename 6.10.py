def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
resultado = fibonacci(n)
print("O", n, "º termo da sequência de Fibonacci é", resultado)
