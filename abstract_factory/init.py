"""
    La factoria abstracta devuelve una instancia a una factoria, y en esta factoria se decide que tipo de clase utilizar
    y usando el interface todas esas clases tienen las mismas propiedades
"""

from abstract_factory import FurnitureFactory

if __name__ == '__main__':
    mesas = ['MesaGrande', 'MesaMediana', 'MesaChiquita']

    sillas = ['SillaGrande', 'SillaMediana', 'SillaChiquita']
    contS = 0
    contT = 0
    for i in range(6):
        
        if i % 2:
            utensilio = FurnitureFactory.get_furniture(sillas[contS])
            if contS < 3:
                contS += 1
        else:
            utensilio = FurnitureFactory.get_furniture(mesas[contT])

            if contT < 3:
                contT += 1
            
        print(utensilio.get_dimensions())
 