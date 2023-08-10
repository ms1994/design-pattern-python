from abc import ABC, abstractmethod

class TicketOrdering(ABC):

    @abstractmethod
    def create_ordering(self, listaTicket):
        """
            Abstract method que ejecutaran los hijos de la clase

            :Params listaTicket: Lista de metodos a procesar
            :Type listaTicket: list

            :Return list
        """
        pass