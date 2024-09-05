# ABC-367 C - Enumerate Sequences
# https://atcoder.jp/contests/abc367/tasks/abc367_c
#
import itertools


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def comb(x, y):
    c = []
    for a, b in list(itertools.product(x, y)):
        a = [a] if type(a) is int else list(a)
        a.append(b)
        c.append(a)
    return c


def main():
    N, K = getIntMap()
    R = getIntList()

    if N > 1:
        a = []
        for i in range(N):
            b = []
            for j in range(R[i]):
                b.append(j + 1)
            a.append(b)

        x = comb(a[0], a[1])

        for i in range(2, N):
            x = comb(x, a[i])

        for y in x:
            if sum(y) % K == 0:
                print(" ".join(map(str, y)))


if __name__ == "__main__":
    main()
