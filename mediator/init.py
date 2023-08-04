"""
    El mediator se usa para manejar una familia de objetos dentro de una misma instancia, se puede usar para notificar
    y enviar mensajes entre ellos, como en este ejemplo
"""

from components import Component

from mediator import Mediator


if __name__ == '__main__':

    # Create the mediator to handle all the components
    mediator = Mediator()

    component1 = Component(mediator, 'componenteMS')
    component2 = Component(mediator, 'ComponenteAS')
    component3 = Component(mediator, 'componenteCR')
    component4 = Component(mediator, 'ComponenteLS')
    
    # Adding every component to the mediator
    mediator.add(component1)
    mediator.add(component2)
    mediator.add(component3)
    mediator.add(component4)

    # Send whatever you want from the component you like, and all the componet are going to receive that you send
    component2.notify("Enviando un mensaje de angee")
    
