def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

resultado_suma, resultado_resta, resultado_multiplicacion = operaciones(10, 5)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
