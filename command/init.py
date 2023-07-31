"""
    Archivo del client donde se configurara el command y se llamaran a los distintos command y sus receiver

    El command design patter sirve para ejecutar distintos comandos cada uno con su clase, y todos ellos deben tener
    la funcion principal del interface, el command pattern se usa tambien para implementar el hacer/desacer metodo

    creando un metodo desacer en el interface y en cada commando hara lo contrario por ejemplo en el switch_on class
    el metodo desacer lo que hara sera apagar la luz (switch_off)
"""
from operator import inv
from time import sleep
from receiver import Lights
from command_on import SwithOnCommand
from command_off import SwithOffCommand
from invoker import Switch

if __name__ == '__main__':
    # creamos nuestro objeto del receiver que sera el que ejecutara los comandos, sean cual fuesen
    bombillo = Lights()

    # Creamos nuestros commandos, y le pasamos el receiver para que lo ejecuten internamente
    comando_encender = SwithOnCommand(bombillo)
    comando_apagar = SwithOffCommand(bombillo)

    # Creamos el invoker que sera el que registre los comando y los ejecute, segun el ordern que queremos
    invoker = Switch()

    # Registramos comando encender y la clase que lo ejecutara
    invoker.register_command('on', command=comando_encender)

    
    # Registramos comando apagado y la clase que lo ejecutara
    invoker.register_command('off', command=comando_apagar)


    # Ejecutamos los comando que queremos
    invoker.execute('on')
    sleep(1)
    invoker.execute('off')
    

    print(invoker.history)
