import sqlite3

conexion = sqlite3.connect("Productos.db") #Establecemos la conexion

cursor = conexion.cursor()

# cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION_P = 'Panaderia'")
# productos = cursor.fetchall()
# print(productos)

# cursor.execute("UPDATE PRODUCTOS SET SECCION_P='PANADERIA' WHERE SECCION_P='Panaderia'")

cursor.execute("DELETE FROM PRODUCTOS WHERE ID = 2")

conexion.commit()
conexion.close()