y = 50

def modificar_variable_global():
    global y
    y = 100

print("Valor antes de modificar:", y)
modificar_variable_global()
print("Valor después de modificar:", y)

