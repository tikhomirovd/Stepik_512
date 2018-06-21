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

    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
    # добавлены

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]

