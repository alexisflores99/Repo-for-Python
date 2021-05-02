#Operador not
# print(not False)

#Operador and 
#print(True and False)

#Operador or
# print(True or False)

# c="Python"
# print(len(c)<8 or c[0] == "p")

print("Sistema de becas 2020")

kil=int(input("A cuantos kilometros de la escuela se encuentra: "))
her=int(input("Cunatos hermanos tiene en la escuela: "))
ing=int(input("De cuantos es el ingreso en su familia: "))

if kil < 10 and her <2 or ing < 1000:
    print("Tiene derecho a la beca")
else:
    print("No tiene derecho a una beca")