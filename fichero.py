from io import open

fichero = open("archivo.txt","a") #creacion y la apertura

#texto = "Hola mundo\nEstudio python"
#fichero.write(texto) #manipulacion
#fichero.close() #cierre

# texto = fichero.read()
# fichero.close()
# print(texto)

# linea = fichero.readlines()
# fichero.close()
# print(linea[0])
fichero.write("\n Esto es el metodo append")
fichero.close()
print(fichero)