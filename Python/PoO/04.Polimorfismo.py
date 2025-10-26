# Polimorfismo

class Persona: 

    def __init__(self, nom, ema):
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

class Alumno(Persona):

    def __init__(self, nom, ema, nota):
        super().__init__(nom, ema)
        self.nota = nota

    def mostrar(self):
        print("============ DATOS DEL ALUMNO ============")
        super().mostrar()
        print(f"Nota: {self.nota}")
        
class Profesor(Persona):

    def __init__(self, nom, ema, esp):
        super().__init__(nom, ema)
        self.especialidad = esp

    def mostrar(self):
        print("============ DATOS DEL PROFESOR ============")
        super().mostrar()
        print(f"Especialidad: {self.especialidad}")

alumno1 = Alumno("Juan Perez", "juan.perez@example.com", 20)
alumno1.mostrar()

profesor1 = Profesor("Ana Gómez", "ana.gomez@example.com", "Historia")
profesor1.mostrar()