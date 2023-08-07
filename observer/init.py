"""
    The observer design pattern is use to monitorize change made for subjects from observers, you can have
    many observer for a one subject, or many subjects from one observer. You can subscribe observers to a subject
    
    Updated the observer whanever a subject is changed.
"""

from concrete_subject import Subject
from observer import Observer


if __name__ == '__main__':

    subject1 = Subject(name="Subject 1")
    subject2 = Subject("Subject 2")
    subject3 = Subject("Subject 3")

    observer = Observer(subject1, "ObserverA")

    # Notify from subject1
    #subject1.notify("Hello from subject1")

    # You can have one subject subscribe to different observers
    observer_2 = Observer(subject1, "Observer2")

    # Notify from subject1
    subject1.notify("Hello from subject1")

    # You can have one observer with differents subjects
    subject2.subscribe(observer)
    subject3.subscribe(observer)

    subject2.notify("This is a second subject")
    subject3.notify("Third subject hehe")

    # Unsubscribe a subject for a observer
    subject1.unsubscribe(observer)

    subject1.notify("Its me again!")
    subject2.unsubscribe(observer)
    subject2.subscribe(observer_2)
    subject2.notify("I made a change")