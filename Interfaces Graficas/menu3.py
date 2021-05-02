from tkinter import *
from tkinter import filedialog

root = Tk()

def abrir():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="Descargas", filetypes=(("Documento Texto","*.txt"),("Documento Excel","*.xlsx")))
    print(archivo)

Button(root,text="Archivos", command=abrir).pack()


root.mainloop()