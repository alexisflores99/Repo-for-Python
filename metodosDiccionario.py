diccionario = {
    "clave1" : 123,
    "clave2" : True,
    "clave3" : [1,2,3]
}

#print(type(diccionario["clave3"]))
#print(diccionario.keys())
#print(diccionario.values())
print(diccionario.items())

for i,c in diccionario.items():
    print(i,c)