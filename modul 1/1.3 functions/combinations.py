def comb(n, k):
    if k > n:
        return 0

    if k == 0:
        return 1

    else:
        return comb(n - 1, k) + comb(n - 1, k - 1)


n, k = map(int, input().split())

print(comb(n, k))
