import sys
import tkinter
from tkinter import ttk

#CHECKBOX
window=tkinter.Tk()

def mifuncion():
    pass

#ETIQUETA titulo
username_label=ttk.Label(window,text="Marque los numeros pares de la lista")
username_label.grid(column=0,row=0,padx=5,pady=5)

window.columnconfigure(0,weight=1)
window.columnconfigure(0,weight=3)

selec1=tkinter.StringVar()
selec2=tkinter.StringVar()
selec3=tkinter.StringVar()
selec4=tkinter.StringVar()

checkbox=tkinter.Checkbutton(window,text="4",variable=selec1,command=mifuncion)
checkbox.grid(row=1, column=0)
checkbox=tkinter.Checkbutton(window,text="65",variable=selec2,command=mifuncion)
checkbox.grid(row=2, column=0)
checkbox=tkinter.Checkbutton(window,text="90",variable=selec3,command=mifuncion)
checkbox.grid(row=3, column=0)
checkbox=tkinter.Checkbutton(window,text="122243",variable=selec4,command=mifuncion)
checkbox.grid(row=4, column=0)



window.mainloop()