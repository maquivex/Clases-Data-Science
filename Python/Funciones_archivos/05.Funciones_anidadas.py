#FUNCIONES ANIDADAS
# Una función anidada es una función definida dentro de otra función.

def operacion(a, b):
    def suma(x, y):
        return x + y
    
    def resta(x, y):
        return x - y
    
    def multiplicacion(x, y):
        return x * y
    
    def division(x, y):
        return x / y
    print("Suma:", suma(a, b))
    print("Resta:", resta(a, b))
    print("Multiplicación:", multiplicacion(a, b))
    print("División:", division(a, b))

operacion(7, 9)

# Funciones Recursivas
# Una función recursiva es una función que se llama a sí misma para resolver un problema.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))

# Funciones como paramentros de otras funciones

def aplicar_funcion(func, valor):
    return func(valor)

doblar = lambda x: x * 2
resultado = aplicar_funcion(doblar, 5)
print("Resultado de aplicar la función:", resultado)

