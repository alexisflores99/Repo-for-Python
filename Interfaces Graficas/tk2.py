import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title('Mi Aplicacion')
        self.geometry('300x50')

        self.label = ttk.Label(self, text = 'Hola Tkinter')
        self.label.pack()

        self.boton = ttk.Button(self, text = 'Haz click aqui')
        self.boton['command'] = self.boton_accion
        self.boton.pack()

    def boton_accion(self):
        showinfo(title = 'Informacion', message= 'Hola mundo')


if __name__ == "__main__":
    app = App()
    app.mainloop()
