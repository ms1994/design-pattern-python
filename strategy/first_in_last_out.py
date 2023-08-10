from interface import TicketOrdering

class FILOTicketOrdering(TicketOrdering):

    def create_ordering(self, listaTicket):
        # Copiamos los valores originales en una nueva variable
        reverse_list = listaTicket.copy()
        reverse_list.reverse()
        return reverse_list