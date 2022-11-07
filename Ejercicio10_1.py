import sys
import tkinter
from tkinter import ttk


window=tkinter.Tk()

def seleccionar():
    print(f"La opcion seleccionada es{seleccionado}")


window.columnconfigure(0,weight=1)
window.columnconfigure(0,weight=3)
seleccionado=tkinter.StringVar()
r1=ttk.Radiobutton(window,text="Opcion 1",value="1",variable=seleccionado,command=seleccionar)
r2=ttk.Radiobutton(window,text="Opcion 2",value="2",variable=seleccionado,command=seleccionar)
r3=ttk.Radiobutton(window,text="Opcion 3",value="3",variable=seleccionado,command=seleccionar)

r1.grid(column=0,row=1,pady=5,padx=5)
r2.grid(column=0,row=2,pady=5,padx=5)
r3.grid(column=0,row=3,pady=5,padx=5)

#BOTONES
reiniciar_button=ttk.Button(window,text="Reiniciar")
reiniciar_button.grid(column=0,row=4,sticky=tkinter.E,padx=5,pady=5)

window.mainloop()