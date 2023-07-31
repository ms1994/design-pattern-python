"""
    Clase que ejecutara la orden del execute, que a su vez esta siendo ejecutado por las clases de command, child of interface 
"""

class Lights:

    def switch_on(self):
        print("Luces encendidas")

    def switch_off(self):
        print("Luces apagadas")