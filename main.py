import operaciones as op #IMPORTO OPERACIONES.PY PARA USAR LA FUNCION SUMA
# y luego la llamo o para que me quwde mas corto
import op2.suma
def main():
    res=op.suma(2,2)
    res2=op2.suma.suma(2,5)
    return res2 
    

print(main())