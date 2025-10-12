#BUCLE WHILE
#CALCULADORA CON PYTHON

bandera = True
while(bandera):
    print("================ CALCULADORA CON PYTHON ==================")
    numero1 = int(input("Numero 1:  "))
    numero2 = int(input("Numero 2:  "))
    print("========== OPCIONES ============")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = int(input("Ingrese la opcion que desea: "))
    if(opcion ==1):
        print("======== SUMA ========")
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado}")
    elif(opcion == 2):
        print("======= RESTA =======")
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado}")
    elif(opcion == 3):
        print("======= MULTIPLICACION =======")
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif(opcion == 4):
        print("======= DIVISION =======")
        if(numero2 != 0):
            resultado = numero1 / numero2
            print(f"El resultado de la division es: {resultado}")
        else:
            print("No se puede dividir entre 0")
    else:
        print("Opcion no valida")
       
      
    bandera = input("¿desea continuar...?(si,no) : ")
    if(bandera == "si"):
        bandera = True
    else:
        bandera = False
        print("Gracias por usar la calculadora")
