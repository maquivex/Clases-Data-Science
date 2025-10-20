# Programación Orientada a Objetos (POO) en Python
# las clases son plantillas para crear objetos (instancias)
# una clase puede tener atributos (propiedades) y métodos (funciones)

class Automovil:
    # Constructor de la clase
    def __init__(self, aa, pl, col, mar):
        self.año = aa          # Atributo año
        self.placa = pl       # Atributo placa
        self.color = col        # Atributo color
        self.marca = mar        # Atributo marca

    # creamos un metodo
    def encender(self):
        print(f"Encender el automóvil {self.marca} {self.placa}")
    
    def avanzar(self):
        print(f"Avanzar el automóvil {self.marca} {self.placa} está avanzando")

    def acelerar(self):
        print(f"Acelerar el automóvil {self.marca} {self.placa} está acelerando")
    
    def frenar(self):
        print(f"Frenar el automóvil {self.marca} {self.placa} está frenando")

wm = Automovil(2020, "XYZ123", "Rojo", "Toyota")
wm.encender()

tico = Automovil(2018, "ABC789", "Azul", "Honda")
tico.encender()


