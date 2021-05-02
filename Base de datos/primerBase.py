import sqlite3

conexion = sqlite3.connect("PrimerBase.db") #Establecemos la conexion




# conexion.close() #cerramos la conexion

cursor = conexion.cursor()
# cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))")

# cursor.execute("INSERT INTO USUARIOS VALUES('ALEXIS',21,'MASCULINO')")



# cursor.execute("SELECT * FROM USUARIOS")
# usuario = cursor.fetchone()
# print(usuario)


# usuarios = [
#     ('Hector',21,'Masculino'),
#     ('Ana',50,'Femenino'),
#     ('Javier',28,'Masculino')
# ]

# cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)", usuarios)


cursor.execute("SELECT * FROM USUARIOS")
usuarios = cursor.fetchall()
print(usuarios)

for i in usuarios:
    print(i)

conexion.commit()
conexion.close()