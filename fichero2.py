from io import open

fichero = open("Archivo2.txt","r")
# fichero.seek(10) #nos muestra a partir del caracter que nosotros indiquemos
# print(fichero.read())

# fichero.close()

# fichero.seek(len(fichero.read())/2) #podemos leer a partir de la mitad

# texto = "Hola esta es otra linea pajin\nArgentino sorete\nAdios"
print(fichero.readlines())
fichero.close()
