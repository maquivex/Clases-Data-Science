class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
       print(f"Nombre: {self.nombre}, Email: {self.email}") 

class Alumno(Persona):
    pass

class Profesor(Persona):
    def __init__(self, nombre, email, asignatura):
        super().__init__(nombre, email)
        self.asignatura = asignatura

    def mostrar_profesor(self):
        print(f"Nombre: {self.nombre}, Email: {self.email}, Asignatura: {self.asignatura}") 

alumno1 = Alumno("Juan Perez", "juan.perez@example.com", "Matemáticas")
alumno1.mostrar()

profesor1 = Profesor("Ana Gómez", "ana.gomez@example.com", "Historia")
profesor1.mostrar_profesor()