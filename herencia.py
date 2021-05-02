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

persona1 = Persona("Alexis","Flores",21,"Masculino")

persona1.datosPersonales()

class Empleado(Persona): #lo mismo que extends
    def datosEmpleado(self,vacaciones,salario):
        print("Sus dias de vacaciones son: ", vacaciones)
        print("Su salario es: ", salario)

persona2 = Empleado("Maria","Luna",22,"Femenino")
persona2.datosPersonales()
persona2.datosEmpleado(20, 5000)
