#from observer.observable import IObservable
from observable import IObservable

class Subject(IObservable):
    """
        Subject object, object that are going to be monitorize for the observer interface.
    """
    _observers = None
    
    def __init__(self, name = 'subject') -> None:
        """Initialize set of observers"""
        self._observers = set()

        self.name = name

    def __str__(self) -> str:
        return "I'm %s" % self.name
    
    def subscribe(self, observer):

        self._observers.add(observer)

    def unsubscribe(self, observer):

        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        # Update every observer
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)
            # they are technique to avoid update all observer, and only the few that you want.
    

    