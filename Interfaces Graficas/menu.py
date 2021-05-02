from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label = "Nuevo Archivo")
archivoMenu.add_command(label = "Nueva Ventana")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir")

editarMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Editar", menu=editarMenu)
editarMenu.add_command(label="Deshacer")
editarMenu.add_command(label="Rehacer")

ayudaMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label = "Ver Licencia")
ayudaMenu.add_command(label = "Acerca de")



root.mainloop()