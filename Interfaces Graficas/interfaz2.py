from tkinter import *

root = Tk()     #creamos la ventana
root.title("Alexis")    #cambiamos el tiyulo
root.resizable(1,1)     #para cambiar el tamaño si queremos          
root.iconbitmap("cosmo.ico")    #para cambiar la imagen de la app
#root.geometry("600x352")        #para cambiar el tamaño manualmente        

miFrame = Frame(root)
miFrame.pack(fill="y", expand = 1)                      #lo empaquetamos
miFrame.config(width = 400, height = 350)   #le ponemos alturay anchura
miFrame.config(cursor = "pirate")             #para cambiar el cursor
miFrame.config(bg = "red")                  #para cambiar el color
miFrame.config(bd = "20")                   #para cambiar el tamaño del borde
miFrame.config(relief = "sunken")           #para cambiar el modelo del borde

root.config(cursor = "boat")             
root.config(bg = "blue")                 
root.config(bd = "25")
root.config(relief = "ridge")

root.mainloop()