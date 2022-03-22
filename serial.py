class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initializes instance of SerialGenerator class with counting capabilities."""
        self.counter = start-1
        self.start = start

    def __repr__(self):
        return f"<SerialGenerator start = {self.start} counter = {self.counter}>"

    def generate(self):
        """Increments the instance's counter by 1, and returns count value."""
        self.counter+=1
        return self.counter

    def reset(self):
        """Resets the instance's counter to starting value. Returns None"""
        self.counter = self.start-1

serial = SerialGenerator(start=100)