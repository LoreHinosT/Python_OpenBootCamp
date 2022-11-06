#import operaciones as op #IMPORTO OPERACIONES.PY PARA USAR LA FUNCION SUMA
# y luego la llamo o para que me quwde mas corto
from operaciones import *
import operaciones as op

#import op082.suma
def main(a=9,b=5):
    suma=op.suma(a,b)
    resta=op.resta(a,b)
    multiplicar=op.multiplicar(a,b)
    dividir=op.dividir(a,b)

    return suma,resta,multiplicar,dividir
    
print(main())