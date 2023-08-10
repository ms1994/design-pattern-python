from interface import Trading

class AverageStrategy(Trading):
    """
        Se implementaran solo las estrategias abstract del template method, puede ser ambas o una sola
    """
    def list_average(self, l):
        return sum(l) / len(l)

    def should_buy(self, prices):
        """
            Return a boolean to say if should buy or not
        """
        return prices[-1] < self.list_average(prices)

    
    def should_sell(self, prices):
        return prices[-1] > self.list_average(prices)


class MinMaxStrategy(Trading):
    """
        Otra concrete class que implementara los abstract methods
    """

    def should_buy(self, prices):
        return prices[-1] == min(prices)

    
    def should_sell(self, prices):
        return prices[-1] == max(prices)