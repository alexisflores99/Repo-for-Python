class Coche:
    def __init__(self,marca,kilometros,año):
        self.marca = marca
        self.kilometros = kilometros
        self.año = año
        print("Se ha creado un auto",self.marca)

    def __del__(self):
        print("Se ha vendido el auto",self.marca)

    def __str__(self):
        return "El auto es un {}, tiene {} kilometros, y es del año {}".format(self.marca,self.kilometros,self.año)

miCoche = Coche("Audi",2000,1993)
print(str(miCoche))
    