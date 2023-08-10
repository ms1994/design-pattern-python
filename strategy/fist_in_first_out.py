from interface import TicketOrdering

class FIFOTicketOrdering(TicketOrdering):

    def create_ordering(self, listaTicket):
        return listaTicket.copy()