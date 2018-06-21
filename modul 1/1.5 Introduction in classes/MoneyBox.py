class MoneyBox:
    def __init__(self, capacity, now=0):
        self.capacity = capacity
        self.now = now

    def can_add(self, v):
        return True if self.now + v <= self.capacity else False

    def add(self, v):
        self.now += v

