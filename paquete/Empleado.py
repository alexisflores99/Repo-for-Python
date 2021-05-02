class Empleado: #lo mismo que extends

    def __init__(self,ocupacion,salario,vacaciones):
        self.__ocupacion = ocupacion
        self.__salario = salario
        self.__vacaciones = vacaciones

    def datosEmpleado(self):
        print("Su ocupacion es: ", self.__ocupacion)
        print("Su salario es: ", self.__salario)
        print("Sus dias de vacaciones son: ", self.__vacaciones)