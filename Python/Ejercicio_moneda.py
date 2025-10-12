#EJERCICIO DE MONEDAS

#DATOS DE ENTRADA (INPUT)
tipo_cambio = 3
moneda_origen = "SOLES"
moneda_destino = "DOLARES"
print("1. Convertir de SOLES a DOLARES")
print("2. Convertir de DOLARES a SOLES")
opcion = int(input("Ingrese una opcion (1-2): "))
if(opcion == 1):
    moneda_origen = "SOLES"
    moneda_destino = "DOLARES"
    monto_origen = float(input("Ingrese el monto a convertir: "))
    #PROCESO
    monto_destino = monto_origen / tipo_cambio
elif(opcion == 2):
    moneda_origen = "DOLARES"
    moneda_destino = "SOLES"
    monto_origen = float(input("Ingrese el monto a convertir:  "))
    #PROCESO
    monto_destino = monto_origen * tipo_cambio
else:
    print("Opcion no valida")
    exit()
print(f"RESULTADO : {monto_origen} {moneda_origen} son {monto_destino} {moneda_destino}")

