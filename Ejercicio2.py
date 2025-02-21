class Estudiante:
    def __init__(self, nombre, edad, estudios):
        self.nombre = nombre
        self.edad = edad
        self.estudios = estudios

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.estudios}."
    
class Persona(Estudiante):
    def __init__(self, nombre ,edad ,materia ,asignatura):
       super(). __init__(nombre ,edad ,materia)
       self.asignatura = asignatura

    def presentarse(self):
           return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.asignatura}"

e = Persona("Carlos", 22, "Estudiante", "Matematicas")
print(e.presentarse())


