from tkinter import *

root = Tk() 
imagen = PhotoImage(file = "jeje.gif")
label = Label(root, image = imagen)
label.pack()

"""
texto_nuevo = StringVar()
texto_nuevo.set("Python")

root.title("Bienvenidos")
root.config(width=400,height=300)


label = Label(root,text = "Hola mundo")
label.place(x = 100, y = 50)           #reemplaza al pack()
label.config(bg = "blue",fg = "white", font = ("Curier", 20))



label = Label(root,text = "Bienvenidos")
label.place(x = 100, y = 100)           #remplaza al pack()
label.config(bg = "red", fg = "white", font = ("Curier", 20), textvariable = texto_nuevo)
"""



root.mainloop()