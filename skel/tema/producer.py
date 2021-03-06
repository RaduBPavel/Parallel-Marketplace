"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time

class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time

    def run(self):
        prod_id = self.marketplace.register_producer()

        # Executes the associated publish operations in an infinite loop.
        while True:
            for product_info in self.products:
                product, quantity, wait_time = product_info[0], product_info[1], product_info[2]

                while quantity > 0:
                    return_code = self.marketplace.publish(prod_id, product)

                    if return_code:
                        quantity -= 1
                        time.sleep(wait_time)
                    else:
                        time.sleep(self.republish_wait_time)
