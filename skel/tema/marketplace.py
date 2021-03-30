"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from threading import Lock
from collections import defaultdict, deque

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.products = defaultdict(deque)
        self.queue_sizes = {}
        self.carts = {}

        self.publish_lock = Lock()
        self.add_lock = Lock()
        self.remove_lock = Lock()
        self.place_lock = Lock()

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        self.queue_sizes[len(self.queue_sizes)] = 0
        return len(self.queue_sizes) - 1

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        with self.publish_lock:
            if self.queue_sizes[producer_id] == self.queue_size_per_producer:
                return False

            self.queue_sizes[producer_id] += 1
            self.products[product].append(producer_id)

            return True


    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """

        # No need for synchronization, as the following operation is atomic
        self.carts[len(self.carts)] = defaultdict(deque)
        return len(self.carts) - 1

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """

        with self.add_lock:
            if not self.products[product]:
                return False

            prod_id = self.products[product].popleft()
            self.queue_sizes[prod_id] -= 1
            self.carts[cart_id][product].append(prod_id)

            return True

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        with self.remove_lock:
            if not self.carts[cart_id][product]:
                return False

            prod_id = self.carts[cart_id][product].popleft()
            self.queue_sizes[prod_id] += 1
            self.products[product].append(prod_id)

            return True

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        with self.place_lock:
            result = []

            for product in self.carts[cart_id]:
                result.extend([product for _ in range(len(self.carts[cart_id][product]))])

            return result
