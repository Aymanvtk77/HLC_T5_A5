class persona:
    def __init__(self ,nombre ,edad ,profesiones):
        self.nombre = nombre
        self.edad = edad
        self.profesiones = profesiones

    def presentarse(self):
        return f"Hola mi nombre es {self.nombre} tengo {self.edad} y trabajo de {self.profesiones}"

p = persona("Ana", 18, "Ingenieria")
print(p.presentarse())

