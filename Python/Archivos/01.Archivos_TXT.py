# MANEJO DE ARCHIVOS EN PYTHON
# ESCRIBIR UN ARCHIVO DE TEXTO

with open("notas.txt", "w") as archivo:
    archivo.write("Hola Mundo\n")
    archivo.write("Esta es una clase de Python\n")

with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)    

with open("notas.txt", "a") as archivo:
    archivo.write("Agregando una nueva línea al archivo.\n")

