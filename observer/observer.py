from observer_interfac import IObserver

class Observer(IObserver):

    def __init__(self, observable, name = 'default') -> None:
        """
            Initialize the observer object and pass a subject that is going to monitorize
            
        """
        # Subscribe a subject to this observer
        observable.subscribe(self)
        self.name = name

    def notify(self, observable, *args, **kwargs):

        print("Observer %s is received a call from" % self.name, observable, args, kwargs)