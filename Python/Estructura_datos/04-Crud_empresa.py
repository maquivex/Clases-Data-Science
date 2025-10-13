import os
from time import sleep

# EJERCICIO FINAL MODULO 1 - CRUD EMPRESAS
# NOMBRE: SAMUEL QUISPE

dic_empresas = {
    '20454545':{
        'razon_social': 'EMPRESA SAC',
        'direccion':'CALLE EL SOL 123'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC: ")
        razon_social = input("Ingrese Razon Social: ")
        direccion = input("Ingrese Direccion: ")
        dic_nueva_empresa = {
            'razon_social': razon_social,
            'direccion': direccion
        }
        dic_empresas[ruc] = dic_nueva_empresa
        print("Empresa registrada exitosamente.")
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Razon Social : {info['razon_social']}")
            print(f"Direccion : {info['direccion']}")
            print("*"*ANCHO)
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la empresa a actualizar: ")
        if ruc in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc]['razon_social']}")
            nueva_razon_social = input("Ingrese nueva razon social (dejar en blanco para no cambiar): ")
            nueva_direccion = input("Ingrese nueva direccion (dejar en blanco para no cambiar): ")
            if nueva_razon_social:
                dic_empresas[ruc]['razon_social'] = nueva_razon_social
            if nueva_direccion:
                dic_empresas[ruc]['direccion'] = nueva_direccion
                
            print("Empresa actualizada exitosamente.")

        else:
            print("Empresa no encontrada.")
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la empresa a eliminar: ")
        if ruc in dic_empresas:
            print("Desea realmente eliminar esta empresa?")
            aux = int(input("1. Si / 2. No          : "))
            if (aux == 1):
                del dic_empresas[ruc]
                print("Empresa eliminada exitosamente.")
            elif (aux ==2):
                print("Empresa no eliminada")
        else:
            print("Empresa no encontrada.")
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")