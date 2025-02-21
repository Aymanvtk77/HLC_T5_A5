class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} tengo {self.edad} de edad."
    
class Trabajo(Persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad)
        self.profesion = profesion
        self.empresa = empresa
    
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} tengo {self.edad} y trabajo en {self.empresa}."
    
e = Trabajo("Elena", 35, "Arquitecta", "Contrucciones XYZ")
print(e.presentarse()) 


        

