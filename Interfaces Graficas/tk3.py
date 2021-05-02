import tkinter as tk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title('Tkinter Color')
root.geometry('300x150')

def cambiarColor():
    colores = askcolor(title = "Tkinter Colores")
    root.configure(bg=colores[1])

tk.Button(
    root,
    text = "Cambiar color",
    command = cambiarColor
).pack(expand=True)

root.mainloop()
