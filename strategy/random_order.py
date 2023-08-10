from interface import TicketOrdering
import random


class RandomTicketOrdering(TicketOrdering):

    def create_ordering(self, listaTicket):
        # Copiamos los valores originales en una nueva variable
        random_list = listaTicket.copy()
        # Variamos la lista
        random.shuffle(random_list)
        return random_list