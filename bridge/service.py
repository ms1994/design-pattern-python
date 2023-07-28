"""
    Interface for the services what is the abstract class to define different services like youtube, twitch, etc.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
"""
    dataclass te permite escribir una clase de forma mas facil, simplemente definiendo su tipo.

    El field method de las dataclass se usa para pasar una funcion como inicializador de un valor, con eso impide
    que diferentes objetos tengan el mismo punto en memoria
"""

@dataclass
class Service(ABC):
    # in the example he create a new kind of type call it BUffer that is a string
    devices: list = field(default_factory=list)

    # Agrega devices al service, el device es una instancia a otra class
    def add_devices(self, device):
        self.devices.append(device)

    # los muestra
    def retrieve_buffer_data(self):
        return self.devices

    """
        Abstract methods to implement for every specific services
    """
    
    @abstractmethod
    def start_stream(self):
        pass

    
    @abstractmethod
    def stop_stream(self, stream_reference):
        pass

    @abstractmethod
    def fill_buffer(self, stream_reference):
        pass