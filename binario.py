import pickle



fichero = open("lista_nombres","wb") #modo escritura y binario

# pickle._dump(lista, fichero)
# fichero.close()

lista = pickle.load(fichero) #para leer el archivo binario

print(lista)
