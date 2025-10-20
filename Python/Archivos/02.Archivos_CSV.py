# Archivos CSV

import csv

with open("alumnos.csv", "w", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Dni", "Nombre", "Email"])
    escritor.writerow(["40513553","Samuel Quispe", "samu123@gmail.com"])
    
with open("alumnos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

 