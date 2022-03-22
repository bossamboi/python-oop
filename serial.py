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
        self.next_serial = self.start = start

    def __repr__(self):
        return f"<SerialGenerator start = {self.start} next_serial = {self.next_serial}>"

    def generate(self):
        """Increments the instance's next_serial by 1, and returns count value."""
        self.next_serial+=1
        return self.next_serial-1

    def reset(self):
        """Resets the instance's next_serial to starting value. Returns None"""
        self.next_serial = self.start

serial = SerialGenerator(start=100)