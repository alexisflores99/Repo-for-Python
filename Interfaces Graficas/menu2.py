from tkinter import *
from tkinter import messagebox

def salir():
    i = messagebox.askquestion("Salir","¿Estás seguro que deseas salir?")
    if i == "yes":
        root.destroy()

def acerca():
    messagebox.showinfo("Informacion", "Creado por Alexis Flores")

def licencia():
    messagebox.showinfo("Licencia","Producto Open Source")

def error():
    messagebox.showerror("Error","Se ha producido un error papi")

def deshacer():
    messagebox.askquestion("¿Deshacer?","¿Estas seguro pa?")

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label = "Nuevo Archivo")
archivoMenu.add_command(label = "Nueva Ventana", command=error)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir", command=salir)

editarMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Editar", menu=editarMenu)
editarMenu.add_command(label="Deshacer",command=deshacer)
editarMenu.add_command(label="Rehacer")

ayudaMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label = "Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label = "Ver Licencia", command=licencia)
ayudaMenu.add_command(label = "Acerca de", command=acerca)



root.mainloop()