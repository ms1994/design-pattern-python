from concrete_chain import Dispenser50, Dispenser20, Dispenser10

class ChainDispenser:

    """
        Class to group all the dispenser and initializer to chain one to another
    """

    def __init__(self) -> None:
        # Create the objects Ichain for different dispenser
        self.dispenser_50 = Dispenser50()
        self.dispenser_20 = Dispenser20()
        self.dispenser_10 = Dispenser10()

        # Chain every dispenser carefully

        self.dispenser_50.set_successor(self.dispenser_20)

        self.dispenser_20.set_successor(self.dispenser_10)