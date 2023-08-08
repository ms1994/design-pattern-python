"""
    The state design patter you will make a lot of state class that implement the same method as a order class
    but the internal state change will be handle by the state class internally, depend in what situation you are.
"""
from context import Context
if __name__ == '__main__':

    order = Context()
    # Check what state we are initially
    print(order.state)
    # Begin make a pay for one product
    order.receive_payment()
    # Check what state we are after some method
    print(order.state)

    # Ship the order
    order.ship()
    
    # Check what state we are after some method
    print(order.state)

    # Delivered the product
    order.mark_delivered()

    # Check what state we are after some method
    print(order.state)
