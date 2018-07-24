import itertools


def primes():
    pr = [2, 3]
    last = [2, 3]
    yield 2
    yield 3
    while True:
        cand = pr[-1] + 2
        i = 0
        while i < len(pr):
            while last[i] < cand:
                last[i] += pr[i]
            if last[i] == cand:
                cand += 2
                i = 0
            i += 1
        pr.append(cand)
        last.append(cand)
        yield cand


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
