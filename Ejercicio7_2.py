import time
#print(time.time())
#tiempo=time.strftime("%H:%M:%S")
#print(tiempo)

#fecha=time.strftime("%d/%m/%y")
#print(fecha)

#formato="%H"
#ahora=time.strftime(formato)
#print(ahora)
#print(int(ahora)<2)

#cumpleaños="3"
#cumpleaños=time.strptime(cumpleaños,"%H")
#print(cumpleaños)
#0 a 24 1111111111111111
#################
def irACasa():
    formato="%H"
    horaAct=time.strftime(formato)
    if int(horaAct)<19 and int(horaAct)>12:
        cantidad=19-int(horaAct)
        return f"Faltan {cantidad} horas para ir a casa"
    else:
        return f"Hora de ir a casa son las {horaAct}"

print(irACasa())
        