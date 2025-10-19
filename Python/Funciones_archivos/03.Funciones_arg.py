# Funciones arg
def sumar_todos(*args):
    print(args)
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado

suma1 = sumar_todos(1, 2, 3, 4, 5)
print(suma1)    
suma2 = sumar_todos(10, 20, 30)
print(suma2)

def caluladora(**kwargs):
    print(kwargs)
    if kwargs['operacion'] == 'suma':
        return kwargs['a'] + kwargs['b']
    elif kwargs['operacion'] == 'resta':
        return kwargs['a'] - kwargs['b']
    else:
        return "Operación no soportada"
    
resultado1 = caluladora(operacion='suma', a=10, b=5)
print(resultado1)   

resultado2 = caluladora(operacion='resta', a=20, b=8)
print(resultado2)   
