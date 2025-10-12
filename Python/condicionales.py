#CALCULADORA

#ENTRADA
numero1 = int(input("Ingrese el 1er nro:  "))
numero2 = int(input("Ingrese el 2do nro:  "))
operacion = input("Ingrese la operacion (+, -, *, /):  ")
#PROCESO
if(operacion == "+"):
    resultado = numero1 + numero2
elif(operacion == "-"):
    resultado = numero1 - numero2
elif(operacion =="*"):
    resultado = numero1*numero2
elif(operacion =="/"):
    resultado = numero1/numero2
else:
    print("Operacion no valida")
    exit()
#SALIDA
print(f"El resultado de {numero1} {operacion} {numero2} es:  {resultado} ")
