class Buffer:
    def __init__(self):
        self.mas = []
        self.sum = 0

    def add(self, *a):
        for i in range(len(a)):
            lenmas = len(self.mas)
            if lenmas < 5:
                self.mas.append(a[i])
                self.sum += a[i]
            else:
                print(self.sum)
                self.sum = a[i]
                self.mas = [a[i]]
        if len(self.mas) == 5:
            print(self.sum)
            self.sum = 0
            self.mas = []

    def get_current_part(self):
        if len(self.mas) == 5:
            self.mas = []
            print(self.mas)
            return self.mas
        print(self.mas)
        return self.mas


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()
