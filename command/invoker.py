"""
    Clase que se utiliza para invocar (ejecutar) el command pattern, puede ejecutar en nuestro ejemplo el switch on o el 
    switch off, no le importa el nombre del child ella solo registra icommand class
"""
from datetime import datetime

class Switch:

    def __init__(self):
        self._commands = {}
        # Adicional uno, crear una list para llevar un registro de los comando utilizado
        self._history = []
    def register_command(self, command_name, command):
        """
            Metodo que registra un comando en base a su nombre (key)

            :Params command_name: nombre del comando, puede ser el nombre de su clase
            :Type command_name: str

            :Params command: Comando para ejecutar
            :Type command: ICommand (el child)
        """

        self._commands[command_name] = command

    def execute(self, command_name):
        """
            Funcion para ejecutar el command_name, no confundir este metodo con la del interface, se llaman igual por comodidad
            y para senalar que se usa para invocar el command

            :Params command_name: nombre del comando
            :Type command_name: str
        """

        if command_name in self._commands:
            # executamos el command (switch_on o swithc_off puede ser cualquiera)
            self._commands[command_name].execute()
            # Adicional 1, guardamos el command name que utilizamos
            self._history.append({command_name: datetime.now().strftime('%d/%m/%Y, %H:%M:%S')})
        else:
            print("Command %s no register" % command_name)

    # Senala que no es un metodo en si, si no una propiedad como invoker.history
    @property
    def history(self):
        return self._history