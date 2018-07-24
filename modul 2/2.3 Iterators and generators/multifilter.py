class multifilter:
    def judge_half(pos, neg):
        return True if pos >= neg else False

    # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return True if pos >= 1 else False

    # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return True if neg == 0 else False

    # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    # iterable - исходная последовательность
    # funcs - допускающие функции
    # judge - решающая функция

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for j in self.funcs:
                if j(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i

    # возвращает итератор по результирующей последовательности


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
