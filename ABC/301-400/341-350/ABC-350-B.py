# ABC-350 B - Dentist Aoki
# https://atcoder.jp/contests/abc350/tasks/abc350_b
#
import collections


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, q = getIntMap()
    t = getIntList()

    ta = collections.Counter(t)
    for x in ta.values():
        if x % 2 == 1:
            n -= 1
    print(n)


if __name__ == "__main__":
    main()