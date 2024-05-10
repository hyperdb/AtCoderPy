# ABC-334 C - Socks 2
# https://atcoder.jp/contests/abc334/tasks/abc334_c
#
import itertools


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    a = getIntList()

    if k % 2 == 0:
        d = 0
        for i in range(0, k, 2):
            d += (a[i + 1] - a[i])
        print(d)
    else:
        l = [0] + [a[i + 1] - a[i] for i in range(0, k // 2 * 2, 2)]
        r = [0] + [a[i] - a[i - 1] for i in range(k // 2 * 2, 0, -2)]

        ld = list(itertools.accumulate(l))
        rd = list(itertools.accumulate(r))
        rd.reverse()

        d = 10 ** 5
        for i in range(k // 2 + 1):
            d = min(ld[i] + rd[i], d)
        print(d)


if __name__ == "__main__":
    main()

