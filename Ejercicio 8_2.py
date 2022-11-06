import pickle
class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
    def getColor(self):
        return self.color
    def getRuedas(self):
        return self.ruedas
    def getPuertas(self):
        return self.puertas

bicicleta=Vehiculo("Rojo",2,0)

f=open("datos.bin","wb")
pickle.dump(bicicleta,f)
f.close()

f=open("datos.bin","rb")
rojo=pickle.load(f)
f.close()

