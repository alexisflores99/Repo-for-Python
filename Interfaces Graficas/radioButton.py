from tkinter import *

def mostrar():
    if opciones.get() == 1:
        label2.config(text="Has elegido Masculino")        
    else:
        label2.config(text="Has elegido femenino")

root = Tk() 

opciones = IntVar()

label = Label(root, text="Escoge tu orientacion")
label.pack()
label.config(bd=4,bg="red")


Radiobutton(root,text="Masculino",variable=opciones, value=1, command=mostrar).pack()

Radiobutton(root,text="Femenino",variable=opciones,value=2,command=mostrar).pack()

label2 = Label(root)
label2.pack()
label2.config(bg="Blue")


root.mainloop()