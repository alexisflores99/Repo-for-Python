class Coche:
    def __init__(self):
        self.marca = "Audi"
        self.color = "Rojo"
        self.__ruedas = 4
        self.enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        if (self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"

    def __str__(self):
        return "Este auto es marca {}, de color {}, tiene {} ruedas".format(self.marca,self.color, self.__ruedas)

miCoche = Coche()
print(miCoche.arrancar(False))
print(miCoche)

print("*****************Otro Vehiculo***************")

miCoche2 = Coche()
miCoche2.ruedas=20
print(miCoche2.arrancar(True))
print(miCoche2)
