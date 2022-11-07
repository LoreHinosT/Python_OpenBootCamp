from functools import reduce

def ListaGeneradora():
    cantList=int(input("Ingrese el tamaño de lista"))
    lista=[]
    for i in range(cantList):
        valor=int(input("Ingrese un valor"))
        lista.append(valor)
    return lista
def mifuncionImpar(x):
    if x %2 !=0:
        return True
    return False

resultado=filter(mifuncionImpar, ListaGeneradora()) 
resultado=list(resultado)
print(f"Los numeros impares son: {resultado}")

def suma(a,b):
    return a+b

res=reduce(suma,resultado)
print(f"Y su suma da: {res}")