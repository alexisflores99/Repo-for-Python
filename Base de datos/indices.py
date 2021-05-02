import sqlite3

conexion = sqlite3.connect("Productos.db") #Establecemos la conexion

cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE PRODUCTOS (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_P VARCHAR(20),
#         SECCION_P VARCHAR(20)
#     )
# ''')

# productos = [
#     ('Leche','Lacteos'),
#     ('Facturas','Panaderia'),
#     ('Asado','Carniceria')
# ]

cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'Cangrejo','Marisco')")

conexion.commit()
conexion.close()