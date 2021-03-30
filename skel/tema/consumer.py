"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a consumer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """

        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.operations = {'add': self.marketplace.add_to_cart,
                            'remove': self.marketplace.remove_from_cart}

    def run(self):
        # For each cart that the customer has, execute the associated operations.
        for cart in self.carts:
            cart_id = self.marketplace.new_cart()

            for action in cart:
                action_type = action['type']
                product, quantity = action['product'], action['quantity']

                while quantity > 0:
                    return_code = self.operations[action_type](cart_id, product)

                    if return_code:
                        quantity -= 1
                    else:
                        time.sleep(self.retry_wait_time)

            # After finishing the operations, print the contents of the cart.
            for item in self.marketplace.place_order(cart_id):
                print('{} bought {}'.format(self.name, item))
