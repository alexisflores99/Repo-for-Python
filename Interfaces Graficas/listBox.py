from tkinter import *

root = Tk() 
root.geometry("400x400")

productos = Label(root, text = "Productos")
productos.pack()

def agregar():
    if entrada.get() != "":
        listaProductos.insert(END, entrada.get())

def eliminar():
    #listaProductos.delete(END)
    for i in range(listaProductos.size()):
        if entrada.get() == listaProductos.get(i):
            listaProductos.delete(i)

listaProductos = Listbox(root,width=50)
listaProductos.insert(0,"Agua")
listaProductos.insert(1,"Maiz")
listaProductos.insert(2,"Carne")
listaProductos.pack()

entrada = Entry(root, bd =10)
entrada.pack()

boton = Button(root,text = "Agregar producto")
boton.config(command=agregar)
boton.pack()

boton2 = Button(root,text = "Eliminar producto")
boton2.config(command=eliminar)
boton2.pack()

root.mainloop()