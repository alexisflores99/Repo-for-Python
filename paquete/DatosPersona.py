class Persona:
    def __init__(self,nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    
    def datosPersonales(self):
        print("El nombre de la persona es:", self.nombre)
        print("El apellido de la persona es:", self.apellido)
        print("La edad de la persona es:", self.edad)
        print("El sexo de la persona es:", self.sexo)