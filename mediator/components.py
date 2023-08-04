from interface import IComponent

class Component(IComponent):
    """
        Todos los component son de una misma familia (parent interface)
    """
    
    def __init__(self, mediator, name):
        
        self.mediator = mediator
        self.name = name
    

    def notify(self, msg):
        # Enviamos mensaje para mostrar que el metodo notify del component se esta ejecutando
        print(self.name + ">>>> OUT >>>> " + msg)

        # call the notify method in the mediator (with that the others component in the mediator are going to know what component is running)
        self.mediator.notify(msg, self.name)

    def receive(self, msg):
        # Know when a component call receive method
        print("Receiving from component " + self.name + " <<<<<<< IN <<<<<< : " + msg)


