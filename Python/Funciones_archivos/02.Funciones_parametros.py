def saludar():
    print("¡Hola, Como estas?!")

def potencia(base, exponente=2):
    return base ** exponente

# Funciones de multiples parámetros
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

saludar()
print(potencia(3))
print(potencia(2, 4))
suma, resta = operaciones(10, 5)
print(f"Suma: {suma}, Resta: {resta}")
