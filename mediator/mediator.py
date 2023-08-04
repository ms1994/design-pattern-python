class Mediator:

    """
        Mediator that will handle all the component, had to have a add method and notify method.
    """

    def __init__(self) -> None:
        self.components = []

    def add(self, component):
        """
            Add a component to the mediator
        """

        self.components.append(component)

    def notify(self, msg, name_component):

        # Method to call receive from every component
        for comp in self.components:
            # Avoid the same component who send the info get call
            if comp.name != name_component:
                comp.receive(msg)

    