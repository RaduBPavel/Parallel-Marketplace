Name: Pavel Radu-Bogdan
Group: 334CA
Faculty: Faculty of Automatic Control and Computer Science, UPB

# Assignment no. 1
#### Parallel Marketplace

***Assignment purpose***
* The purpose of this assignment was to simulate the Multiple Producer Multiple Consumers (MPMC) scenario.
* In order to simulate this scenario, the following context was given: the objective was to simulate how
products are produced and sold in a marketplace, by multiple producers and multiple consumers at the same time.

***Assignment structure***
* The main logic of the assignment is implemented in three .py files: marketplace.py, consumer.py and producer.py
* The marketplace, which acts as the broker between the producers and consumers, has all the logic implemented
inside it, which consists of: registering producers and carts of consumers, publishing the products of producers
and adding and removing products from user's carts.
* The producer and consumer entities use the methods declared inside the Marketplace class to simulate their
functionalities.

***Implementation details***
* Some of the most important elements used in constructing the Marketplace methods logic are:
    * dictionaries used to store data regarding the products on the market (more specifically, defaultdicts from
    the collections module) and Python lists
    * synchronization mechanisms in the form of Locks, imported from the threading module
* By using these elements, synchronization is achieved. The Python data structures are mostly atomic in nature,
due to the usage of GIL (Global Interpreter Lock) and, where it is needed (for example incremental operations),
locks are used to ensure synchronization.

***Resources and other observations***
* More info regarding the GIL can be found in these articles:
    * [What is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)
    * [Grok the GIL: How to write fast and thread-safe Python](https://opensource.com/article/17/4/grok-gil)
* In short, the GIL is used to run programs that use multi-threading in a single-thread mode, in order to have
backwards compatibility with the underlying C and C++ modules used (when using the CPython Compiler).
Other compilers, such as IronPython or Jython, don't use the GIL in their implementation.
* The GitHub repo of this project can be found [here](https://github.com/RaduBPavel/Parallel-Marketplace).
