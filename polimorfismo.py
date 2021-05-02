# class Persona:
#     def __init__(self):
#         self.cedula = 12345

#     def mensaje(self):
#         print("Este mensaje viene de la clase Persona")

    
# class Obrero(Persona):
#     def __init__(self):
#         self.especialista = 1
    
#     def mensaje(self):
#         print("Este mensaje viene de la clase Obrero")

# obrero1 = Obrero()
# obrero1.mensaje()

class Gato:
    def hablar(self):
        print("Miuau")

class Perro(Gato):
    def hablar(Self):
        print("Guau")

def escucharMascota(animal):
    animal.hablar()

mascota1 = Perro()
escucharMascota(mascota1) 
