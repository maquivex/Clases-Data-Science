#BUCLE FOR

for contador in range(10):
    print(contador)

#Tabla de multiplicar
tabla = int(input("Ingrese la tabla de multiplicar que desea:  "))
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")
    