def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

resultado = factorial(7)
print("Factorial de 7 es:", resultado)
