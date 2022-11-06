def escribe(fichero,datos):
    f=open(fichero,"w") #LA W ES PARA INDICAR QUE VOY A ESCRIBIR#
    for linea in datos:
        if not linea.endswith("\n"):
            linea=linea+"\n"
        f.write(linea)
    f.close(linea)
lista=[
    "una linea",
    "dos lineas",
    "tres lineas",
]