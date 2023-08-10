"""
    El enfoque del strategy pattern es usar una instancia (objeto) de una clase, dentro de otra, pudiendo cambiar 
    su comportamiento en runtime, por ejemplo la clase process ticket, uno de sus metodos acepta una variable de tipo
    ticketOrdering (Parent class), pero nosotros le vamos a pasar es su hijo (FIFOTicket, FILOTicket o randomTIcket), esto
    se llama poliformismo, como son hijos de la clase tipo ticketProcess pueden cambiar su comportamiento.

    Asi dentro de la clase process ticket podemos usar el metodo de procesamiento de manera dinamica, solo cambiando
    la instancia o la clase del metodo que queremos ya sea first in, last out, o random.
"""


from first_in_last_out import FILOTicketOrdering
from fist_in_first_out import FIFOTicketOrdering
from random_order import RandomTicketOrdering

class ProcessTiket():

    tickets = []

    def crear_ticket(self, ticket_asunto):
        """
            :Params tickt_asunto: asunto del ticket a procesar
        """


        self.tickets.append(ticket_asunto)
    
    def process_ticket(self, process_strategy):
        """
            Funcion para procesar los tickets segun diferentes estrategias

            :Params process_strategy: clase segun lo que se vaya a utilizar
        """

        tickets = process_strategy.create_ordering(listaTicket = self.tickets)

        for index,ticket in enumerate(tickets):
            print("ticket %s :" % (index + 1 ))
            print(ticket)


if __name__ == '__main__':

    ticket = ProcessTiket()

    ticket.crear_ticket("Lino se fue")
    ticket.crear_ticket("Angee se tira peos")
    ticket.crear_ticket("Carmen se porta mal")
    ticket.crear_ticket("A miquel le ira bien")

    # Procesar los ticket segun la clase que quieras, puede ser FIFO o FILO o RANDOM
    ticket.process_ticket(RandomTicketOrdering())


