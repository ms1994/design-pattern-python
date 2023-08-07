from abc import ABCMeta, abstractstaticmethod

class IObservable(metaclass = ABCMeta):
    """
        Interface for subject object, can subscribe, unsubcribe and notify a observer
    """

    @abstractstaticmethod
    def subscribe(observer):
        """
            Abstract method to subscribe a subject to a observer.
        """

    @abstractstaticmethod
    def unsubscribe(observer):
        """
            Abstract method to unsuscribe a subject/observer.
        """

    @abstractstaticmethod
    def notify(observer):
        """
            Method to notify when a change is made. Update the observer
        """