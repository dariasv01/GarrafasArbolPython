# This is a sample Python script.
from Model import Arbol as ar
from Model import Garrafa as gr

def check():
    return True

def transpasar(garrafaUno, garrafaDos, valorOldUno, valorOldDos):
    if (garrafaUno.getVNow() < garrafaUno.getVMax() and garrafaDos.getVNow() > 0):
        res = valorOldUno + valorOldDos
        if res >= garrafaUno.getVMax():
            if valorOldDos > valorOldUno:
                garrafaUno.llenar()
                garrafaDos.setVNow(res - garrafaUno.getVMax())
            elif (valorOldDos == valorOldUno):
                garrafaUno.llenar()
                garrafaDos.setVNow(res - garrafaUno.getVMax())
            else:
                garrafaUno.llenar()
                garrafaDos.setVNow(valorOldUno - valorOldDos)
        else:
            garrafaUno.setVNow(res)
            garrafaDos.setVNow(0)

    return [garrafaUno, garrafaDos]

garrafaUno = gr.Garrafa(0, 5)
garrafaDos = gr.Garrafa(0, 3)

# a = ar.ArbolN(None, [garrafaUno.get_capacidad() , garrafaDos.get_capacidad() ])

historicoGar = []
nodosPorExpan = []
nodosPorExpan.append([0, 0])

while ((garrafaUno.get_capacidad() + garrafaDos.get_capacidad()) != 7) & len(nodosPorExpan) < 0:
        capacidadInicalUno = garrafaUno.get_capacidad()
        capacidadInicalDos = garrafaDos.get_capacidad()
        if garrafaUno.get_capacidad() == 0:
            garrafaUno.llenar()
            if check():
                nodosPorExpan.append([garrafaUno.get_capacidad(), garrafaDos.get_capacidad()])
            garrafaUno.set_capacidad(capacidadInicalUno)
        if garrafaDos.get_capacidad() == 0:
            garrafaDos.llenar()
            if check():
                nodosPorExpan.append([garrafaUno.get_capacidad(), garrafaDos.get_capacidad()])
            garrafaDos.set_capacidad(capacidadInicalDos)
        if garrafaUno.get_capacidad() != 0:
            garrafaUno.vaciar()
            if check():
                nodosPorExpan.append([garrafaUno.get_capacidad(), garrafaDos.get_capacidad()])
            garrafaUno.set_capacidad(capacidadInicalUno)
        if garrafaDos.get_capacidad() != 0:
            garrafaDos.vaciar()
            if check():
                nodosPorExpan.append([garrafaUno.get_capacidad(), garrafaDos.get_capacidad()])
            garrafaDos.set_capacidad(capacidadInicalDos)

        historicoGar.append(garrafaUno.get_capacidad(), garrafaDos.get_capacidad())




# a.mostrar()

