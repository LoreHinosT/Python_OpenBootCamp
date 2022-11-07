
def genListaPais():
    numeros=int(input("Ingrese la cantidad de paises"))
    cantidad=1
    paises={"prueba"}
    while cantidad<=numeros:
        pais=input("Ingrese pais")
        paises.add(pais)
        cantidad+=1
    paises.remove("prueba")
    return paises,type(paises)
print(genListaPais())