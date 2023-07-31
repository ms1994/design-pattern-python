from interface import IChain

class Dispenser50(IChain):

    """
        Concrete class to dispenser 50$ from the amount
    """

    def __init__(self) -> None:
        
        self.successor = None

    def handle(self, amount):

        if amount >= 50:
            # How many times can I substract 50 from the amount
            times = amount // 50

            # Reminder
            rem = amount % 50

            print(f"Dispenser {times} 50$ from this amount {amount}")

            if rem != 0:
                self.successor.handle(rem)
        else:
            self.successor.handle(amount)
                
    
    def set_successor(self, successor):
        # Attach the next chain to 50 dispenser
        self.successor = successor

class Dispenser20(IChain):

    """
        Concrete class to dispenser 20$ from the amount
    """

    def __init__(self) -> None:
        
        self.successor = None

    def handle(self, amount):

        if amount >= 20:
            # How many times can I substract 20 from the amount
            times = amount // 20

            # Reminder
            rem = amount % 20

            print(f"Dispenser {times} 20$ from this amount {amount}")

            if rem != 0:
                self.successor.handle(rem)
        else:
            self.successor.handle(amount)
                
    
    def set_successor(self, successor):
        # Attach the next chain to 20 dispenser
        self.successor = successor


class Dispenser10(IChain):

    """
        Concrete class to dispenser 10$ from the amount
    """

    def __init__(self) -> None:
        
        self.successor = None

    def handle(self, amount):

        if amount >= 10:
            # How many times can I substract 10 from the amount
            times = amount // 10

            # Reminder
            rem = amount % 10

            print(f"Dispenser {times} 10$ from this amount {amount}")

            if rem != 0:
                self.successor.handle(rem)
        else:
            self.successor.handle(amount)
                
    
    def set_successor(self, successor):
        # Attach the next chain to 10 dispenser
        self.successor = successor