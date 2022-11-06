f=open("fichero_e8_1","w")
lista=[
    "Linea 1 \n",
    "Linea 2 \n",
    "Linea 3 \n"
]

f.writelines(lista)
f.close()

f=open("fichero_e8_1","r")
print(f.read())
f.close()
