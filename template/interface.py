from abc import ABCMeta, abstractmethod

class Trading(metaclass = ABCMeta):

    def connect(self):
        print("Connecting...")

    def get_market_data(self, coin):

        return [10, 20, 30, 45]

    
    @abstractmethod
    def should_buy(self, prices):
        """abstract method"""

    @abstractmethod
    def should_sell(self, prices):
        """abstract method"""

    def check_prices(self, coin):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}")
        elif should_sell:
            print(f"Your should sell {coin}")
        else:
            print("No action needed")