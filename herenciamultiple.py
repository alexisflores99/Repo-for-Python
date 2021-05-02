class Clase1:
    def saluda(self):
        print("Hola soy el metodo de la clase 1")

class Clase2:
    def metodo2(self):
        print("Soy el metodo de la clase 2")

class Clase3(Clase1,Clase2):
    def metodo3(self):
        print("Hola soy el metodo de la clase 3")

hola = Clase3()
hola.saluda()
hola.metodo2()
hola.metodo3()