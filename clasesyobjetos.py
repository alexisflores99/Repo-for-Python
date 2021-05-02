#Clases y Objetos
# class Gelatina: #Iniciolizamos el molde
#     def __init__(self,sabor,color,tamaño):
#         self.sabor = sabor
#         self.color = color
#         self.tamaño = tamaño

#     def imprimir(self):
#         print("La gelatina es ", self.sabor)
#         print("La gelatina se ve de color ", self.color)
#         print("La gelatina es ", self.tamaño)
    
# gela1 = Gelatina("rojo", "frutilla", "grande")
# gela2 = Gelatina("azul", "mora", "chica")

# gela1.imprimir()
# gela2.imprimir()

import pickle

class Persona: 
    def __init__(self, nombre, edad, email, telefono):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Email: ", self.email)
        print("Telefono: ", self.telefono)
        print("\n")

per1 = Persona("Alexis", 21, "alexis@alexis.com", 980622918)
per2 = Persona("Marco", 23, "marco@marco.com", 980622918)
per3 = Persona("Javier", 28, "javier@javier.com", 980622918)

lista_personas = [per1,per2,per3]

fichero = open("Personas","wb")

pickle.dump(lista_personas, fichero)
fichero.close()

del(fichero)

fichero_leer = open("Personas","rb")
personitas = pickle.load(fichero_leer)
fichero_leer.close()

for i in personitas:
    print(i.imprimir())
