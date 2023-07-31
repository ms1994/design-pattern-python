"""
    Clase para ejecutar el command switch_on (encendido), cada vez que se quiera encender el objeto, no importar que objeto, se usa
    esta clase
"""

from interface import ICommand

class SwithOnCommand(ICommand):

    def __init__(self, light):
        """
            Crea una referencia al receiver y lo guardar en una variable privada

            :Params light: objeto que funjira como el reciver y ejecutar la orden dada
            :Type light: class, es un receiver
        """
        
        self._light = light

    # Metodo heredado del Icommand
    def execute(self):
        # Ejecuta el swith on del receiver porque estamos en la clase switch on
        self._light.switch_on()