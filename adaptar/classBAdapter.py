from classAInterface import AInterface
from classBInterface import BInterface
class BAdapter(AInterface):
    """
        Adapter design pattern que instance un objeto de la clase B, y la usa dentro de los
        metodos de la clase A interface.
    """
    OBJETO_B = None

    def __init__(self, objeto_b) -> None:
        self.OBJETO_B = objeto_b
    
    def method_a(self):
        print("Adapter")
        self.OBJETO_B.method_b()