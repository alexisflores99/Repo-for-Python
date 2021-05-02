from tkinter import *

root = Tk()
root.geometry("400x300")

w = Spinbox(root, values = ("Python", "html5","Java"))
w.pack()

r = Spinbox(root, values = ("Carne", "Agua","Queso"))
r.pack()

root.mainloop()