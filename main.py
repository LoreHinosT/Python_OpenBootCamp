import sys
import tkinter
from tkinter import ttk

#CHECKBOX
window=tkinter.Tk()
def salir(event):
    print("Adios")
    window.quit

def saludar(event):
    print("Han hecho click en saludar")

def saludarDobleClick(event):
    print("Han hecho doble click en saludar")

boton=tkinter.Button(window,text="Hax click")
boton.pack()
boton.bind("<Button-1>",saludar)
boton.bind("<Double-1>",saludarDobleClick)


botonSalida=tkinter.Button(window,text="Salida")
botonSalida.pack()
botonSalida.bind("<Button-1>",salir)

window.mainloop()